from fastapi import FastAPI, Query, Path, status, Form, UploadFile, File, Body, Depends, Cookie
from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime


app = FastAPI()
db = []

"""
path parameter for api..
"""

# Request Body..
class City(BaseModel):
    name: str
    timezone: str

class User(BaseModel):
    username: str = Field(..., description="this field is required")
    password: str

class Cluster(BaseModel):
    namespace: str
    container: List[City] = Field(..., example = [{'name': 'delhi', 'timezone': 'delhi india'}])
    timestamp: datetime
    class Config:
        schema_extra = {
            'example' : {
                'namespace': 'my-cluster-name',
                'container': [{
                    "name": 'delhi',
                    'timezone': 'delhi india timezone'
                }], 
                'timestamp': "2021-02-14T11:59:00+00:00"
            }
        }

class UserIn(BaseModel):
    name: str
    username: str
    password: str

class UserOut(BaseModel):
    name: str
    username: str


# test api is running..
@app.get('/')
def index():
    return {'key': 'value'}

# get request for cities..
@app.get('/cities')
def get_cities():
    return db

# get request by id..
@app.get('cities/{city_id}')
def getBy_Id(city_id: int):
    return db.pop(city_id-1)

# post new request..
# request body used for city parameter
@app.post('/cities')
def create_city(city: City):
    db.append(city.dict())
    return db[-1]

# delete cities..
@app.delete('/cities/{city_id}')
def delete_city(city_id: int):
    db.pop(city_id-1)
    return {}


"""
    query parameter
"""
# second parameter required automatically in query..
@app.get('/requried-field/{item_id}')
def required(item_id: int, item_name):
    return {'item_id': item_id, 'item_name': item_name}

@app.get('/default-values/{item_id}')
def default_query(item_id: int, item_name: Optional[str] = None):
    return {'item_id': item_id, 'item_name': item_name}

# bool type convert internally.. if yes-no, true-false, 0-1 typed in url query..
@app.get('/bool-conversion/{item_id}')
def conversion(item_id: int, item_name: Optional[str] = None, sold: bool = False):
    return {'item_id': item_id, 'item_name': item_name, 'sold': sold}


"""
 Request Body..
"""

@app.post('/direct-use')
def direct_use(city: City):
    return {'name': city.name, 'timezone': city.timezone}

@app.put("/city-plus-item/{item_id}")
async def create_item(item_id: int, city: City):
    return {"item_id": item_id, **city.dict()}


"""
 query parameter and string validator..
 Query(... (required field), min_length= int, max_length= int, regex= '^fixedvalue$')
"""

@app.get('/validation/', tags= ["validation"])
def query_validation(q: Optional[str] = Query(None, max_length=50)):
    return {'query': q}


@app.get('/list-validation/')
def list_validation(q: Optional[List[str]] = Query(None)):
    return {'query': q}


# http://127.0.0.1:8000/items/?item-query=foobaritems
# here item-query is not valid python variable
# so use alias in query


@app.get('/alias/')
def alias(q: Optional[str] = Query(None, alias="item-query")):
    return {'query': q}

# meta data in fastapi

@app.get("/items/")
async def read_items(
    q: Optional[str] = Query(
        None,
        alias="item-query",
        title="Query string",
        description="Query string for the items to search in the database that have a good match",
        min_length=3,
        max_length=50,
        regex="^fixedquery$",
        deprecated=True,
    )
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

"""
path parameter.. numeric validation...
"""

#  gt = greater than
#  le = less than or equal to
#  ge = greater than or equal to
@app.get("/items/{item_id}")
async def numeric_validation(*,
    item_id: int = Path(..., title="The ID of the item to get", gt=0, le=1000),
    q: str,
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results

"""
Body request..
"""

@app.put('/body-can-set', tags = ["Body"])
def update_city(*, city: Optional[City] = None):
    return {
        'body': city
    }


@app.put('/nested-dict')
def multiple_body(*, city: Optional[City] = None, user: User):
    return {
        'city': city,
        'user': user
    }

@app.put('/embed-agr-key-into-body')
def embed(city: City = Body(..., embed = True)):
    return {'body': city}



@app.put('/cluster')
def cluster(cluster: Cluster = Body(..., embed = True)):
    return {**Cluster}


"""
Response model..
"""
@app.post("/cluster-response", response_model = Cluster, tags = ["cluster"], response_description="The cluster created")
def cluster_res(cluster: Cluster):
    return {**cluster}

@app.post('/user-out', response_model = UserOut, status_code= status.HTTP_201_CREATED)
def user_out(user: UserIn):
    return user

@app.post("/login/")
async def login(username: str = Form(...), password: str = Form(...)):
    return {"username": username}

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    return {"filename": file.filename}

"""
dependency injection with sub-dependency
"""
def query_extractor(q: Optional[str] = None):
    return q


def query_or_cookie_extractor(
    q: str = Depends(query_extractor), last_query: Optional[str] = Cookie(None)
):
    if not q:
        return last_query
    return q


@app.get("/items/")
async def read_query(query_or_default: str = Depends(query_or_cookie_extractor)):
    return {"q_or_cookie": query_or_default}