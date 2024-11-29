def fetch_data_from_elasticsearch(index_name):
    query = {
        "query": {
            "match_all": {}
        }
    }
    result = es.search(index=index_name, body=query, size=1000)  # Извлекаем все записи
    data = [hit["_source"] for hit in result["hits"]["hits"]]
    return data

# Пример использования
elastic_data = fetch_data_from_elasticsearch(index_name)
print("Fetched data:", elastic_data)
