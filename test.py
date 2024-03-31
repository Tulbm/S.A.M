import asyncio
import aiohttp

async def predict(text, feeling, stress_level, loaded=False):
    API_KEY = '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'
    MODEL_ID = 'DaJulster/Mental_health_identification'
    API_URL = f"https://api-inference.huggingface.co/models/{MODEL_ID}"
    input_text = f"I am feeling: {feeling}. {text}" 
    headers = {"Authorization": f"Bearer {API_KEY}"}

    async with aiohttp.ClientSession() as session:
        async def query(payload, url, headers):
            async with session.post(url, json=payload, headers=headers) as response:
                response.raise_for_status()
                return await response.json()

        try:
            output = await query({"inputs": input_text}, API_URL, headers)
        except Exception as e:
            print(f"Error occurred: {e}")
            await asyncio.sleep(10)
            output = await query({"inputs": input_text}, API_URL, headers)

        score = None
        for item in output[0]:
            if item['label'] == 'NEGATIVE':
                score = item['score']

        if score is not None:
            score += 0.08 * stress_level
        print('---------DEBUG------------')
        print("Score as", score)
        print('---------DEBUG------------')
        return score

async def test_predict():
    text = "Example text"
    feeling = "Happiness"
    stress_level = 0.5
    result = await predict(text, feeling, stress_level)
    print("Result:", result)

# Run the test function
asyncio.run(test_predict())
