import mysql.connector
import logging
import  os
from dotenv import find_dotenv,load_dotenv

# Load environment variables from .env file
dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

host = os.getenv("host")

# Function to insert or update product data in the database
def add_to_database(data):
    logging.info('💾 adding to database...')
    try :
        # Connect to MySQL database
        db = mysql.connector.connect(
                host=os.getenv('DB_HOST'),
                port=int(os.getenv('DB_PORT', 4000)),
                user=os.getenv('DB_USER'),
                password=os.getenv('DB_PASS'),
                database=os.getenv('DB_NAME'),
                ssl_disabled=False  
            )
        mycursor = db.cursor(dictionary=True)  # Use dictionary cursor for named column access

        # Loop through each product in the data list
        for product in data:
            title = product['title']
            price = product['price']
            link = product['link']
            in_stock = product['in_stock']
            store = product['store']
            try:
                # Attempt to insert the product
                query = 'INSERT INTO products_info (title, price, link, in_stock, store) VALUES (%s, %s, %s, %s, %s)'
                mycursor.execute(query,(title,price,link,in_stock,store))
                db.commit()
            except mysql.connector.Error as e:
                # Handle duplicate entry (error code 1062)
                if e.errno == 1062:
                    # Fetch existing product info
                    mycursor.execute('select id , price from products_info where link = %s', (link,))
                    result = mycursor.fetchone()
                    product_id = result['id']
                    old_price = result['price']
                    new_price = price

                    # Skip if price hasn’t changed
                    if old_price == new_price:
                        continue

                    # Insert price change into history and update product price
                    mycursor.execute('insert into price_history (product_id,old_price,new_price) values(%s,%s,%s)',(product_id,old_price,new_price))
                    mycursor.execute('UPDATE products_info SET price = %s WHERE id = %s',(new_price,product_id))
                    db.commit()
            
        logging.info('✅ finshed adding to database for data check your database')
    except Exception as e :
        logging.error(f'their was an error connecting to the database as {e}')



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
