import requests
def main():
    ligma = requests.get("rest.coincap.io/v3/assets/bitcoin?apiKey=YourApiKey")
    print(ligma.json())
main()
    