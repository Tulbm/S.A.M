import asyncio
import aiohttp

async def generate_bad(text, feeling):
    API_KEY = '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'
    MODEL_ID = 'DaJulster/Mental_health_response'
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

        return output[0]['generated_text']

async def main():
    text = input("Enter your text: ")
    feeling = input("Enter your feeling: ")

    result = await generate_bad(text, feeling)
    print(result)

if __name__ == "__main__":
    asyncio.run(main())
