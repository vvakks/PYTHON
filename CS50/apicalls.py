import requests


def main():
    print("Seartch the art institieu of chicgo")
    artist = input("Artist")
    try:
        response=requests.get("https://api.artic.edu/api/v1/artworks/search", {"q": artist})
        response.raise_for_status()
    except requests.HTTPError:
        print("Couldnt complete request")
        return
    content=response.json()
    for artwork in content["data"]:
        print(f"* {artwork['title']}")
    #print(content)
    
main()