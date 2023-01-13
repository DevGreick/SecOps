import requests
from bs4 import BeautifulSoup

def check_vulnerabilidade(url: str) -> None:
    """
    Verifica vulnerabilidades no website.
    """
    try:
        # Envia um GET request para o website.
        response = requests.get(url)

        # Checa se a resposta e 200.
        if response.status_code != 200:
            raise ValueError(f"Invalid status code: {response.status_code}")

        soup = BeautifulSoup(response.text, 'html.parser')

        # Busca vulnerabilidades cross-site scripting (XSS) .
        for tag in soup.find_all(['script', 'a']):
            if 'javascript:' in tag.get('href', '') or 'javascript:' in tag.get('onclick', ''):
                print(f"XSS encontrado em: {tag}")

        # Busca por SQL injection.
        for form in soup.find_all('form'):
            if 'sql' in form.get('action', ''):
                print(f"SQL injection  encontrado em: {form}")
            for input_ in form.find_all('input'):
                if 'sql' in input_.get('name', ''):
                    print(f"vuln SQL injection  encontrado em: {input_}")

        # Busca  por arquivo vulneravel.
        for tag in soup.find_all(['img', 'link']):
            if 'include' in tag.get('src', '') or 'require' in tag.get('src', ''):
                print(f"Arquivo  vulneravel encontrado em: {tag}")

        print("Site seguro.")
    except Exception as e:
        print(f"Um erro ocorreu: {e}")

# Exemplo
check_vulnerabilidade("http://www.terra.com.br")