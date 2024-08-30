from fastapi import FastAPI, status, Depends
import model
import webScraping
from database import engine, get_db
from sqlalchemy.orm import Session

model.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/quadrado/{num}")
def square(num: int):
    return num ** 2

@app.get("/")
def read_root():
    return {"Hello": "lala"}

'''@app.post("/criar", status_code=status.HTTP_201_CREATED)
def criar_valores(nova_mensagem: classes.Mensagem, db: Session = Depends(get_db)):
    nova_mensagem = webScraping.return_dado
    mensagem_criada = model.Model_Mensagem(**nova_mensagem.model_dump())
    db.add(mensagem_criada)
    db.commit()
    db.refresh(mensagem_criada)
    return {"Mensagem": mensagem_criada}'''
@app.post("/criar", status_code=status.HTTP_201_CREATED)
def criar_valores(db: Session = Depends(get_db)):
    # Obtém os dados via web scraping
    nova_mensagem = webScraping.return_dado()
    
    if nova_mensagem:
        db.add(nova_mensagem)  # Adiciona a instância de Model_Mensagem ao banco de dados
        db.commit()  # Confirma a transação
        db.refresh(nova_mensagem)  # Atualiza a instância com os dados do banco de dados
        return {"Mensagem": nova_mensagem}  # Retorna a mensagem criada
    else:
        return {"Erro": "Não foi possível obter os dados da URL especificada."}