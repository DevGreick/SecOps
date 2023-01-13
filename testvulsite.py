import requests

def check_vulnerabilities(url: str) -> None:
    """
    Check for vulnerabilities in a website.
    """
    try:
        # Send a GET request to the website.
        response = requests.get(url)

        # Check the response status code.
        if response.status_code != 200:
            raise ValueError(f"Invalid status code: {response.status_code}")

        # Check for common vulnerabilities.
        check_xss(response.text)
        check_sql_injection(response.text)
        check_file_inclusion(response.text)
        
        print("Website is secure.")
    except Exception as e:
        print(f"An error occurred: {e}")

def check_xss(text: str) -> None:
    """
    Check for cross-site scripting (XSS) vulnerabilities.
    """
    if "<script>" in text or "<script" in text:
        raise ValueError("XSS vulnerability detected.")

def check_sql_injection(text: str) -> None:
    """
    Check for SQL injection vulnerabilities.
    """
    if "SELECT" in text or "UPDATE" in text or "DELETE" in text:
        raise ValueError("SQL injection vulnerability detected.")

def check_file_inclusion(text: str) -> None:
    """
    Check for file inclusion vulnerabilities.
    """
    if "include(" in text or "require(" in text:
        raise ValueError("File inclusion vulnerability detected.")

# Example usage
check_vulnerabilities("http://www.terra.com")