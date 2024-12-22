from setup_webdriver import setup_driver
from login_amazon import login_amazon
from categories import categories
from scraper import get_category_products
from save_data import save_data_to_csv, save_data_to_json

def main():
    driver = setup_driver()
    username = "your_amazon_email"
    password = "your_amazon_password"
    login_amazon(driver, username, password)
    all_products = []
    for category_url in categories:
        products = get_category_products(driver, category_url)
        all_products.extend(products)
    save_data_to_csv(all_products, 'amazon_best_sellers.csv')
    save_data_to_json(all_products, 'amazon_best_sellers.json')
    driver.quit()

if __name__ == "__main__":
    main()
