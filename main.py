from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello from Render!"}

@app.get("/hello/{name}")
def say_hello(name: str):
    # This prints to the server console (visible in Render logs)
    print(f"Hello {name}") 
    
    # This returns the data to the user's browser/API client
    return {"message": f"Hello {name}"}
