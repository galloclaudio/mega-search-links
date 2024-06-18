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
