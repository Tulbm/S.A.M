import vertexai
from vertexai.generative_models import GenerativeModel, ChatSession

# TODO(developer): Update and un-comment below lines
# project_id = "genaigenesis"
# location = "us-central1"

vertexai.init(project='genaigenesis', location='us-central1')
model = GenerativeModel("gemini-1.0-pro")
chat = model.start_chat()

def get_chat_response(chat: ChatSession, prompt: str) -> str:
    text_response = []
    responses = chat.send_message(prompt, stream=True)
    for chunk in responses:
        text_response.append(chunk.text)
    return "".join(text_response)

prompt = "Hello."
print(prompt)
print(get_chat_response(chat, prompt))

prompt = "What are all the colors in a rainbow?"
print(prompt)
print(get_chat_response(chat, prompt))

prompt = "Why does it appear when it rains?"
print(prompt)
print(get_chat_response(chat, prompt))

