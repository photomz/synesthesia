from fastapi import FastAPI
from starlette.responses import JSONResponse

app = FastAPI()

@app.get('/analyze')
async def analyze(track_id: str):
    # Placeholder for the actual implementation
    # Here you would typically call the get_analysis function from spotify.py
    # with the provided track_id and return its result.
    return JSONResponse(content={"message": f"I am a {track_id} teapot"})


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=3000)
