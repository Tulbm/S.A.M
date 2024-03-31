# TODO(developer): Vertex AI SDK - uncomment below & run
# pip3 install --upgrade --user google-cloud-aiplatform
# gcloud auth application-default login

import vertexai
from vertexai.generative_models import GenerativeModel, Part


def generate_text(project_id: str, location: str, prompt) -> str:
    # Initialize Vertex AI
    vertexai.init(project=project_id, location=location)
    # Load the model
    multimodal_model = GenerativeModel("gemini-1.0-pro-vision")
    # Query the model
    response = multimodal_model.generate_content(
        [
            # Add an example image
            #Part.from_uri(
            #    "gs://generativeai-downloads/images/scones.jpg", mime_type="image/jpeg"
            #),
            # Add an example query
            prompt,
        ]
    )
    #print(response)
    return response.text

str = generate_text('genaigenesis','us-central1','Im feeling sad') 

print(str)