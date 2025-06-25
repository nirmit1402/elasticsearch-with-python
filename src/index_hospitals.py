import sys
from pathlib import Path
import pandas as pd
from elasticsearch import Elasticsearch, helpers
from src.config import ES_HOST, ES_PORT, INDEX_NAME, MAPPING

def parse_geo_point(coord_str: str):
    try:
        lat, lon = map(float, coord_str.split(","))
        return {"lat": lat, "lon": lon}
    except Exception:
        return None

def preprocess(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df.fillna("Not Available", inplace=True)
    df["Location_Coordinates"] = df["Location_Coordinates"].apply(parse_geo_point)
    df.dropna(subset=["Location_Coordinates"], inplace=True)
    df.drop_duplicates(subset=["Sr_No"], inplace=True)
    return df

def build_actions(df: pd.DataFrame):
    for rec in df.to_dict(orient="records"):
        yield {
            "_op_type": "index",
            "_index": INDEX_NAME,
            "_id": rec["Sr_No"],
            **rec,
        }

def main(csv_path):
    es = Elasticsearch(hosts=[{"host": ES_HOST, "port": ES_PORT}])

    if not es.indices.exists(index=INDEX_NAME):
        es.indices.create(index=INDEX_NAME, body=MAPPING)

    df = pd.read_csv(csv_path)
    df = preprocess(df)

    helpers.bulk(es, build_actions(df))
    es.indices.refresh(index=INDEX_NAME)
    print(f"Indexed {len(df)} documents into '{INDEX_NAME}'.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Usage: python -m src.index_hospitals <csv_path>")
    main(Path(sys.argv[1]))
