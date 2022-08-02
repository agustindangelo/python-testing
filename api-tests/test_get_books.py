import unittest
import requests
import logging
import pytest

class TestGetBooks:
    base_url = "http://localhost:50000"

    def test_get_books(self):
        log = logging.getLogger("TestAPI.test_get_books")
        log.info("running get_books test")
        response = requests.get(f"{self.base_url}/books")

        books = response.json()

        assert response.status_code == 200
        assert len(books) > 0
        assert books[0]["id"] is not None, "Book id is null"
    
    def test_get_book(self):
        response = requests.get(f"{self.base_url}/books")
        book_to_query = response.json()[0]
        book_id_to_query = book_to_query["id"]

        response = requests.get(f"{self.base_url}/books/{book_id_to_query}")
        book = response.json()

        assert response.status_code == 200
        assert response.headers['Content-Type'] == "application/json", "Content-Type header is not application/json"
        assert book["id"] == book_to_query["id"]
        assert book["name"] == book_to_query["name"]
        assert book["author"] == book_to_query["author"]
        assert book["description"] == book_to_query["description"]
        assert book["cover"] == book_to_query["cover"]