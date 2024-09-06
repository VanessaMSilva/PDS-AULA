import requests
from bs4 import BeautifulSoup
from model import Model_Mensagem




def return_dado():
    resposta = requests.get('http://www.prefe.ufu.br/concessoes/cantina-da-tia-lu')

    if resposta.status_code == 200:
        # Verifica a resposta HTML
        print("Resposta recebida com sucesso!")
        soup = BeautifulSoup(resposta.content, 'html.parser')
        
        # Imprime o HTML da página para análise
        #print(soup.prettify())  # Veja como está estruturada a página
        
        # Extraindo o título e conteúdo dos elementos HTML
        valor = soup.find('div', class_='region-content')
      
        if not valor:
            print("Erro: Não foi possível encontrar os itens necessários.")
            return None
        
        
        dados_menu= {
            "menuNav": "Web Scraping tia lu",
            "link": valor.text,
        }
        print(f'{dados_menu["menuNav"]}: {dados_menu["link"]}')
        
        return dados_menu
    else:
        print(f"Erro ao acessar o site: Status {resposta.status_code}")
        return None