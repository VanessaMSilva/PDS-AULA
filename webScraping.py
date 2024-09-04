import requests
from bs4 import BeautifulSoup
from model import Model_Mensagem



    
    #print(soup.title)
    #print(soup.title.contents)
def return_dado():
    resposta = requests.get('http://www.prefe.ufu.br/concessoes/cantina-da-tia-lu')
    
    if resposta.status_code == 200:
        soup = BeautifulSoup(resposta.content, 'html.parser')
        itens = soup.find_all('div', class_='field-label')
        for item in itens:
            print(item.text, '\n')
        # Cria uma instância da classe `Model_Mensagem`
        model_msg = Model_Mensagem(
            titulo="Web scraping",
            conteudo=soup.prettify()
        )
        
        return model_msg
    else:
        return None

    
'''S
    itens = soup.find_all('div', class_='field-label')
    for item in itens:
        print(item.text, '\n')

    itens = soup.find_all('p')
    print(resposta.text, '\n')
   

    barra_esquerda = soup.find('ul', class_='menu nav')
    print(barra_esquerda)
    print(soup.title.name)
    
    #Pegar só o conteúdo
    linhas_barra_esquerda = barra_esquerda.find_all('li')
    for linha in linhas_barra_esquerda:
        print(linha.text)

    linhas_barra_esquerda = barra_esquerda.find_all('a')
    for linha in linhas_barra_esquerda:
        print(linha.text)






print(resposta)
print(resposta.content)
print(resposta.url)
print(resposta.status_code)



if(resposta.status_code == 200):
    print("sim")'''