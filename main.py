from database import get_data
from searching import update_token_and_terms
import logging
logging.basicConfig(level=logging.INFO)





def main_processing(product_name):
    search = update_token_and_terms(product_name)
    return get_data(search)

    




   