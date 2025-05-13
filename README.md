# ProductService

A FastAPI-based microservice for managing product data. This service allows importing products from an Excel file, creating products manually, and retrieving product information.

## Features

- Import product data from Excel files
- Create individual product entries
- Retrieve all stored products

## Tech Stack

- Python 3.10 or 3.11
- FastAPI
- MongoDB (via pymongo)
- Pandas
- Uvicorn
- openpyxl (for Excel support)
- Postman

## Getting Started

### Prerequisites

Make sure you have the following installed:

- Python 3.10 or above
- PyCharm or Visual Studio
- MongoDB running locally or in the cloud

### Installation

```bash
# Clone the repository
git clone https://github.com/sheetal-ut/ProductService
cd ProductService

# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate     # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

```
### Run the service in terminal
```bash
uvicorn app.main:app --reload
```
## API Endpoints

### Import Products from Excel
- Set the method to POST. 
- Set the URL to http://localhost:8000//import-excel. 
- In the Body tab, select form-data and upload the file field with the Excel file. 
- Hit Send to upload the file.

### Create Individual Product
```bash

{
  "product_name": "Laptop",
  "type": "High-end gaming laptop",
  "brand": "Dell",
  "price": 190000,
  "quantity": 10
}

```
- Set the method to POST. 
- Set the URL to http://localhost:8000/products. 
- In the Body tab, select raw and set the format to JSON. 
- Paste the JSON above and hit Send to create the product.

### GetProducts
Example Postman Request:
- Set the method to GET.
- Set the URL to http://localhost:8000/products.
- Hit Send to retrieve the list of products in JSON format.


