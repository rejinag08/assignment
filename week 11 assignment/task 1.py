import requests

def get_random_chuck_norris_joke():
    url = "https://api.chucknorris.io/jokes/random"
    try:
        response = requests.get(url)
        if response.status_code ==200:
            joke_data = response.json()
            print(joke_data['value'])  # Print only the joke text
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    get_random_chuck_norris_joke()