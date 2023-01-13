import requests
from bs4 import BeautifulSoup

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

        soup = BeautifulSoup(response.text, 'html.parser')

        # Check for cross-site scripting (XSS) vulnerabilities.
        for tag in soup.find_all(['script', 'a']):
            if 'javascript:' in tag.get('href', '') or 'javascript:' in tag.get('onclick', ''):
                print(f"XSS vulnerability found in: {tag}")

        # Check for SQL injection vulnerabilities.
        for form in soup.find_all('form'):
            if 'sql' in form.get('action', ''):
                print(f"SQL injection vulnerability found in: {form}")
            for input_ in form.find_all('input'):
                if 'sql' in input_.get('name', ''):
                    print(f"SQL injection vulnerability found in: {input_}")

        # Check for file inclusion vulnerabilities.
        for tag in soup.find_all(['img', 'link']):
            if 'include' in tag.get('src', '') or 'require' in tag.get('src', ''):
                print(f"File inclusion vulnerability found in: {tag}")

        print("Website is secure.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
check_vulnerabilities("http://www.terra.com.br")