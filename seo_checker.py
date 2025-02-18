# Import necessary libraries
import requests
from bs4 import BeautifulSoup

# Function to fetch and parse a webpage
def fetch_page(url):
    try:
        # Fetch the webpage
        response = requests.get(url)
        response.raise_for_status()  # Raises an error if the request fails
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup
    except Exception as e:
        print(f"Error fetching the page: {e}")
        return None

# Test the function with a sample URL
url = "https://example.com"  # Replace with any website URL
soup = fetch_page(url)

if soup:
    print("Page fetched successfully!")
    print(soup.prettify()[:500])  # Print first 500 characters of the HTML
else:
    print("Failed to fetch the page.")