from enum import Enum
import requests
import json
from typing import Any

class RequestType(Enum):
    GET     = 0
    POST    = 1
    PUT     = 2
    DELETE  = 3



def geminiRequestAll(API_KEY: str, payload):

    return generateRequest(f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={API_KEY}",RequestType.POST,{
    "contents": [
        {
        "parts": [
            {
            "text": f"Please write docstrings to explain what each part of code does. You need to write <linebreak> instead of '\\n'\n\n. DO NOT contain the markdown for code highlighting like '```c```'\n\n\n {payload}"
                }
            ]
            }
        ]
    })


def generateRequest(url: str, reqType: RequestType, data: dict[str, Any]) -> dict:

    ERROR_HEADER_LEN = 70
    headers = {"Content-Type": "application/json"}

    # if reqType == RequestType.GET:
    #     r = requests.get(url, headers=headers, params=data)
    #     if r.status_code >= 200 and r.status_code <= 299:
    #         return r
    #     else:
    #         raise ValueError("\n\n" + "="*ERROR_HEADER_LEN + f"\n\n\tPOST_ERROR:\n\n\t  Status: {r.status_code}"+f"\n\n\t Body: {r.text}\n\n"+"="*ERROR_HEADER_LEN)

    if reqType == RequestType.POST:
        r = requests.post(url, headers=headers, json=data)
        if r.status_code >= 200 and r.status_code <= 299:
            return r.json()
        else:
            raise ValueError("\n\n" + "="*ERROR_HEADER_LEN + f"\n\n\tPOST_ERROR:\n\n\t  Status: {r.status_code}"+f"\n\n\t Body: {r.text}\n\n"+"="*ERROR_HEADER_LEN)

    raise ValueError(f"Unsupported request type {reqType}")

