import time
from selenium.webdriver.common.by import By

def get_category_products(driver, category_url):
    driver.get(category_url)
    time.sleep(3)
    products = []
    product_elements = driver.find_elements(By.XPATH, "//div[@class='zg_itemWrapper']")
    for product in product_elements[:150]:
        product_data = {}
        try:
            product_data['Product Name'] = product.find_element(By.XPATH, ".//div[@class='p13n-sc-truncated']").text
            product_data['Product Price'] = product.find_element(By.XPATH, ".//span[@class='p13n-sc-price']").text
            product_data['Sale Discount'] = product.find_element(By.XPATH, ".//span[@class='a-price-whole']").text
            product_data['Best Seller Rating'] = product.find_element(By.XPATH, ".//span[@class='zg-badge-text']").text
            product_data['Rating'] = product.find_element(By.XPATH, ".//span[@class='a-icon-alt']").text
            product_data['Category Name'] = category_url.split("/")[-1]
            products.append(product_data)
        except Exception as e:
            print(f"Error extracting data for product: {e}")
    return products