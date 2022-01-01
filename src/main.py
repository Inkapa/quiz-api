import uvicorn
from fastapi import FastAPI

if __name__ == "__main__":
    app = FastAPI()
    # to play with API run the script and visit http://127.0.0.1:8000/docs
    uvicorn.run("main:src.config.app", host="127.0.0.1", port=8000)  # you can use reload=True in dev mode
