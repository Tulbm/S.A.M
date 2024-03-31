# S.A.M

## Inspiration
- Inspired by one of our group member's experience working with vulnerable individuals
- Access to mental health services is not easily available. Counselling can be expensive, and the friction to get into sections can be a big obstacle for many
- The third United Nation's Sustainable Development Goal, Good Health and Well-being
## What it does
- Initially assesses a user's mental status to gauge how the conversation should go
- Interacts with the user while continuing to gather data about their emotional situation
## How we built it
- Based on Transformers models BART and DistilBERT
- Integrated Jupyter Notebooks APIs with a django front-end
## Challenges we ran into
- For a while the text generator model was spewing inaccurate and short answers
- The classification model for the responses was not able to discern between positive and negative emotions for some time while testing
## What's next for S.A.M
- Adding support to languages other than English
- Tracking changes in users' mental health status over longer periods of time

## Models made
(based on distilbert and bart models respectively)

https://huggingface.co/DaJulster/Mental_health_identification

https://huggingface.co/DaJulster/Mental_health_response

https://www.kaggle.com/code/julienserbanescu/mental-health-response-model-e2e1fa

https://www.kaggle.com/code/julienserbanescu/mental-health-identification-model 


## Datasets used
https://www.kaggle.com/datasets/infamouscoder/mental-health-social-media

https://www.kaggle.com/datasets/alexyarbor/depression-data-set-with-depression-level

https://www.kaggle.com/datasets/reihanenamdari/mental-health-corpus

https://www.kaggle.com/datasets/thedevastator/nlp-mental-health-conversations
