import random
import string
from faker import Faker
from data import UrlApi
import requests

class Person:
    fake = Faker()

    def generate_random_email(self):
        return self.fake.email()

    def generate_random_password(self, length=10):
        letters = string.ascii_letters
        return ''.join(random.choice(letters) for i in range(length))

    def generate_random_first_name(self):
        return self.fake.first_name()

def generation_new_data_user():
    person = Person()
    email_new = person.generate_random_email()
    password_new = person.generate_random_password()
    first_name_new = person.generate_random_first_name()

    data = {"email": email_new, "password": password_new, "name": first_name_new}
    return data

def generation_new_data_user_and_avtorization():
    user_data = generation_new_data_user()
    email = user_data["email"]
    password = user_data["password"]
    name = user_data["name"]

    payload = {
        "email": email,
        "password": password,
        "name": name,
    }

    # Create the new user
    response = requests.post(f"{UrlApi.CREATE_USER}", data=payload)

    if response.status_code == 200:
        return {
            "user_data": user_data,
            "token": response.json().get("accessToken"),
            "response": response
        }
    else:
        raise Exception("User creation failed")
