from elasticsearch import Elasticsearch, helpers

# Настройка подключения
es = Elasticsearch("http://localhost:9200")

# Создание индекса Elasticsearch
def create_index(index_name):
    if es.indices.exists(index=index_name):
        es.indices.delete(index=index_name)  # Удаляем старый индекс
    mappings = {
        "mappings": {
            "properties": {
                "time_of_day": {"type": "integer"},
                "threat_score": {"type": "integer"}
            }
        }
    }
    es.indices.create(index=index_name, body=mappings)
    print(f"Index {index_name} created.")

# Заполнение индекса данными
def populate_index(index_name, data):
    actions = [
        {
            "_index": index_name,
            "_source": record
        }
        for record in data
    ]
    helpers.bulk(es, actions)
    print(f"Index {index_name} populated with data.")

# Пример использования
index_name = "threat_scores"
create_index(index_name)

if data:
    # Конвертация данных в нужный формат
    elastic_data = [
        {"time_of_day": int(record["time_of_day"]), "threat_score": int(record["threat_score"])}
        for record in data
    ]
    populate_index(index_name, elastic_data)
