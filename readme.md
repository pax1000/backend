# Egyptian E-commerce Price Scraper 🛒

A Python-based web scraper that extracts product data (title, price, availability, and links) from major Egyptian tech e-commerce websites. Perfect for price comparison and finding the best deals on electronics and computer hardware.

## 🌐 Supported Websites

- [`elbadrgroupeg.store`](https://elbadrgroupeg.store/) - Computer hardware and electronics
- [`elnekhelytechnology.com`](https://www.elnekhelytechnology.com/) - Technology products
- [`sigma-computer.com`](https://www.sigma-computer.com/) - Computer components and accessories  
- [`compumarts.com`](https://www.compumarts.com/) - IT products and electronics

## ✨ Features

- 🔍 **Multi-site scraping** with concurrent execution for faster data collection
- 📦 **Stock filtering** - automatically excludes out-of-stock items
- 🔄 **Infinite scroll support** - handles dynamic content loading and "load more" buttons
- 🗄️ **Database integration** - stores data in MySQL with duplicate handling
- 🔄 **Retry mechanism** - robust error handling with automatic retries
- 📊 **Search history tracking** - avoids redundant scraping of previously searched products
- 🤖 **Undetected browsing** - uses SeleniumBase with stealth mode to bypass anti-bot measures
- ⚡ **Headless operation** - runs efficiently without GUI overhead

## 📁 Project Structure

```
egyptian-ecommerce-scraper/
├── compumarts.py          # Compumarts.com scraper
├── elbadrgroupeg.py       # ElBadr Group scraper  
├── elnekhely.py           # ElNekhely Technology scraper
├── sigma.py               # Sigma Computer scraper
├── data_collection.py     # Main data aggregation logic
├── database.py            # MySQL database operations
├── searching.py           # Search history and user input handling
├── main.py               # Application entry point
├── used_token.json       # Search history tracking
├── .env                  # Database configuration (create this)
└── README.md
```

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.7+
- MySQL database
- Chrome browser (for Selenium automation)

### Install Dependencies
```bash
pip install seleniumbase selenium mysql-connector-python python-dotenv
```

### Database Setup
1. Create a MySQL database for the project
2. Create a `.env` file in the project root:
```env
DB_HOST=localhost
DB_USER=your_username
DB_PASS=your_password
DB_NAME=your_database_name
```

3. Create the products table:
```sql
CREATE TABLE products_info (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(500) NOT NULL,
    price INT,
    link VARCHAR(500) UNIQUE,
    in_stock BOOLEAN,
    store VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
```

## 🚀 Usage

### Basic Usage
```bash
python main.py
```
The program will prompt you to enter a product name to search for across all supported websites.

### How It Works
1. **Input**: Enter a product name when prompted
2. **Search History**: Checks if the product was previously searched to avoid redundant scraping
3. **Multi-threaded Scraping**: Simultaneously scrapes all 4 websites
4. **Data Processing**: Cleans and standardizes price data
5. **Database Storage**: Saves results to MySQL with duplicate handling
6. **Results**: View collected data in your database

## 🏗️ Technical Implementation

### Scraping Strategy
- **SeleniumBase** with undetected Chrome for bypassing anti-bot measures
- **Dynamic waiting** for elements to load properly
- **Infinite scroll handling** using JavaScript execution
- **Smart element detection** with multiple CSS selectors as fallbacks

### Data Processing
- **Price normalization** - extracts numeric values from price strings
- **Concurrent execution** - all scrapers run simultaneously using ThreadPoolExecutor
- **Error resilience** - continues operation even if individual scrapers fail
- **Data validation** - ensures consistent data structure across all sources

### Database Operations
- **Upsert functionality** - updates existing records or inserts new ones
- **Duplicate prevention** - uses unique constraints on product links
- **Optimized queries** - batch insertions for better performance

## 📊 Sample Output

```json
[
  {
    "title": "NVIDIA GeForce RTX 4070 Gaming Graphics Card",
    "price": 25000,
    "link": "https://example.com/product/rtx-4070",
    "in_stock": true,
    "store": "sigma"
  },
  {
    "title": "AMD Ryzen 7 5800X Processor",
    "price": 12500,
    "link": "https://example.com/product/ryzen-7-5800x", 
    "in_stock": true,
    "store": "compumarts"
  }
]
```

## ⚠️ Important Notes

- **Respect robots.txt** - The scrapers include delays and respectful browsing patterns
- **Rate limiting** - Built-in delays prevent overwhelming target servers
- **Legal compliance** - Ensure you comply with website terms of service
- **Maintenance required** - Websites may change their structure, requiring scraper updates

## 🔧 Configuration

### Timeout Settings
- Element wait timeouts can be adjusted in individual scraper files
- Database connection timeout is configurable via environment variables

### Retry Logic
- Failed scrapers automatically retry up to 3 times
- Individual scraper failures don't stop the entire process

## 🚧 Known Limitations

- **Captcha handling** - Some sites may require manual intervention for complex captchas
- **Dynamic pricing** - Prices may change between scraping sessions
- **Site structure changes** - Scrapers may need updates when websites modify their layouts
- **Geographic restrictions** - Some sites may block non-Egyptian IP addresses

## 🛣️ Roadmap

- [ ] **Web interface** - User-friendly GUI for easier product searching
- [ ] **API endpoints** - REST API for programmatic access
- [ ] **More websites** - Expand to additional Egyptian e-commerce platforms
- [ ] **Price tracking** - Historical price monitoring and alerts
- [ ] **Advanced filtering** - Category-based and specification-based filtering
- [ ] **Mobile app** - Native mobile application
- [ ] **Export features** - CSV/Excel export of comparison results

## 🤝 Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for:
- Adding new e-commerce websites
- Improving scraper reliability  
- Enhancing error handling
- Code optimization and refactoring

## 📄 License

This project is for educational and personal use. Please respect the terms of service of the scraped websites and use responsibly.

---
*Built with ❤️ for the Egyptian tech community*