from fastapi import FastAPI
from server.routes.student import router as StudentRouter
from server.routes.user import router as UserRouter
from server.routes.authentication import router as AuthRouter

app = FastAPI()

app.include_router(AuthRouter, tags=["Authentication"])
app.include_router(UserRouter, tags=["User"], prefix="/user")
app.include_router(StudentRouter, tags=["Student"], prefix="/student")


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to EcoDrive!"}
