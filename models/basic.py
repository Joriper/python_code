from pydantic import *
from pydantic.json_schema import SkipJsonSchema
from typing import Optional,List
from datetime import datetime

class Basic(BaseModel):
    status:int
    message:str
    site:str
    error:int





class CreateItem(BaseModel):
    name:str
    email:str
    item_name:str
    quantity:int
    expiry_date:str
    inserted_at:SkipJsonSchema[str] = Field(exclude=True,default=str(datetime.now()).split(" ")[0])



    @validator('expiry_date')
    def parse_dob(cls, v):
        return str(datetime.strptime(v, '%Y-%m-%d').date())

class GetItem(BaseModel):
    id:str

class FilterItem(BaseModel):
    email:str
    expiry_date:str
    insert_at:str
    quantity:int

class UpdateItem(BaseModel):
    email:str
    name:str
    item_name:str
    expiry_date:str
    quantity:int

    @validator('expiry_date')
    def parse_dob(cls, v):
        return str(datetime.strptime(v, '%Y-%m-%d').date())


############### Clock Model ###################
class CreateClock(BaseModel):
    email:str
    location:str
    inserted_at:SkipJsonSchema[str] = Field(exclude=True,default=str(datetime.now()).split(" ")[0])

class UpdateClock(BaseModel):
    email:str
    location:str



######## Response Models #################
class FilterAndGet(BaseModel):
    status:int
    message:str
    data:List[dict]

class DeleteUpdate(BaseModel):
    status:int
    message:str
    id:str

class CreateResponse(BaseModel):
    status:int
    message:str