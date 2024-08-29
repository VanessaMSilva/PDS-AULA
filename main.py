from fastapi import FastAPI, status , Depends
import os
import classes

import model
#from database import engine, get_db
from sqlalchemy.orm import Session
import os
from dotenv import load_dotenv

load_dotenv()  # Loads environment variables from .env file

#model.Base.metadata.create_all(bind=engine)

app = FastAPI()
# Agora você pode acessar as variáveis de ambiente
database_url = os.getenv("DATABASE_URL")
secret_key = os.getenv("SECRET_KEY")


@app.get("/quadrado/{num}")
def square(num: int):
    return num ** 2

@app.get("/")
def read_root():
    return {"Hello": "lalala"}

@app.get("/")
def read_root():
    database_url = os.getenv("DATABASE_URL")
    secret_key = os.getenv("SECRET_KEY")
    return {
        "database_url": database_url,
        "secret_key": secret_key,
        "debug_mode": os.getenv("DEBUG")
    }

@app.post("/criar", status_code = status.HTTP_201_CREATED)
def criar_valores(nova_mensagem: classes.Mensagem, db: Session = Depends(read_root)):
    #mensagem_criada = model.Model_Mensagem(titulo=nova_mensagem.titulo,
    #conteudo=nova_mensagem.conteudo, publicada=nova_mensagem.publicada)
    mensagem_criada = model.Model_Mensagem(**nova_mensagem.model_dump())
    db.add(mensagem_criada)
    db.commit()
    db.refresh(mensagem_criada) #Atualiza a sessão com a mensagem do postman para retornar a mensagem com os valores
    return {"Mensagem": mensagem_criada}