import requests

def post(address, resource, payload={}, headers={}):
    response =  requests.post(
                    f"{address}{resource}", 
                    json=payload,
                    headers=headers
                )

    return response
