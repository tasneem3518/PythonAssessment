from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as Expected
from selenium.webdriver.support.wait import WebDriverWait



class DemoBlaze:

    def __init__(self):
        # initializing Chrome driver everytime the object is instantiated.
        self.driver = webdriver.Chrome(executable_path="C:\\Users\\adbul\\chromedriver_win32\\chromedriver.exe")
        self.driver.maximize_window()

    def navigate_to_website(self):
        # opening the web page
        baseURL = "https://www.demoblaze.com/"
        self.driver.get(baseURL)

    def new_user_creation(self):
        # signing up for new user
        login = True
        sign_in = self.driver.find_element(By.XPATH, "//*[@id='signin2']")
        sign_in.click()
        self.driver.implicitly_wait(1000)
        username_create = self.driver.find_element(By.ID, "sign-username")
        username_create.send_keys("Testing145")
        password_create = self.driver.find_element(By.ID, "sign-password")
        password_create.send_keys("testing")
        user_created = self.driver.find_element(By.XPATH, "//*[@id='signInModal']/div/div/div[3]/button[2]")
        user_created.click()
        if login:
            WebDriverWait(self.driver, 3).until(Expected.alert_is_present(),
                                                'Waiting for product added popup to appear')
            alert = self.driver.switch_to.alert
            alertmessagenew = alert.text
            if alertmessagenew == "This user already exist.":
                print("User exists already")
                alert.accept()
        else:
            print("User created successfully")
        close_button = self.driver.find_element(By.XPATH, "//*[@id='signInModal']/div/div/div[3]/button[1]")
        close_button.click()

    def new_user_login(self):
        #Logging with the user created in new_user_creation method.
        loginlink = self.driver.find_element(By.XPATH, "//*[@id='login2']")
        loginlink.click()
        self.driver.implicitly_wait(3)
        username = self.driver.find_element(By.ID, "loginusername")
        username.send_keys("Testing145")
        password = self.driver.find_element(By.ID, "loginpassword")
        password.send_keys("testing")
        loginbutton = self.driver.find_element(By.XPATH, "//*[@id='logInModal']/div[1]/div[1]/div[3]/button[2]")
        loginbutton.click()
        self.driver.implicitly_wait(10)

    def add_products_to_cart(self, number):
        #scrolling the page to find element.
        self.driver.execute_script("return document.body.scrollHeight")
        i = 1
        #Creating a while loop to add products to cart after selecting catalogue,clicking on product and adding to cart.
        while i <= number:
            catalog = self.driver.find_element(By.XPATH, "/html/body/div[5]/div/div[1]/div/a[2]")
            catalog.click()
            product = self.driver.find_element(By.XPATH, "//*[@id='tbodyid']/div['+i+']/div[1]/div[1]/h4[1]/a[1]")
            product.click()
            WebDriverWait(self.driver, 10).until(Expected.element_to_be_clickable(add_to_cart))
            add_to_cart = self.driver.find_element(By.XPATH, "//a[contains(@class, 'btn btn-success btn-lg')]")
            add_to_cart.click()
            WebDriverWait(self.driver, 10).until(Expected.alert_is_present(),
                                                 'Waiting for product added popup to appear')
            alert = self.driver.switch_to.alert
            alertmessage = alert.text
            if alertmessage == "Product added":
                print("Product added successfully")
                alert.accept
            else:
                print("No alert found")

    def delete_items_from_cart(self, count):
        items = self.driver.find_element(By.XPATH, "//div[@class='table-responsive']//tbody/tr[@class='success']")
        total_items = len(items)
        if total_items > 0:
            for count in range(total_items):
                delete = self.driver.find_element(By.XPATH, "//*[@id='tbodyid']/tr[1]/td[4]/a[1]")
                delete.click()
            print("Cart is empty")
        else:
            print("No item found to delete")

    def logout(self):
        logoutlink = self.driver.find_element(By.XPATH, "//*[@id='logout2']")
        logoutlink.click()

    # Press the green button in the gutter to run the script.


ff = DemoBlaze()
ff.navigate_to_website()
ff.new_user_creation()
ff.new_user_login()
ff.add_products_to_cart(2)
ff.delete_items_from_cart(2)
ff.logout()
ff.driver.implicitly_wait(1000)
ff.add_products_to_cart(1)
ff.delete_items_from_cart(1)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
