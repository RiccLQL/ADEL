from fastapi import FastAPI

app = FastAPI();

@app.get("/receive")
async def receive():
    