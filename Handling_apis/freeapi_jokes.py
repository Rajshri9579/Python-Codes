import requests

def fetch_random_jokes_freeapi():
    url = "https://api.freeapi.app/api/v1/public/randomjokes/joke/random"
    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data:
        joke_data = data["data"]
        joke = joke_data["categories"]["content"]
        id = joke_data["categories"]["id"]
        return joke,id
    else:
        raise Exception("Failed to fetch joke!!")
    

def main():
    try:
        joke = fetch_random_jokes_freeapi()
        print(f"Joke: {joke}")
    except Exception as e:
        print(str(e))

if __name__ =="__main__":
    main()