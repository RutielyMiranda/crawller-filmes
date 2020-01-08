import requests 
from bs4 import BeautifulSoup

top_ranking = []

def home():
    url = 'https://www.imdb.com/search/title/?release_date=2019&sort=num_votes,desc&page=2&ref_=adv_nxt'

    r = requests.get(url)
    html = r.text

    soup = BeautifulSoup(html, 'html.parser')
    for content in soup.find_all('div', class_ = 'lister-item mode-advanced'):
        parser_content(content)

def parser_content(content):
    header = content.find('h3', class_ = 'lister-item-header')
    title = header.find('a').string
    genre = content.find('span', class_ = 'genre').string

    content_star = content.find('div', class_ = 'ratings-bar')
    star = content_star.find('strong').string

    content_vote = content.find('p', class_ = 'sort-num_votes-visible')
    vote = content_vote.find('span', {'name':'nv'}).string
    
    data = {'title':title, 'genre':genre, 'star':star, 'vote':vote}
    top_ranking.append(data)

home()

print(top_ranking)