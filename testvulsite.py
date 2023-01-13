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
        
        print("Website e seguro.")
    except Exception as e:
        print(f"um erro ocorreu: {e}")

def check_xss(text: str) -> None:
    """
            # Busca vulnerabilidades cross-site scripting (XSS) .
    """
    if "<script>" in text or "<script" in text:
        raise ValueError(" vulnerabilidade XSS detectado.")

def check_sql_injection(text: str) -> None:
    """
     # Busca por SQL injection.
    """
    if "SELECT" in text or "UPDATE" in text or "DELETE" in text:
        raise ValueError("SQL injection  detectado.")

def check_file_inclusion(text: str) -> None:
    """
    # Busca  por arquivo vulneravel.
    """
    if "include(" in text or "require(" in text:
        raise ValueError("arquivo vulneravel detectado.")

# Exemplo de uso
check_vulnerabilities("https://www.terra.com")