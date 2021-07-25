"""
python tutorial from 
https://www.youtube.com/watch?v=FoPPgcpSmNs
"""

import random
import requests
from bs4 import BeautifulSoup

url = 'https://www.imdb.com/chart/top'

def main():
    response = requests.get(url)
    html = response.text

    soup = BeautifulSoup(html, 'html.parser')
    movietags = soup.select('td.titleColumn')
    inner_movietags = soup.select('td.titleColumn a')
    
    ratingtags = soup.select('td.posterColumn span[name=ir]')

    years = [tag.text.split()[-1] for tag in movietags]
    titles = [tag.text for tag in inner_movietags]
    actors = [tag['title'] for tag in inner_movietags]
    ratings = [float(tag['data-value']) for tag in ratingtags]
    
    n_movies = len(titles)

    while(True):
        idx = random.randrange(0, n_movies)
        print(f'{titles[idx]}, {years[idx]}, rating: {ratings[idx]:.1f}, starring: {actors[idx]}')

        user_input = input('do you want another movie (y/[n])?')
        if user_input != 'y':
            break

if __name__ == '__main__':
    main()
    