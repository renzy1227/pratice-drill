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




r= review(
     sentiment="positive",
     rating=9,
     summary="The product is excellent."
 )
 
print(r)