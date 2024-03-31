from gensim import corpora, models
import spacy
import aiohttp
import asyncio
import string

nlp = spacy.load("en_core_web_sm")  # Load the model once

async def query(payload, url, headers, session, max_retries=5):
    retries = 0
    while retries < max_retries:
        try:
            # Include parameters directly in the payload for consistency
            payload["parameters"] = {"max_length": 150}
            async with session.post(url, json=payload, headers=headers) as response:
                if response.status == 200:
                    return await response.json()  # Successful request
                else:
                    error = await response.json()  # Attempt to get JSON response
                    if "error" in error and "Model is loading" in error["error"]:
                        print("Model is loading, waiting...")
                        await asyncio.sleep(15)  # Use asyncio.sleep for async context
                        retries += 1
                    else:
                        # If the error is not related to model loading, return it
                        return error
        except aiohttp.ClientResponseError as e:
            print(f"ClientResponseError: {e.status}. Retrying...")
            await asyncio.sleep(5)  # Wait before retrying for generic client errors
            retries += 1
        except aiohttp.ContentTypeError:
            # If the response is not JSON or another error occurs
            print(f"Failed to parse error response. Retrying...")
            await asyncio.sleep(5)  # Backoff before retrying
            retries += 1
        except Exception as e:
            print(f"Unexpected error: {e}. Retrying...")
            await asyncio.sleep(5)
            retries += 1

    return {"error": "Max retries exceeded or other error"}

def extract_topics(text):
    # Function renamed from 'topics' to 'extract_topics' to avoid naming conflicts
    text = text.translate(str.maketrans('', '', string.punctuation)).replace("\n", " ").lower()
    
    doc = nlp(text)
    nouns = [token.text for token in doc if token.pos_ in ["NOUN", "PROPN"]]
    nouns = set(nouns)
    
    if not nouns:
        return []

    dictionary = corpora.Dictionary([nouns])
    corpus = [dictionary.doc2bow(nouns)]
    
    if not corpus or not corpus[0]:
        return []
    
    ldamodel = models.LdaModel(corpus, num_topics=3, id2word=dictionary)
    topics = ldamodel.print_topics(num_topics=3, num_words=1)
    topic_list = [topic[1].split('"')[1] for topic in topics]
    
    return list(set(topic_list))

async def predict(text, feeling, stress_level, session):
    API_KEY = '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'
    MODEL_ID = 'DaJulster/Mental_health_identification'
    API_URL = f"https://api-inference.huggingface.co/models/{MODEL_ID}"
    input_text = f"I am feeling: {feeling}. {text}" 
    headers = {"Authorization": f"Bearer {API_KEY}"}

    output = await query({"inputs": input_text}, API_URL, headers, session)
    score = None
    for item in output[0]:
        if item['label'] == 'NEGATIVE':
            score = item['score']
            break  # Assuming only one NEGATIVE label is needed

    if score is not None:
        score += 0.02 * stress_level

    return score

async def generate_response(text, feeling, session, positive=True):
    # Unified function for generating responses, either good or bad
    API_KEY = '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'
    MODEL_ID = 'DaJulster/Mental_health_response'
    API_URL = f"https://api-inference.huggingface.co/models/{MODEL_ID}"
    headers = {"Authorization": f"Bearer {API_KEY}"}

    if positive:
        topics = extract_topics(text)
        topic_list = ', '.join(topics)
        input_text = f"I am interested in {topic_list}. {text}" 
    else:
        input_text = f"I am feeling: {feeling}. {text}"

    output = await query({"inputs": input_text, "parameters": {"max_length": 150}}, API_URL, headers, session)
    return output[0]['generated_text']


