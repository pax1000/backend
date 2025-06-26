import mysql.connector
import logging
import  os
from dotenv import find_dotenv,load_dotenv

# Load environment variables from .env file
dotenv_path = find_dotenv()
load_dotenv(dotenv_path)
host = os.getenv("host")



def get_data(product_name):
    logging.info('🔍searching from database...')
    try:
        # Connect to MySQL database
        db = mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USER'),
            passwd=os.getenv('DB_PASS'),
            database=os.getenv('DB_NAME')
        )
        mycursor = db.cursor(dictionary=True)

        # Split search term into words for flexible LIKE matching
        words = product_name.lower().split()
        conditions = " AND ".join(["LOWER(title) LIKE %s" for _ in words])
        params = [f"%{word}%" for word in words]

        # Query products with partial match and order by price (numerically)
        query = f"SELECT * FROM products_info WHERE {conditions}"
        mycursor.execute(query, params)
        results = mycursor.fetchall()

        # Close connection and return results
        db.close()
        logging.info('✅ Finished querying database')
        return results
    except Exception as e:
        logging.error(f'there was an error connecting to the database as {e}')
