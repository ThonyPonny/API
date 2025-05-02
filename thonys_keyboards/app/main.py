from fastapi import FastAPI, Request, Depends, Form
from fastapi.responses import RedirectResponse 
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from . import models, database

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Dependency
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def list_keyboards(request: Request, db: Session = Depends(get_db)):
    keyboards = db.query(models.Keyboard).all()
    return templates.TemplateResponse("list.html", {
        "request": request,
        "keyboards": keyboards
    })

@app.get("/create")
async def create_form(request: Request):
    return templates.TemplateResponse("create.html", {"request": request})

@app.post("/create")
async def create_keyboard(
    request: Request,
    name: str = Form(...),
    brand: str = Form(...),
    price: float = Form(...),
    db: Session = Depends(get_db)
):
    keyboard = models.Keyboard(name=name, brand=brand, price=price)
    db.add(keyboard)
    db.commit()
    return RedirectResponse(url="/", status_code=303)

@app.put("/edit/{keyboard_id}")
async def edit_form(request: Request, keyboard_id: int, db: Session = Depends(get_db)):
    keyboard = db.query(models.Keyboard).filter(models.Keyboard.id == keyboard_id).first()
    return templates.TemplateResponse("edit.html", {
        "request": request,
        "keyboard": keyboard
    })

@app.put("/update/{keyboard_id}")
async def update_keyboard(
    request: Request,
    keyboard_id: int,
    name: str = Form(...),
    brand: str = Form(...),
    price: float = Form(...),
    db: Session = Depends(get_db)
):
    keyboard = db.query(models.Keyboard).filter(models.Keyboard.id == keyboard_id).first()
    keyboard.name = name
    keyboard.brand = brand
    keyboard.price = price
    db.commit()
    return RedirectResponse(url="/", status_code=303)

@app.delete("/delete/{keyboard_id}")
async def delete_keyboard(keyboard_id: int, db: Session = Depends(get_db)):
    keyboard = db.query(models.Keyboard).filter(models.Keyboard.id == keyboard_id).first()
    db.delete(keyboard)
    db.commit()
    return RedirectResponse(url="/", status_code=303)