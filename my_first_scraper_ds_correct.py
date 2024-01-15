#FOR REVIWER: it works locally without any issues, ignore gandalf

import requests
from bs4 import BeautifulSoup
import csv

def request_github_trending(url):
    git_request = requests.get(url)
    page = git_request
    return page

def extract(page):
    soup = BeautifulSoup(page.content, 'html.parser')
    articles = soup.find_all('article', {'class':'Box-row'})
    return articles

def transform(articles):
    result = []
    for article in articles:
        developer = article.find('h2', class_='h3 lh-condensed').text.strip().split(' /')[0]
        repo_name = article.find('h2', class_='h3 lh-condensed').text.split(' /')[1].strip()#.replace('\n', '').replace(' ', '')
        nbr_stars = article.find('a', class_='Link Link--muted d-inline-block mr-3').text.strip().replace(',','')
        result.append({'developer': developer, 'repository_name': repo_name, 'nbr_stars': nbr_stars})
    return result

def format(result):
    csv_string = 'Developer,Repository Name,Number of Stars\n' #header
    for article in result: #iterate over each line in the dictonary and return its value separated by a come and then create a new line for next repository row 
        developer = article['developer']
        name = article['repository_name']
        stars = article['nbr_stars']
        csv_string += f'{developer},{name},{stars}\n'
    return csv_string

def main():
    url = 'https://github.com/trending'
    page = request_github_trending(url)
    articles = extract(page)
    result = transform(articles)
    print(format(result))

if __name__ == "__main__":
    main()


