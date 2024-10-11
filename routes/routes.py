from fastapi import *
from models.basic import * 
from db.connection import *
from bson import ObjectId

app = APIRouter()

############### Items API #####################

@app.post("/items",response_model=CreateResponse)
def item_create(handle_model:CreateItem):
    items_collection.insert_one(dict(handle_model))
    return {"status":200,"message":'Successfully inserted'}


@app.get("/items/filter",response_model=FilterAndGet)
def filter_items(email: str,expiry_date:str,inserted_at:str,quantity:int):
    print("called")
    filter_ = list(items_collection.find({"email":email,"expiry_date":expiry_date,"inserted_at":inserted_at,"quantity":{"$gte":quantity}}))

    for items in filter_:
        items['_id']=str(items['_id'])

    return {"status":200,"message":"Success","data":list(filter_)}



@app.get("/items/{id}",response_model=FilterAndGet)
def get_item(id:str):
    result = items_collection.find_one({"_id":ObjectId(str(id))})
    if result:
        result['_id']=str(result['_id'])
    else:
        result={}
    return {"status":200,"message":"Fetched successfully","data":[result]}

@app.delete("/items/{id}",response_model=DeleteUpdate)
def delete_item(id:str):
    result = items_collection.delete_one({"_id":ObjectId(str(id))})
    return {"status":200,"message":"Deleted successfully","id":id}

@app.put("/items/{id}",response_model=DeleteUpdate)
def update_item(id:str,data:UpdateItem):
    updates = items_collection.update_one({"_id":ObjectId(str(id))},{"$set":dict(data)})
    return {"status":200,"message":"Item update successfully","id":id}



################ Clock in record API ###################

@app.post("/clock-in",response_model=CreateResponse)
def create_clock(clock_models:CreateClock):
    clock_collection.insert_one(dict(clock_models))
    return {"status":200,"message":'Clock Created'}

@app.get("/clock-in/filter",response_model=FilterAndGet)
def filter_clock_tems(email: str,location:str,inserted_at:str):
    print("called")
    filter_clock = list(clock_collection.find({"email":email,"location":location,"inserted_at":inserted_at}))

    for items in filter_clock:
        items['_id']=str(items['_id'])
    return {"status":200,"message":"Success","data":list(filter_clock)}



@app.get("/clock-in/{id}",response_model=FilterAndGet)
def get_clock(id:str):
    result =  clock_collection.find_one({"_id":ObjectId(str(id))})
    if result:
        result['_id']=str(result['_id'])
    else:
        result={}
    return {"status":200,"message":"Clock Fetched successfully","data":[result]}


@app.delete("/delete-in/{id}",response_model=DeleteUpdate)
def delete_item(id:str):
    result = clock_collection.delete_one({"_id":ObjectId(str(id))})
    return {"status":200,"message":"Clock Deleted successfully","id":id}

@app.put("/clock-in/{id}",response_model=DeleteUpdate)
def update_item(id:str,data:UpdateClock):
    updates = clock_collection.update_one({"_id":ObjectId(str(id))},{"$set":dict(data)})
    return {"status":200,"message":"Clock update successfully","id":id}