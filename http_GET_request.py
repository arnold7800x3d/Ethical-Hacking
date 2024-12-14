"""

Using the Requests library to perform a basic HTTP GET request

"""
import requests

def check_website(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"Successfully connected to {url}")
            print(f"Server: {response.headers.get('Server')}")
        else:
            print(f"Failed to connect to {url}. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occured: {e}")

check_website("https://www.example.com")