import os

ES_HOST: str = os.getenv("ES_HOST", "localhost")
ES_PORT: int = int(os.getenv("ES_PORT", 9200))
INDEX_NAME: str = os.getenv("ES_INDEX", "hosp")

MAPPING: dict = {
    "settings": {
        "number_of_shards": 2,
        "number_of_replicas": 1
    },
    "mappings": {
        "dynamic": True,
        "properties": {
            "Location_Coordinates": {"type": "geo_point"}
        }
    }
}
