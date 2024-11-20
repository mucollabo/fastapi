from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route

async def greeting(request):
    return JSONResponse('Hello? Charles?')

app = Starlette(debug=True, routes=[
    Route('/hi', greeting),
])