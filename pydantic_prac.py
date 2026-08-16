from pydantic import BaseModel 
from pydantic import Field
from enum import Enum 

class sentiment(str,Enum):
    positive="positive"
    negative="negative"

class review(BaseModel):
    sentiment:sentiment
    rating:int=Field(ge=1,le=9)
    summary:str

class revresult(BaseModel):
    reviews:list[review]




r = revresult(
    reviews=[
        {
            "sentiment": "positive",
            "rating": 5,
            "summary": "The product is excellent."
        },
        {
            "sentiment": "positive",
            "rating": 4,
            "summary": "The product is nice."
        }
    ]
)



 
print(r)