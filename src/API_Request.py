from enum import Enum
import requests
import json
from typing import Any

class RequestType(Enum):
    GET     = 0
    POST    = 1
    PUT     = 2
    DELETE  = 3

def loadApiKey(path: str):
    
    key = None

    try:
        with open(path,"r") as file:
            key = file.readline()
    except FileNotFoundError as err:
        print(f"FILE_ERROR: {err}")
        exit(1)

    return key


def geminiRequest(API_KEY: str):

    generateRequest(f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={API_KEY}",RequestType.POST,{
    "contents": [
        {
        "parts": [
            {
            "text": "Explain how AI works in a few words"
                }
            ]
            }
        ]
    })



def generateRequest(url: str, reqType: RequestType, data: dict[str, Any]) -> str:
    
    ERROR_HEADER_LEN = 70
    headers = {"Content-Type": "application/json"}
    r = None

    if reqType == RequestType.GET:
        r = requests.get(url, headers=headers, params=data)
        if r.status_code >= 200 and r.status_code <= 299:
            return r
        else:
            raise ValueError("\n\n" + "="*ERROR_HEADER_LEN + f"\n\n\tPOST_ERROR:\n\n\t  Status: {r.status_code}"+f"\n\n\t Body: {r.text}\n\n"+"="*ERROR_HEADER_LEN)
    elif reqType == RequestType.POST:
        r = requests.post(url, headers=headers, json=data)
        if r.status_code >= 200 and r.status_code <= 299:
            return r
        else:
            raise ValueError("\n\n" + "="*ERROR_HEADER_LEN + f"\n\n\tPOST_ERROR:\n\n\t  Status: {r.status_code}"+f"\n\n\t Body: {r.text}\n\n"+"="*ERROR_HEADER_LEN)

    raise ValueError(f"Unsupported request type {reqType}")

