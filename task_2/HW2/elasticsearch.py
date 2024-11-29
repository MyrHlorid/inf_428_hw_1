import numpy as np
from elasticsearch import Elasticsearch, helpers
import matplotlib.pyplot as plt

# Генерация случайных данных для уровня угроз
def generate_random_data(mean, variance, num_samples):
    return np.random.randint(max(mean - variance, 0), min(mean + variance + 1, 90), num_samples)

# Подключение к Elasticsearch
es = Elasticsearch()

# Загрузка данных в Elasticsearch
def upload_to_elasticsearch(index_name, departments):
    actions = []
    for department in departments:
        data = {
            "department": department["name"],
            "scores": department["scores"].tolist()  # Преобразуем numpy массив в список
        }
        actions.append({
            "_index": index_name,
            "_source": data
        })
    helpers.bulk(es, actions)

# Чтение данных из Elasticsearch
def read_from_elasticsearch(index_name):
    res = es.search(index=index_name, body={"query": {"match_all": {}}}, size=10000)
    department_data = []
    for hit in res["hits"]["hits"]:
        department_data.append(hit["_source"]["scores"])
    return department_data
