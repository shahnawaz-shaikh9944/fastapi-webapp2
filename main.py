from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "WE HAVE DEPLOYED FAST API ON AZURE CLOUD"}
