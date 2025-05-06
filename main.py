from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel

import json

from dotenv import load_dotenv
import os

load_dotenv()

FRONTEND_DEV_URL = os.getenv("FRONTEND_DEV_URL")
FRONTEND_PROD_URL = os.getenv("FRONTEND_PROD_URL")

import sys

sys.path.insert(0, "/Users/yashpola/Repositories/AlgoRepo/algorithms/flow/")

from maxflow import max_flow

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[FRONTEND_DEV_URL, FRONTEND_PROD_URL],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class RequestData(BaseModel):
    graph: str
    src: str
    sink: str


class MaxFlowResult(BaseModel):
    flowVal: str


@app.get("/")
async def root():
    return {"message": "test"}


def stog(s: str) -> list[list[int]]:
    graph = []
    for row in s:
        graph.append(s[row])
    return graph


@app.post("/", response_model=MaxFlowResult)
def root(data: RequestData) -> MaxFlowResult:
    print(data.graph, data.src, data.sink)
    res = max_flow(stog(json.loads(data.graph)), int(data.src), int(data.sink))[0]
    return dict(flowVal=str(res))
