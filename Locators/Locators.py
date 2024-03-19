from selenium.webdriver.common.by import By


class Locators:
    dialogOk = By.XPATH, '//button[contains(text(), "OK")]'
    loginDropdown = By.XPATH, '(//a[@data-bs-toggle="dropdown"])[2]'
    generalUser = By.XPATH, '//a[@href="/general-user/logIn/"]'
    email = By.ID, 'emailId'
    password = By.ID, 'password'
    buttonLogin = By.XPATH, '(//button[@id="btnLogin"])[1]'
    postAd = By.XPATH, '(//button[@id="signin_active_class"])[2]'
    sellRentButton = By.XPATH, '//p[contains(text(), " Sell, Rent, property, service & Job")]'
    electronics = By.XPATH, '(//ul[@id="category"])[1]/li/a'
    laptops = By.XPATH, '//li/a[contains(text(), "Laptops")]'
    title = By.XPATH, '//input[@id="title"]'
    condition1 = By.XPATH, '//span[@id="select2-condition-container"]'
    searchCondition = By.XPATH, '//input[@class="select2-search__field"]'
    new = By.XPATH, '//ul[@id="select2-condition-results"]'
    brand1 = By.XPATH, '//span[@id="select2-brand-container"]'
    hp = By.XPATH, '//ul[@id="select2-brand-results"]'
    model = By.XPATH, '//input[@id="modelName"]'
    displaySize = By.XPATH, '//input[@id="displaySize"]'
    ram = By.XPATH, '//input[@id="ram"]'
    processor = By.XPATH, '//input[@id="processor"]'
    hDD = By.XPATH, '//input[@id="hDD"]'
    price = By.XPATH, '//input[@id="price"]'
    # district = By.XPATH, '//span[@id="select2-district-container"]'
    district = By.XPATH, '//select[@id="district"]'
    # district = By.XPATH, '(//span[@class="select2-selection__arrow"])[3]'
    dhaka = By.XPATH, '//ul[@id="select2-district-results"]'
    # area = By.XPATH, '//span[@id="select2-thana-container"]'
    area = By.XPATH, '//select[@id="thana"]'
    aftagNagar = By.XPATH, '//ul[@id="select2-thana-results"]'
    phoneNumber = By.XPATH, '//input[@id="phoneNumber"]'
    image = "fileInput"
    submit = By.XPATH, '//button[contains(text(), " Submit")]'








