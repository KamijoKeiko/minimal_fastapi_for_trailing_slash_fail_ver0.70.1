from fastapi import FastAPI, APIRouter

app = FastAPI(redirect_slashes=False)
router = APIRouter()


@router.get("/")
async def root():
    return {"message": "Hello World"}


@router.get("/hello")
async def say_hello():
    return {"message": "Hello me"}


app.include_router(router)