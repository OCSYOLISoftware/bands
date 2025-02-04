from fastapi import FastAPI, Request, Form, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from controller.user import User
from lib.check_passw import check_user
from model.handle_db import HandleDB

app = FastAPI()
template = Jinja2Templates(directory='./view')
db = HandleDB()

# Root route
@app.get("/", response_class=HTMLResponse)
def root(req: Request):
    return template.TemplateResponse("index.html", {"request": req})

# Signup route
@app.get("/signup", response_class=HTMLResponse)
def signup(req: Request):
    return template.TemplateResponse("signup.html", {"request": req})

# Login route to process the form and verify the user
@app.post("/user", response_class=HTMLResponse)
def login_user(req: Request, username: str = Form(), password_user: str = Form()):
    verify = check_user(username, password_user)
    if verify:
        users = db.get_all()  # Obtener todos los usuarios de la base de datos
        return template.TemplateResponse("user.html", {"request": req, "data_user": verify, "users": users})
    return RedirectResponse("/", status_code=303)

# User route - only accessible if the user is logged in
@app.get("/user", response_class=HTMLResponse)
def get_user(req: Request):
    # Verificar si el usuario ha iniciado sesión correctamente
    if not req.cookies.get("user_logged_in"):  # Asegúrate de que esta lógica esté alineada con cómo manejas la sesión
        return RedirectResponse("/")
    users = db.get_all()  # Obtener todos los usuarios
    return template.TemplateResponse("user.html", {"request": req, "users": users})

@app.post("/delete_user", response_class=HTMLResponse)
def delete_user(req: Request, username: str = Form()):
    db = HandleDB()
    db.delete(username)  # Eliminar el usuario por su nombre de usuario
    users = db.get_all()  # Obtener la lista de usuarios actualizada
    return template.TemplateResponse("user.html", {"request": req, "users": users})



# Data processing route for sign up
@app.post("/data-processing", response_class=RedirectResponse)
def data_processing(firstname: str = Form(), lastname: str = Form(), username: str = Form(), password_user: str = Form()):
    data_user = {
        "firstname": firstname,
        "lastname": lastname,
        "username": username,
        "password_user": password_user,
    }
    db = User(data_user)
    db.create_user()
    return RedirectResponse("/", status_code=303)
