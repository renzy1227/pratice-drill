from pydantic import BaseModel 
from pydantic import Field
from enum import Enum 
from openai import OpenAI
from dotenv import load_dotenv
import os

client = OpenAI()

print(os.getenv("OPENAI_API_KEY")) 
load_dotenv()


class sentiment(str,Enum):
    positive="positive"
    negative="negative"

class review(BaseModel):
    sentiment:sentiment
    rating:int=Field(ge=1,le=9)
    summary:str


response = client.responses.parse(
    model="gpt-5.6",
    input="""  
    Honestly, I love this phone. The camera is amazing and the battery
    lasts all day. The only issue is that it gets slightly hot while gaming.
    Overall, I'd give it 4 stars.
    """,
    text_format=review,
)





review = response.output_parsed