from fastapi import FastAPI, Query

app = FastAPI()

# BEGIN (write your solution here
@app.get("/filter")
async def func_min_max(
    min: int = Query(default=0, gt=0),
    max: int = Query(default=100, lt=100)):
    return {"min":min, "max":max}

# END
