from elasticsearch import Elasticsearch 
from elasticsearch import helpers
from elasticsearch_dsl.connections import connections
import csv

filename = 'sentiment_file.csv'

es = Elasticsearch(hosts=["https://admin:UFEHWTCNLMWJPMYB@portal-ssl1069-26.bmix-dal-yp-9125e16e-d33b-4653-821a-d337a1ee72d8.3753951333.composedb.com:57498/"], timeout=5000) # Define a default Elasticsearch client


with open(filename, "r", encoding="utf8") as f:
    reader = csv.DictReader(f)
    helpers.bulk(es, reader, index='sentiment_analysis_elastic_search', doc_type='application/json')
    
    
    
