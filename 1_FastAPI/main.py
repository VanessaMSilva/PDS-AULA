from fastapi import FastAPI, Depends, status, HTTPException
import model
import webScraping
from database import engine, get_db
from sqlalchemy.orm import Session
import classes
from typing import List
from fastapi.middleware.cors import CORSMiddleware

model.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/quadrado/{num}")
def square(num: int):
    return num ** 2

@app.get("/")
def read_root():
    return {"Hello": "lala"}

@app.post("/criar/", status_code=status.HTTP_201_CREATED)
def criar_valores(nova_mensagem: classes.Mensagem, db: Session = Depends(get_db)):
    mensagem_criada = model.Model_Mensagem(**nova_mensagem.model_dump())
    db.add(mensagem_criada)
    db.commit()
    db.refresh(mensagem_criada)
    return {"Mensagem": mensagem_criada}

@app.get("/menu/", status_code=status.HTTP_201_CREATED)
def criar_valores(db: Session = Depends(get_db)):
    # Chama a função de scraping para obter os dados
    dados = webScraping.return_dado()

    if not dados:
        raise HTTPException(status_code=400, detail="Erro ao coletar dados do menu")
    
    # Itera sobre os dados retornados pelo web scraping e insere no banco
    mensagens_criadas = []
    
    print(f'{dados["menuNav"]}: {dados["link"]} --------------------------------')
    nova_mensagem = model.Model_Menu(
        menuNav = dados["menuNav"],
        link = dados["link"],
    )
    db.add(nova_mensagem)
    db.commit()
    db.refresh(nova_mensagem)
    mensagens_criadas.append(nova_mensagem)
    return {"Mensagens": mensagens_criadas}
origins = [
 'http://localhost:3000'
]
app.add_middleware(
 CORSMiddleware,
 allow_origins=origins,
 allow_credentials=True,
 allow_methods=['*'],
 allow_headers=['*']
)


@app.get("/mensagens", response_model=List[classes.Mensagem], status_code=status.HTTP_200_OK)
async def buscar_valores(db: Session = Depends(get_db), skip: int = 0, limit: int=100):
    mensagens = db.query(model.Model_Mensagem).offset(skip).limit(limit).all()
    return mensagens
