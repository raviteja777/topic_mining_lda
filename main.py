# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from topic_mining import TopicMiner

DIR_PATH = "data/sample"
NUM_TOPICS = 10


def disp_topics(topics):
    for i, topic in enumerate(topics):
        print("Topic: ", i)
        print(*topic,sep=", ")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    topic_miner = TopicMiner(DIR_PATH, NUM_TOPICS)
    disp_topics(topic_miner.get_topics())
