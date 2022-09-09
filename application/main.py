from email.mime import application
from typing import Union

from fastapi import FastAPI

import uvicorn
import redis

app = FastAPI()

r = redis.Redis(
    host='35.175.216.6',
    port=6379
    #password='password'
    )
r.set("visits", 0)

def conn():
    if r.ping():
        return "PONG"
    else:
        return "Connection failed"


@app.get("/")
def read_root():
    
    # if r.ping():
    #     return{"PONG"}
    # else:
    #     return("Connection failed!")
    r.set("visits", (int(r.get("visits"))+1) )
    return {str(r.get("visits"))}



if __name__== '__main__':
    uvicorn.run(app, port =8000, host = "0.0.0.0")