import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time

class PythonOrg_TestCase(unittest.TestCase):
    
    driver = None

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.python.org")
        assert "Python" in self.driver.title

    def tearDown(self):
        self.driver.close()
     
    def xtest_001_web_page_exists(self):
        assert "Python" in self.driver.title

    def xtest_002_query_returns_some_results(self):
        elem = self.driver.find_element_by_name("q")
        elem.clear()
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in self.driver.page_source

    def test_003_query_returns_at_least_3_results(self):
        elem = self.driver.find_element_by_name("q")
        elem.clear()
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in self.driver.page_source
        item_list = self.driver.find_element_by_class_name('list-recent-events')
        items = item_list.find_elements_by_tag_name("li")
        print(len(items))
        assert(len(items) >= 3)
        for item in items:
            print(item.text)

if __name__ == "__main__":
    unittest.main(verbosity=2)