import mysql.connector
import logging
import os

def get_data(product_name):
    logging.info('🔍searching from database...')
    try:
        db = mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USER'),
            passwd=os.getenv('DB_PASS'),
            database=os.getenv('DB_NAME')
        )
        mycursor = db.cursor(dictionary=True)
        words = product_name.lower().split()
        conditions = " AND ".join(["LOWER(title) LIKE %s" for _ in words])
        params = [f"%{word}%" for word in words]
        query = f"SELECT * FROM products_info WHERE {conditions}"
        mycursor.execute(query, params)
        results = mycursor.fetchall()
        db.close()
        logging.info('✅ Finished querying database')
        return results
    except Exception as e:
        logging.error(f'there was an error connecting to the database as {e}')

def most_searched(searched):
    try:
        db = mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USER'),
            passwd=os.getenv('DB_PASS'),
            database=os.getenv('DB_NAME')
        )
        mycursor = db.cursor()
        query = "INSERT INTO most_searched (product_name, search_count) VALUES (%s, %s) ON DUPLICATE KEY UPDATE search_count = search_count + 1"
        mycursor.execute(query, (searched, 1))
        db.commit()
        db.close()
        logging.info('✅ Finished querying database')
    except Exception as e:
        logging.error(f'there was an error connecting to the database as {e}')

def get_most_searched():
    logging.info('🔍searching from database...')
    try:
        db = mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USER'),
            passwd=os.getenv('DB_PASS'),
            database=os.getenv('DB_NAME')
        )
        mycursor = db.cursor(dictionary=True)
        query = "SELECT product_name, search_count FROM most_searched"
        mycursor.execute(query)
        results = mycursor.fetchall()
        db.close()
        logging.info('✅ Finished querying database')
        return results
    except Exception as e:
        logging.error(f'there was an error connecting to the database as {e}')
