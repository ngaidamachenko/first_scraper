# Welcome to My First Scraper
***************************************************************************

## Task
Using python libraries requests and beautifulsoup4, return a CSV of the TOP 25 trending repositories from Github.

- Request (with request)
- Extract (with beautifulsoup4)
- Transform    
- Format

## Description
Created four functions to fulfuil the task:
def request_github_trending(url) using request library to return the page.
def extract(page) using beautifulsoup4 library to extract content from the page.
def transform(articles) to filter and then transform the required content into a dictionary that contains name of the developer, name of the repository and number of stars received. 
def format(result) using csv library to return csv string with filtered data. 

## Installation
It works as a website scraper that retrieves data from github trending repositories.

## Usage
Using the commandline in terminal call the function with python my_first_scraper.py .It will return top-25 GitHub repositories.

./my_first_scraper.py url
```

### The Core Team
The project completed by Nikita Gaidamachenko

<span><i>Made at <a href='https://qwasar.io'>Qwasar SV -- Software Engineering School</a></i></span>
<span><img alt='Qwasar SV -- Software Engineering School's Logo' src='https://storage.googleapis.com/qwasar-public/qwasar-logo_50x50.png' width='20px'></span>
