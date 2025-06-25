# 🚑 Hospital Indexer

A utility to bulk index hospital data from CSV into Elasticsearch, with support for geo-point indexing and district-based search.

---

## Quick-start

```bash
# Clone this repo
cd hospital-indexer

# Create a virtual environment
python -m venv .venv && source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the indexer
python -m src.index_hospitals data/hospital_directory_sample.csv

# Try a sample query
python -m src.search_examples anantapur
