import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import logging

class QualitativeDataProcessor:
    def __init__(self, data):
        """
        Initialize the processor with qualitative text data.
        """
        self.data = data
        self.nlp = spacy.load("en_core_web_sm")
        logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")

    def extract_entities(self):
        """
        Extract named entities from qualitative data.
        """
        logging.info("Extracting entities from data.")
        all_entities = []
        for doc in self.nlp.pipe(self.data):
            entities = [(ent.text, ent.label_) for ent in doc.ents]
            all_entities.append(entities)
        return all_entities

    def cluster_responses(self, num_clusters=3):
        """
        Cluster qualitative responses using KMeans and TF-IDF.
        """
        logging.info(f"Clustering data into {num_clusters} clusters.")
        vectorizer = TfidfVectorizer(stop_words="english")
        X = vectorizer.fit_transform(self.data)
        model = KMeans(n_clusters=num_clusters, random_state=42)
        model.fit(X)
        return model.labels_

if __name__ == "__main__":
    responses = [
        "The public transport system is efficient.",
        "I love the city parks and their maintenance.",
        "Traffic congestion is a major issue.",
        "More bike lanes would be great."
    ]
    processor = QualitativeDataProcessor(responses)
    entities = processor.extract_entities()
    clusters = processor.cluster_responses(num_clusters=2)
    print("Extracted Entities:\n", entities)
    print("Cluster Labels:\n", clusters)