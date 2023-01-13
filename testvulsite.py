import requests

def check_vulnerabilities(url: str) -> None:
    """
    Verifica vulnerabilidades no website.
    """
    try:
          # Envia um GET request para o website.
        response = requests.get(url)

         # Checa se a resposta e 200.
        if response.status_code != 200:
            raise ValueError(f"Invalid status code: {response.status_code}")

        # Checa por vulnerabilidades comuns.
        check_xss(response.text)
        check_sql_injection(response.text)
        check_file_inclusion(response.text)
        
        print("Website is secure.")
    except Exception as e:
        print(f"An error occurred: {e}")

def check_xss(text: str) -> None:
    """
            # Busca vulnerabilidades cross-site scripting (XSS) .
    """
    if "<script>" in text or "<script" in text:
        raise ValueError("XSS vulnerability detected.")

def check_sql_injection(text: str) -> None:
    """
     # Busca por SQL injection.
    """
    if "SELECT" in text or "UPDATE" in text or "DELETE" in text:
        raise ValueError("SQL injection vulnerability detected.")

def check_file_inclusion(text: str) -> None:
    """
    # Busca  por arquivo vulneravel.
    """
    if "include(" in text or "require(" in text:
        raise ValueError("File inclusion vulnerability detected.")

# Exemplo de uso
check_vulnerabilities("http://www.google.com")