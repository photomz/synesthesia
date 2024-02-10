from fastapi import FastAPI
from starlette.responses import JSONResponse

app = FastAPI()

@app.get('/analyze')
async def analyze():
    # get track id
    # Placeholder for the actual implementation
    return JSONResponse(content={"message": "I am a teapot"})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=3000)
