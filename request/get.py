import requests

def get(address, resource, payload={}, headers={}):
    response =  requests.get(
                    f"{address}{resource}", 
                    json=payload,
                    headers=headers
                )

    return response