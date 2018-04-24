import requests
import random
import urllib
import time
import sys
import re
from unicodedata import normalize
from bs4 import BeautifulSoup


BASE_URL_444 = 'https://444.hu/2018/?page={}'
BASE_URL_DISQUS = 'https://disqus.com/embed/comments/?base=default&f=444hu&t_u={}&s_o=default'
OUTPUT_FILE = 'users.txt'
PAGES_TO_CRAWL = 2
COOKIES = {              # Application/Cookies in Chrome develper toolbar
    'PHPSESSID':     '', # https://444.hu
    'hubspotutk':    '', # https://disqus.com
    'disqus_unique': '', # https://disqus.com
}


def remove_accents(username):
    """
    Returns: <str>
    eg.: "lószőr" -> "loszor"
    """
    return str(normalize('NFKD', username).encode('ascii', 'ignore'), 'utf-8')


def mutate_username(username):
    """
    Returns: [<str>, <str>, ...] or []
    - Drop usernames longer than 10 (return empty list)
    - Remove accents
    - Add numbers 1-9, eg.: "user" -> ["user1", "user2", ...]
    """

    # http://www.pythonforbeginners.com/basics/list-comprehensions-in-python
    # TODO: implement what the function description says
    return [username + str(d) for d in range(10)]


def get_links_to_entries():
    """
    Returns: [<str>, <str>, ...]
    """
    
    links = set()
        
    # TODO: Iterate over first N pages of 2018 entries, get detail links
    try:
        resp = requests.get(BASE_URL_444.format(1))
    except requests.exceptions.ConnectionError:
        # They found the crawler, this is all we have
        return links

    # Parse retrieved document
    soup = BeautifulSoup(resp.text, 'html.parser')

    # Get all the links
    for a in soup.find_all('a'):
        href = a.attrs.get('href', '')

        # Filter links pointing at articles
        # TODO: filter links that START with 'https://444.hu/2018/'
        if 'https://444.hu/2018/' in href:
            links.add(href)
        
        links.add(href)
                
        print('[*] Found {} links to entries'.format(len(links)))

    return links
                
def get_usernames_from_comments(link):
    """
    Returns: [<str>, <str>, ...]
    Get usernames from disqus.com comments
    """

    # Construct and fetch a link that exists at disqus.com, use cookies to maintain session
    resp = requests.get(BASE_URL_DISQUS.format(urllib.parse.quote(link, safe='')),
                        cookies=COOKIES)

    # Find usernames with regular expression
    # TODO: filter out auto generated diqus.com names (the ones that contain "disqus_")
    # http://www.pythonforbeginners.com/basics/list-comprehensions-in-python
    # https://www.analyticsvidhya.com/blog/2015/06/regular-expression-python/
    return [u for u in re.findall('username"\:"(\w*)"', resp.text)]


def main():
    usernames = set()

    for link in get_links_to_entries():
        unames = get_usernames_from_comments(link)
        usernames.update(set(unames))

        print('[*] Found {} usernames for entry'.format(len(unames)))
        
    # Write results to file
    # TODO: mutate username
    with open(OUTPUT_FILE, 'w') as f:
        for username in usernames:
            f.write(username + '\n')


main()
