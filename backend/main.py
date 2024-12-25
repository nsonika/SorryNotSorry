from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import excuses

app = FastAPI(title="SorryNotSorry AI Excuse Maker")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"], 
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

# Include the routes for excuse generation
app.include_router(excuses.router)

@app.get("/")
def root():
    return {"message": "Welcome to the SorryNotSorry AI Excuse Maker API"}
