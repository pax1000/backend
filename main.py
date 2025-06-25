from database import add_to_database , get_data
from searching import update_token_and_terms
import logging


logging.basicConfig(level=logging.INFO)
logging.getLogger('seleniumbase').setLevel(logging.ERROR)
logging.getLogger('selenium').setLevel(logging.WARNING)
logging.getLogger('urllib3').setLevel(logging.WARNING)




def main_processing(product_name):
    found,result = update_token_and_terms(product_name)
    if not found:
        add_to_database(result)
    return get_data(product_name)

    




   