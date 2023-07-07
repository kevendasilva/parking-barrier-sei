import os

def get_variable(variable):
    response = os.getenv(variable)

    if not response:
        print(f"{variable} environment variable not set.")
        return None
    
    return response
