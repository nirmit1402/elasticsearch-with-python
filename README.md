# 🚑 Hospital Indexer

A tiny utility that cleans a MoHFW-style hospital directory CSV, creates an
Elasticsearch index with a **geo_point** field, and bulk-loads every row.
A sample search script shows how to query by district name and/or by
geo distance.

> Tested on **Python 3.10+** and **Elasticsearch 8.x**.

---

## Quick-start

```bash
# 1. clone / unpack this repo
cd hospital-indexer

# 2. create a virtual env
python -m venv .venv && source .venv/bin/activate

# 3. install deps
pip install -r requirements.txt

# 4. set ES connection details
export ES_HOST=localhost
export ES_PORT=9200

# 5. run the indexer (replace CSV path if needed)
python -m src.index_hospitals data/hospital_directory_sample.csv
