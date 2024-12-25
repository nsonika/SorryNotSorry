# from fastapi import FastAPI
# from routes import excuses

# app = FastAPI(title="SorryNotSorry AI Excuse Maker")

# # Include the routes for excuse generation
# app.include_router(excuses.router)

# @app.get("/")
# def root():
#     return {"message": "Welcome to the SorryNotSorry AI Excuse Maker API"}


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import excuses

app = FastAPI(title="SorryNotSorry AI Excuse Maker")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Allow specific origin (frontend)
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all HTTP headers
)

# Include the routes for excuse generation
app.include_router(excuses.router)

@app.get("/")
def root():
    return {"message": "Welcome to the SorryNotSorry AI Excuse Maker API"}
