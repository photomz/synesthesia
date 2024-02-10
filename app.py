from fastapi import FastAPI
from starlette.responses import JSONResponse
from spotify import *

app = FastAPI()

@app.get('/analyze')
async def analyze(track_id: str):
    track_info = get_analysis(track_id)
    data = analyze_track(track_info)
    return JSONResponse(content=data)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=3000)
