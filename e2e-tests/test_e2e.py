from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from faker import Faker
import pytest

fake = Faker()

class TestE2EBooks:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:50001/")
        self.driver.implicitly_wait(5)
        self.wait = WebDriverWait(self.driver, 5)

    @pytest.mark.skip("Not implemented yet")
    def test_create_book(self):
        driver = self.driver

        new_book = {
            "name": fake.name(),
            "author": fake.name(),
        }

        driver.find_element(By.ID, "create").click()
        assert "/books/create" in driver.current_url

        driver.find_element(By.ID, "name").send_keys(new_book["name"])
        driver.find_element(By.ID, "author").send_keys(new_book["author"])
        driver.find_element(By.ID, "save").click()

        books_table = driver.find_elements(By.CSS_SELECTOR, "tbody tr")
        table_rows = [table_row.find_elements(By.TAG_NAME, "td") for table_row in books_table]
        books_names = [table_row[0].text for table_row in table_rows]

        assert new_book["name"] in books_names

    @pytest.mark.skip("Not implemented yet")
    def test_edit_book(self):
        driver = self.driver

        first_book = driver.find_elements(By.TAG_NAME, "tr")[1]
        first_book.click()

        self.wait.until(EC.element_to_be_clickable((By.ID, "edit")))
        edit_btn = driver.find_element(By.ID, "edit")
        edit_btn.click()

        author_field = self.wait.until(EC.visibility_of_element_located((By.ID, "author")))
        author_field.clear()
        author_field.send_keys("Agustin")
        driver.find_element(By.ID, "save").click()

        successfully_saved_alert = driver.find_element(By.CLASS_NAME, "alert-success")
        assert successfully_saved_alert.is_displayed()

        first_book = driver.find_elements(By.TAG_NAME, "tr")[1]
        new_author = first_book.find_elements(By.TAG_NAME, "td")[1].text
        assert new_author == "Agustin"

    # @pytest.mark.skip("Not implemented yet")
    def test_book_details(self):
        driver = self.driver

        first_book = driver.find_elements(By.CSS_SELECTOR, "tbody tr")[0]
        first_book_name = first_book.find_elements(By.TAG_NAME, "td")[0].text
        first_book_author = first_book.find_elements(By.TAG_NAME, "td")[1].text

        first_book.click()

        view_details_btn = driver.find_element(By.ID, "viewDetails")
        view_details_btn.click()

        driver.implicitly_wait(5)

        driver.get_screenshot_as_file("./e2e-tests/screenshots/screenshot.png")

        # wait = WebDriverWait(driver, 5)
        book_name_on_details_modal = self.wait.until(EC.visibility_of_element_located((By.ID, "book_name"))).text
        author_name_on_details_modal = self.wait.until(EC.visibility_of_element_located((By.ID, "book_author"))).text
        
        assert book_name_on_details_modal == first_book_name, "Book name on details modal is not the same as on the table"
        assert author_name_on_details_modal == first_book_author, "Author name on details modal is not the same as on the table"

    def teardown_method(self):
        self.driver.close()