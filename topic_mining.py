import os
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
import numpy as np


class TopicMiner:

    def __init__(self, dir_path, num_topics):
        self.topics = []
        files = self.load_files(dir_path)
        vectors, feature_names = self.transform_file(files)
        self.compute_topics(vectors, feature_names,num_topics)

    def load_files(self,dir_path):
        files = [open(os.path.join(dir_path, f),'r') for f in os.listdir(dir_path)]
        return files

    def transform_file(self, files):
        # print("file name -- " + file)
        # dat_file = [open(file, 'r')]
        cv = CountVectorizer(input='file', stop_words='english',min_df=0.1, max_features=1000)
        vectors = cv.fit_transform(raw_documents=files)
        feature_names = cv.get_feature_names()
        return vectors, feature_names

    def compute_topics(self, vectors, feature_names,num_topics):
        lda = LatentDirichletAllocation(n_components=num_topics, max_iter=25, learning_method='batch')
        doc_topics = lda.fit_transform(vectors)
        print(doc_topics)
        topic_features = np.argsort(lda.components_, axis=1)[:, ::-1]
        for topic in topic_features:
            self.topics.append([feature_names[ind] for ind in topic])

    def get_topics(self):
        return self.topics

# print(transform_file("data/sample/006.txt"))
