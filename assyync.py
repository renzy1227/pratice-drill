

import asyncio
from openai import AsyncOpenAI

client = AsyncOpenAI()

headlines = [
    "AI company launches new model",
    "India wins cricket match",
    "New smartphone released",
    "NASA announces space mission",
    "Stock market reaches new high"
]


async def summarize(headline):
    response = await client.responses.create(
        model="gpt-5",
        input=f"Summarize this headline in one sentence: {headline}"
    )

    print(response.output_text)


async def main():
    tasks = [summarize(headline) for headline in headlines]

    await asyncio.gather(*tasks)


asyncio.run(main())