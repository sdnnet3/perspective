# filepath: /home/clayton/perspective/api.py
from ninja import NinjaAPI

api = NinjaAPI()

@api.get("/example")
def example(request):
    return {"message": "Hello, world!"}