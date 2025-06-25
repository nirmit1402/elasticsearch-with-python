from elasticsearch import Elasticsearch
from src.config import ES_HOST, ES_PORT, INDEX_NAME

def by_district(district: str, size: int = 10):
    es = Elasticsearch(hosts=[{"host": ES_HOST, "port": ES_PORT}])
    res = es.search(
        index=INDEX_NAME,
        size=size,
        query={"match": {"District": district}}
    )
    print(f"Found {res['hits']['total']['value']} results for '{district}':")
    for hit in res["hits"]["hits"]:
        src = hit["_source"]
        print(f" • {src['Hospital_Name']} — {src['Location']}")

if __name__ == "__main__":
    import sys
    district = sys.argv[1] if len(sys.argv) > 1 else "Anantapur"
    by_district(district)
