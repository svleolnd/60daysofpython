from bs4 import BeautifulSoup
import requests

url = "https://pt.wikipedia.org/wiki/Star_Wars"

headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)


if response.status_code == 200:
    print("Sucesso ao acessar a URL")
    
    # acessa a url e pega a html estruturada
    soup = BeautifulSoup(response.text, "html.parser")
    
    title = soup.title.string
    print(title)
    
    paragrafo_um = soup.find('p').text
    
    print(paragrafo_um)
    print("-------------------------")
    
    paragrafos = soup.find_all("p")
    
    if len(paragrafos) > 1:
        print(paragrafos[1].text)
    else:
        print("Nao existe mais de 1 paragrafo")
        
    links = soup.find_all("a", href=True)[:5]
    
    for link in links:
        print(link["href"])
        
        
else:
    print("Erro ao acessar a URL. Código:", response.status_code)