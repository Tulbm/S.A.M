from gensim import corpora, models
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string
import nltk
import spacy
import requests
import time
# Replace YOUR_API_KEY with your Hugging Face API key
# Replace MODEL_ID with the model's name on Hugging Face; for example, "bert-base-uncased"
loaded = False

def query(payload, API_URL, headers):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()


def topics(text):
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = text.replace("\n", " ")
    text = text.lower()
    nlp = spacy.load("en_core_web_sm")

    doc = nlp(text)
    nouns = [token.text for token in doc if token.pos_ in ["NOUN", "PROPN"]]
    nouns = set(nouns)

    # create a dictionary from the text data
    dictionary = corpora.Dictionary([nouns])
    # create a corpus from the text data
    corpus = [dictionary.doc2bow(nouns)]
    # train the LDA model on the corpus
    ldamodel = models.LdaModel(corpus, num_topics=3, id2word=dictionary)

    # extract the topics from the model
    topics = ldamodel.print_topics(num_topics=3, num_words=1)

    # print the topics
    topic_list = []
    for topic in topics:
        topic_list.append(topic[1].split('"')[1])

    return list(set(topic_list))



import requests
import time

def predict(text, feeling, stress_level, loaded=False):
    API_KEY = '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'
    MODEL_ID = 'DaJulster/Mental_health_identification'
    API_URL = f"https://api-inference.huggingface.co/models/{MODEL_ID}"
    input_text = f"I am feeling: {feeling}. {text}" 
    headers = {"Authorization": f"Bearer {API_KEY}"}

    def query(payload, url, headers):
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        return response.json()

    try:
        output = query({"inputs": input_text}, API_URL, headers)
    except Exception as e:
        print(f"Error occurred: {e}")
        time.sleep(10)
        output = query({"inputs": input_text}, API_URL, headers)

    score = None
    for item in output[0]:
        if item['label'] == 'Negative':
            score = item['score']

    if score is not None:
        score += 0.08 * stress_level

    return score



def generate_bad(text):
    API_KEY = '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'
    MODEL_ID = 'DaJulster/Mental_health_identification'
    API_URL = f"https://api-inference.huggingface.co/models/{MODEL_ID}"
    input_text = text
    headers = {"Authorization": f"Bearer {API_KEY}"}
    if not loaded:
        try:
            output = query({"inputs": input_text}, API_URL, headers)
        except:
            time.sleep(10)
            output = query({"inputs": input_text}, API_URL, headers)
    else:
        output = query({"inputs": input_text}, API_URL, headers)
    for item in output[0]:
        if item['label'] == 'Negative':
            score = item['score']
    return score

