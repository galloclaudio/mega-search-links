# URL Fetcher Tool

## Overview

The URL Fetcher Tool is a Python-based application designed to retrieve URLs from an internal API provided by Meawfy. This tool connects to the API, processes the JSON results containing URLs, and displays them in a user-friendly format. It is highly customizable, allowing users to modify the user-agent for their HTTP requests.

## Purpose

The primary purpose of this tool is to facilitate the retrieval of URLs from Meawfy's internal API. These URLs can represent various types of resources such as articles, images, videos, or other web pages. By automating the fetching and processing of these URLs, users can streamline their workflows, particularly in environments where bulk data processing is required.

You can check more usages and information in https://meawfy.com

## Features

- **Customizable User-Agent:** Allows modification of the user-agent to mimic different browsers or clients.
- **Error Handling:** Robust error handling to manage HTTP request issues.
- **Modular Design:** Encapsulated functionality within a class for easy maintenance and extension.

## Real-World Use Cases

Meawfy's internal API provides URLs that can link to diverse content, including but not limited to:
- **Articles and Blog Posts:** Useful for content aggregation, SEO analysis, and competitive research.
- **Multimedia Resources:** Access to images, videos, and other media can support digital marketing campaigns, content creation, and more.
- **Data Aggregation:** Ideal for applications requiring bulk data collection, such as market analysis, academic research, and automated reporting.

## Requirements

- Python 3.x
- `requests` library

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/galloclaudio/mega-search-links
    ```
2. Navigate to the project directory:
    ```bash
    cd mega-search-links
    ```
3. Install the required dependencies:
    ```bash
    pip install requests
    ```

## Usage

1. Open the `main.py` file and modify the `search_query` variable with your desired query.
2. Customize the `user_agent` variable if needed.
3. Run the script:
    ```bash
    python main.py
    ```

## Code Structure

```python
import requests

class URLFetcher:
    def __init__(self, base_url, user_agent):
        """
        Initializes the URLFetcher with a base URL and user-agent.
        
        Parameters:
        base_url (str): The base URL for the API.
        user_agent (str): The user-agent string to be used for the requests.
        """
        self.base_url = base_url
        self.headers = {'User-Agent': user_agent}

    def fetch_urls(self, search_query):
        """
        Fetches URLs from the API based on the search query.

        Parameters:
        search_query (str): The query string for the API search.

        Returns:
        list: A list of URLs retrieved from the API.
        """
        try:
            # Construct the complete URL with the search query
            url = f"{self.base_url}?q={search_query}"
            
            # Send a GET request to the API
            response = requests.get(url, headers=self.headers)
            
            # Raise an HTTPError for bad responses (4xx and 5xx)
            response.raise_for_status()
            
            # Parse the JSON response
            data = response.json()
            
            # Extract URLs from the data
            urls = data.get('urls', [])
            return urls
        
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return []

def main():
    # Base URL of the API
    base_url = "https://meawfy.com/internal/api/results.json"
    
    # User-agent string
    user_agent = "MyCustomUserAgent/1.0"
    
    # Initialize the URLFetcher with the base URL and user-agent
    url_fetcher = URLFetcher(base_url, user_agent)
    
    # Example search query
    search_query = "example_query"
    
    # Fetch URLs based on the search query
    urls = url_fetcher.fetch_urls(search_query)
    
    # Display the retrieved URLs
    if urls:
        print("Retrieved URLs:")
        for url in urls:
            print(url)
    else:
        print("No URLs found or an error occurred.")

if __name__ == "__main__":
    main()
```


## License
This project is licensed under the MIT License. See the LICENSE file for more details.

## Contributing
Contributions are welcome! Please fork this repository and submit a pull request with your changes. Make sure to follow the existing code style and include comments for any new functionality.

## About Meawfy

Meawfy is a powerful search engine designed to help users find a wide variety of files hosted on Mega.nz. The platform enables users to search for movies, games, courses, software, e-books, music, TV series, documentaries, tutorials, video games, and more. It aims to promote learning and education by providing access to public domain and legally shared content, while ensuring compliance with copyright regulations and swiftly removing any illegal material reported by users. Meawfy is committed to maintaining high ethical standards and supporting the distribution of educational and creative materials.
