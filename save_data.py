import pandas as pd
import json

def save_data_to_csv(products, filename):
    df = pd.DataFrame(products)
    df.to_csv(filename, index=False)

def save_data_to_json(products, filename):
    with open(filename, 'w') as f:
        json.dump(products, f, indent=4)
