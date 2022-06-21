# Pet_project "Online store testing".
This is the final test project for the course [Test Automation with Selenium and Python](https://stepik.org/course/575/info)

The project used the [Page Object Model](https://www.selenium.dev/documentation/test_practices/encouraged/page_object_models/).

Page Object Model is a programming pattern that is very popular in test automation and is one of the standards in web product test automation and one of the convenient ways to structure your code in such a way that it is easy to maintain.

The basic idea is that each page of a web application can be described as a class object. The way a user interacts with a page can be described using class methods. Ideally, the test that will use the Page Object should describe the business logic of the test scenario and hide the Selenium methods for interacting with the browser and the page. If you make changes to the layout of a page, you won't have to fix the tests associated with that page. Instead, only the class that describes the page needs to be fixed.

Implemented several test cases for the main page of the online store and the product page.



To run the tests in need of review use the following command:
```pytest -v --tb=line --language=en -m need_review test_product_page.py```
