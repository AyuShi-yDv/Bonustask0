from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from supabase_client import supabase
from fastapi.staticfiles import StaticFiles

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Optional: for CSS/JS if you add a 'static' folder
# app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def home(request: Request):
    # Fetch all records from Supabase table 'todos'
    response = supabase.table("todos").select("*").execute()
    data = response.data
    return templates.TemplateResponse("index.html", {"request": request, "data": data})
