from fastapi import FastAPI
from routes import excuses

app = FastAPI(title="SorryNotSorry AI Excuse Maker")

# Include the routes for excuse generation
app.include_router(excuses.router)

@app.get("/")
def root():
    return {"message": "Welcome to the SorryNotSorry AI Excuse Maker API"}
