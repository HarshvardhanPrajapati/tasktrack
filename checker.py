import requests

def fetch_random_quote():
    url="https://zenquotes.io/api/random"
    try:
        response=requests.get(url)
        response.raise_for_status()
        data=response.json()
        if data:
            quote=data[0]['q']
            return quote
        else:
            return "Never lose hope"
    except requests.exceptions.RequestException as e:
        return f"error occured {e}"
 
print(fetch_random_quote())