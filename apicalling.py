from dotenv import load_dotenv
from openai import OpenAI
from pydantic import BaseModel, Field
from enum import Enum

load_dotenv()

client = OpenAI()


class Sentiment(str, Enum):
    positive = "positive"
    negative = "negative"


class ProductReview(BaseModel):
    sentiment: Sentiment
    rating: int = Field(ge=1, le=5)
    summary: str


review_text = """
I absolutely love this phone. The camera is amazing and the battery
lasts all day. The only annoying thing is that it gets slightly warm
while gaming. I'd give it 4 out of 5.
"""


response = client.responses.parse(
    model="gpt-5.6",
    input=review_text,
    text_format=ProductReview,
)

review = response.output_parsed

print(review)
print(type(review))

print(review.sentiment)
print(review.rating)
print(review.summary)