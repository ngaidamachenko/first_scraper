import requests
from bs4 import BeautifulSoup
import csv

url = 'https://github.com/trending'

def request_github_trending(url):
    git_request = requests.get(url)
    page = git_request
    return page

def extract(page):
    #page = request_github_trending(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    articles = soup.find_all('article', {'class':'Box-row'})
    return articles

def transform(articles):
    result = []
    for article in articles:
        #NAME = article.find({'class':'d-inline-block'}, {'href':True}).text.strip() - dont need curvy brackets for href, put it in one with class
        #NAME = article.find('a', {'class': 'd-inline-block', 'href': True}).text.split('/')[0]
        NAME = article.find('h1').text.split()[0].strip()
        REPOS_NAME = article.find('h1').text.split(' /')[1].strip()
        NBR_STARS = article.find('a',{'class':'Link--muted d-inline-block mr-3'}).text.strip()
        result.append({'developer': NAME, 'repository_name': REPOS_NAME, 'nbr_stars': NBR_STARS}) #dictionary 
    return result

def format(result):
    csv_string = 'Developer,Repository Name,Number of Stars\n' #header
    for article in result: #iterate over each line in the dictonary and return its value separated by a come and then create a new line for next repository row 
        developer = article['developer']
        name = article['repository_name']
        stars = article['nbr_stars']
        csv_string += f'{developer},{name},{stars}\n'
    return csv_string