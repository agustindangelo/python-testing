import requests
import pytest
from faker import Faker

fake = Faker()

class TestCreateBooks:
    base_url = "http://localhost:50000"

    def test_create_book(self):
        new_book = {
            "name": fake.name(),
            "author": fake.name(),
        }

        response = requests.post(f"{self.base_url}/books", json = new_book)
        book = response.json()

        assert response.status_code == 201, f"Expected status code to be 201, but got {response.status_code}"
        assert book["id"] is not None, "Book id is null"

    def test_try_to_create_an_existing_book(self):
        # precondition: the book should exist
        response = requests.get(f"{self.base_url}/books")
        first_book = response.json()[0]
        # ---------------

        new_book = {
            "name": first_book["name"],
            "author": first_book["author"]
        }
        response = requests.post(f"{self.base_url}/books", json = new_book)

        assert response.status_code == 400, f"Expected status code to be 400, but got {response.status_code}"
        assert f"Book with name: {first_book['name']} written by author: {first_book['author']} already exists" in response.text