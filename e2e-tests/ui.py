import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class books_tests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    @unittest.skip("demonstrating skipping")
    def test_create_book(self):
        new_book = {
            "name": "The Lord of the Rings",
            "author": "J.R.R. Tolkien",
            "description": "A meaningful description for a meaningful book",
            "cover_link": "https://images-na.ssl-images-amazon.com/images/I/51-X-Q-X-QL._SX331_BO1,204,203,200_.jpg"
        }

        driver = self.driver
        driver.get("http://localhost:50001/")

        driver.find_element(By.ID, "create").click()
        assert "/books/create" in driver.current_url

        driver.find_element(By.ID, "name").send_keys(new_book["name"])
        driver.find_element(By.ID, "author").send_keys(new_book["author"])
        driver.find_element(By.ID, "description").send_keys(new_book["description"])
        driver.find_element(By.ID, "cover").send_keys(new_book["cover_link"])
        driver.find_element(By.ID, "save").click()

        books_table = driver.find_elements(By.CSS_SELECTOR, "tbody tr")
        table_rows = [table_row.find_elements(By.TAG_NAME, "td") for table_row in books_table]
        books_names = [table_row[0].text for table_row in table_rows]

        assert new_book["name"] in books_names

    @unittest.skip("demonstrating skipping")
    def test_edit_book(self):
        driver = self.driver
        driver.get("http://localhost:50001/")

        first_book = driver.find_elements(By.TAG_NAME, "tr")[0]
        first_book_name = first_book.find_elements(By.TAG_NAME, "td")[0].text
        first_book_author = first_book.find_elements(By.TAG_NAME, "td")[1].text

        first_book.click()
        edit_btn = driver.find_element(By.ID, "edit")
        edit_btn.click()

        assert driver.find_element(By.TAG_NAME, "h1").text == "Edit Book"

        author_field = driver.find_element(By.ID, "author")
        author_field.clear()
        author_field.send_keys("Agustin")
        driver.find_element("#save").click()

        successfully_saved_alert = driver.find_element(By.CLASS_NAME, "alert-success")
        assert successfully_saved_alert.is_displayed()

        first_book = driver.find_elements(By.TAG_NAME, "tr")[0]
        new_author = first_book.find_elements(By.TAG_NAME, "td")[1].text
        assert new_author == "Agustin"

    def test_book_details(self):
        driver = self.driver
        driver.get("http://localhost:50001/")

        first_book = driver.find_elements(By.CSS_SELECTOR, "tbody tr")[0]
        first_book_name = first_book.find_elements(By.TAG_NAME, "td")[0].text
        first_book_author = first_book.find_elements(By.TAG_NAME, "td")[1].text

        first_book.click()

        view_details_btn = driver.find_element(By.ID, "viewDetails")
        view_details_btn.click()

        wait = WebDriverWait(driver, 5)
        wait.until(EC.element_to_be_clickable((By.ID, "edit")))
        assert driver.find_element(By.CSS_SELECTOR, ".modal-content").is_displayed
        book_name = driver.find_element(By.ID, "book_name").text
        author_name = driver.find_element(By.ID, "book_author").text
        
        print(f'{book_name} by {author_name}')

        assert driver.find_element(By.ID, "book_name").text == first_book_name
        assert driver.find_element(By.ID, "book_author").text == first_book_author

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()