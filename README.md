# ProductService

A FastAPI-based microservice for managing product data. This service allows importing products from an Excel file, creating products manually, and retrieving product information.

## Features

- Import product data from Excel files
- Create individual product entries
- Retrieve all stored products

## Tech Stack

- Python 3.10+
- FastAPI
- MongoDB (via pymongo)
- Pandas
- Uvicorn
- openpyxl (for Excel support)

## Getting Started

### Prerequisites

Make sure you have the following installed:

- Python 3.10 or above
- MongoDB running locally or in the cloud
- `virtualenv` (optional but recommended)

### Installation

```bash
# Clone the repository
git clone <repo-url>
cd ProductService

# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate     # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
