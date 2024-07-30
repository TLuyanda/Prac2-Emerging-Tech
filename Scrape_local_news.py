#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

# URL of the website you want to scrape
url = 'https://www.msn.com/en-za/sports/other/daniel-ricciardo-given-red-bull-lifeline-after-surprise-sergio-perez-call/ar-BB1qSCl3?ocid=entnewsntp&pc=LCTS&cvid=5d7e692929ac45488828eede6369c632&ei=40'  # Replace with the actual URL of the local news website

def scrape_headlines():
    try:
        # Send a GET request to the website
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the elements containing the headlines
        headlines = soup.find_all('h2', class_='headline')  # Adjust the tag and class to match the actual HTML structure

        # Print the extracted headlines
        print("Local News Headlines:")
        for idx, headline in enumerate(headlines, 1):
            print(f"{idx}. {headline.get_text()}")

    except requests.RequestException as e:
        print(f"Failed to retrieve the webpage. Error: {e}")

if __name__ == "__main__":
    scrape_headlines()
