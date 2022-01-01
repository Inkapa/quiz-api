import uvicorn
import src.endpoints
import src.config
from dotenv import load_dotenv
import os

load_dotenv()
if __name__ == "__main__":
    # to play with API run the script and visit http://0.0.0.0:$PORT/docs
    uvicorn.run("src.main:src.config.app", host="0.0.0.0", port=os.getenv("PORT"))  # you can use reload=True in dev mode
