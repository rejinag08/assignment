import requests

class Destination:
    def __init__(self, name, country):
        self.name = name
        self.country = country

class DomesticDestination(Destination):
    def __init__(self, name):
        super().__init__(name, "YourCountry")

class InternationalDestination(Destination):
    def __init__(self, name, country):
        super().__init__(name, country)

class User:
    def __init__(self, name, preference):
        self.name = name
        self.preference = preference  # "hot" or "cold"
        self.itineraries = []

    def add_itinerary(self, itinerary):
        self.itineraries.append(itinerary)

class Itinerary:
    def __init__(self, destination, weather, activities):
        self.destination = destination
        self.weather = weather
        self.activities = activities

api = "885bea98bb6d42f4cd3795ab7b715545"

def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        weather = data['weather'][0]['main']
        return temp, weather
    else:
        return None, None

def suggest_activities(weather):
    if weather.lower() in ["snow", "cold"]:
        return ["Skiing", "Hot Chocolate Tour"]
    elif weather.lower() in ["clear", "sunny"]:
        return ["Beach Day", "City Walking Tour"]
    elif weather.lower() in ["rain", "storm"]:
        return ["Museum Visit", "Indoor Attractions"]
    else:
        return ["Local Exploration"]

def suggest_destinations(destinations, preference):
    matched = []
    for dest in destinations:
        temp, weather = get_weather(dest.name)
        if temp is None:
            continue
        if preference == "hot" and temp >= 20:
            matched.append((dest, temp, weather))
        elif preference == "cold" and temp < 20:
            matched.append((dest, temp, weather))
    return matched

def main():
    destinations = [
        DomesticDestination("Helsinki"),
        InternationalDestination("Bangkok", "Thailand"),
        InternationalDestination("Reykjavik", "Iceland"),
        InternationalDestination("Barcelona", "Spain"),
    ]

    name = input("Enter your name: ")
    preference = input("Do you prefer hot or cold destinations? ").lower()
    user = User(name, preference)

    while True:
        print("\nSearching for destinations based on your preference...")
        matches = suggest_destinations(destinations, preference)

        if not matches:
            print("No destinations found. Try again later.")
            break

        print("\nRecommended Destinations:")
        for i, (dest, temp, weather) in enumerate(matches):
            print(f"{i + 1}. {dest.name} ({dest.country}) - {temp}°C, {weather}")

        choice = int(input("Select a destination by number (or 0 to exit): "))
        if choice == 0:
            break

        selected_dest, temp, weather = matches[choice - 1]
        activities = suggest_activities(weather)
        itinerary = Itinerary(selected_dest, weather, activities)
        user.add_itinerary(itinerary)

        print(f"\nItinerary for {selected_dest.name}:")
        print(f"Weather: {weather}, Temperature: {temp}°C")
        print("Recommended Activities:")
        for act in activities:
            print(f"- {act}")

        again = input("\nPlan another trip? (yes/no): ").lower()
        if again != "yes":
            break

    print("\nThank you for using the Travel Planner, {0}! Here are your itineraries:".format(user.name))
    for i, itin in enumerate(user.itineraries):
        print(f"\nTrip {i + 1}: {itin.destination.name} ({itin.destination.country})")
        print(f"Weather: {itin.weather}")
        print("Activities:")
        for act in itin.activities:
            print(f"- {act}")

if __name__ == "__main__":
    main()


