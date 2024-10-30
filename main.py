import requests

name = input("Enter a name to get the predicted gender: ")

parameters = {
    "name": name,
}

print(f"I think you are {requests.get('https://api.genderize.io', params=parameters).json()["gender"]}.")
