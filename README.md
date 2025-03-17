# AI_Similiarity_Matcher


## Overview

This project is a Flask-based API that retrieves the most similar content to a user's query using FAISS (Facebook AI Similarity Search). It utilizes Hugging Face's `sentence-transformers/all-mpnet-base-v2` model to generate embeddings and stores them in a FAISS vector database.

## Features

- Loads or creates a FAISS index from web content.
- Uses `sentence-transformers/all-mpnet-base-v2` for semantic similarity.
- Provides an API endpoint to return the most relevant content.

## Installation

### Prerequisites

Ensure you have the following installed:

- Python 3.8+
- pip

### Clone the Repository

```bash
git clone https://github.com/KrithikTheCoder/AI_Similiarity_Matcher.git
cd AI_Similiarity_Matcher
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Usage

### Running the API

```bash
python app.py
```

The API will start on `http://0.0.0.0:5001`

### API Endpoint

#### Query Similar Content

- **Endpoint**: `POST /query`
- **Request Body**:
  ```json
  {
    "query": "your search term here"
  }
  ```
- **Response**:
  ```json
  [
    {
      "content": "Relevant content snippet",
      "metadata": {}
    }
  ]
  ```

## FAISS Index Handling

- If a FAISS index exists, it loads it.
- If not, it scrapes the predefined URL(s) and creates a new FAISS index.


