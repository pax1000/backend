# Product Search API

A FastAPI-based product search system with MySQL database integration, fuzzy search matching, and search analytics tracking.

## Features

- **Fast Product Search**: Search products with flexible partial matching
- **Search Analytics**: Track search terms and trending products
- **Fuzzy Matching**: Intelligent search term matching using thefuzz library
- **CORS Support**: Frontend integration ready
- **Database Integration**: MySQL database for product storage
- **Environment Configuration**: Secure credential management

## Tech Stack

- **Backend**: FastAPI, Python 3.x
- **Database**: MySQL
- **Search Engine**: thefuzz (fuzzy string matching)
- **Server**: Uvicorn/Gunicorn
- **Environment**: python-dotenv

## Installation

### Prerequisites

- Python 3.7+
- MySQL Server
- pip package manager

### Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd product-search-api
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Environment Configuration**
   
   Create a `.env` file in the root directory:
   ```env
   DB_HOST=your_mysql_host
   DB_USER=your_mysql_username
   DB_PASS=your_mysql_password
   DB_NAME=your_database_name
   ```

4. **Database Setup**
   
   Create a MySQL table with the following structure:
   ```sql
   CREATE TABLE products_info (
       id INT AUTO_INCREMENT PRIMARY KEY,
       title VARCHAR(255) NOT NULL,
       price DECIMAL(10, 2),
       description TEXT,
       category VARCHAR(100),
       brand VARCHAR(100),
       -- Add other relevant columns
       INDEX idx_title (title)
   );
   ```

## Usage

### Starting the Server

**Development:**
```bash
uvicorn api:app --reload --host 127.0.0.1 --port 8000
```

**Production:**
```bash
gunicorn api:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
```

### API Endpoints

#### Search Products
```http
GET /search/{product}
```
Search for products by name with fuzzy matching.

**Example:**
```bash
curl http://127.0.0.1:8000/search/rtx%204070
```

**Response:**
```json
[
  {
    "id": 1,
    "title": "NVIDIA RTX 4070 Graphics Card",
    "price": 599.99,
    "description": "High-performance graphics card...",
    "category": "GPU",
    "brand": "NVIDIA"
  }
]
```

#### Get Trending Products
```http
GET /trending
```
Get the most searched product terms and their search counts.

**Example:**
```bash
curl http://127.0.0.1:8000/trending
```

**Response:**
```json
[
  {
    "product_name": "4070",
    "search_count": 15
  },
  {
    "product_name": "i7 13700k",
    "search_count": 8
  }
]
```

## Project Structure

```
├── api.py                 # FastAPI application and routes
├── main.py               # Main processing logic
├── database.py           # MySQL database operations
├── searching.py          # Search analytics and fuzzy matching
├── requirements.txt      # Python dependencies
├── most_searched.json    # Trending products data
├── used_token.json      # Search term analytics
└── README.md            # Project documentation
```

## Configuration Files

### most_searched.json
Tracks popular product searches with their counts:
```json
[
  {"product_name": "4070", "search_count": 0},
  {"product_name": "i5 12400f", "search_count": 0}
]
```

### used_token.json
Detailed analytics for search categories and terms:
```json
[
  {
    "token": "GPU",
    "count": 23,
    "inputs": [
      {"term": "rtx", "count": 2},
      {"term": "4070", "count": 4}
    ]
  }
]
```

## Key Components

### Search Analytics System
The system tracks search patterns across multiple categories:
- **CPU**: Processors (Intel, AMD, Ryzen)
- **GPU**: Graphics Cards (RTX, RX series)
- **Motherboard**: Mainboards (AM4, AM5, LGA1700)
- **RAM**: Memory (DDR4, DDR5)
- **Storage**: SSDs, HDDs
- **Power Supply**: PSUs with wattage ratings
- **Peripherals**: Keyboards, mice, monitors

### Fuzzy Search Matching
Uses thefuzz library with 80% similarity threshold for intelligent search term matching, allowing users to find products even with typos or partial terms.

### Database Query Optimization
- Flexible LIKE matching with multiple search terms
- Dictionary cursor for easy result handling
- Proper connection management

## API Integration

### Frontend Integration
The API is configured with CORS to allow requests from `http://127.0.0.1:3000`, making it ready for React, Vue, or other frontend frameworks.

### Example Frontend Usage
```javascript
// Search for products
const searchProducts = async (query) => {
  const response = await fetch(`http://127.0.0.1:8000/search/${query}`);
  return await response.json();
};

// Get trending products
const getTrending = async () => {
  const response = await fetch('http://127.0.0.1:8000/trending');
  return await response.json();
};
```

## Error Handling

The application includes comprehensive error handling:
- Database connection errors
- Search processing errors
- JSON file operations
- Logging for debugging

## Performance Considerations

- Database connections are properly closed after queries
- Fuzzy matching threshold optimized for performance
- JSON files used for fast analytics access
- Indexed database columns for faster searches

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support and questions:
- Create an issue in the repository
- Check the logs for detailed error information
- Ensure all environment variables are properly configured

## Roadmap

- [ ] Add product categories filtering
- [ ] Implement price range search
- [ ] Add product image support
- [ ] Real-time search suggestions
- [ ] Advanced analytics dashboard
- [ ] Redis caching for improved performance
- [ ] Docker containerization
- [ ] API rate limiting
- [ ] User authentication system