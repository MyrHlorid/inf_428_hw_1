class TestElasticsearchWorkflow(unittest.TestCase):

    def test_csv_generation(self):
        self.assertTrue(os.path.exists(file_path), "CSV file not generated.")

    def test_elasticsearch_index(self):
        self.assertTrue(es.indices.exists(index=index_name), "Index not created in Elasticsearch.")

    def test_elasticsearch_data(self):
        data = fetch_data_from_elasticsearch(index_name)
        self.assertTrue(len(data) > 0, "No data found in Elasticsearch.")

if __name__ == "__main__":
    unittest.main()
