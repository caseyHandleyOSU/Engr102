
import requests
from time import sleep
from html.parser import HTMLParser
from bs4 import BeautifulSoup as bs
from quote import Quote

def main():
    url = 'https://quotes.toscrape.com'
    num = 1
    r = requests.get(url)
    soup = bs(r.content, 'html.parser')
    url_processing = url
    quotes = []
    while True: 
        print('Processing URL', url_processing)
        r = requests.get(url_processing)
        soup = bs(r.content, 'html.parser')
        quotes.extend(scrape_quotes(soup))
        num += 1   
        try:
            url_processing = url + get_next_url(soup)
            #sleep(1)
        except AttributeError:
            break
    
    num_tags = get_num_tags(quotes)
    tags_sorted = {k: v for k, v in list(reversed(sorted(num_tags.items(), key=lambda item: item[1])))}
    print('Answer 1:\n', _dict_to_str(tags_sorted, '   ',limit=10))
    print('Answer 2: The largest quote is:\n   ', get_largest_quote(quotes).quote)
    print('Answer 3: The shortest quote is:\n   ', get_shortest_quote(quotes).quote)
    num_quotes_author = get_author_quote_num(quotes)
    # Sort the number of quotes via author, including only authors that have more than one quote
    num_quotes_sorted = {k: v for k, v in list(reversed(sorted(num_quotes_author.items(), key=lambda item: item[1]))) if v > 1}
    print('Answer 4:\n', _dict_to_str(num_quotes_sorted, '   ', ' quotes\n'))

def get_next_url(soup: bs):
    next = soup.find('li',{'class': 'next'})
    return next.find('a')['href']

def get_largest_quote(quotes: list[Quote]):
    largest = quotes[0]
    for quote in quotes:
        if quote > largest:
            largest = quote
    
    return largest

def get_shortest_quote(quotes: list[Quote]):
    shortest = quotes[0]
    for quote in quotes:
        if quote < shortest:
            shortest = quote
    
    return shortest

def get_author_quote_num(quotes: list[Quote]):
    authors = {}
    for quote in quotes:
        if quote.author in authors.keys():
            authors[quote.author] = authors[quote.author] + 1
        else:
            authors[quote.author] = 1

    return authors

def scrape_quotes(soup: bs):
    quotes  = soup.find_all('div',{'class': 'quote'})
    proccessed_quotes = []
    for quote in quotes:
        text = quote.find('span',{'class':'text'}).get_text(strip=True)
        author = quote.find('small',{'class':'author'}).get_text(strip=True)
        tags = [t.get_text(strip=True) for t in quote.find_all('a',{'class':'tag'})]
        proccessed_quotes.append(Quote(author, text, tags))

    return proccessed_quotes


def get_num_tags(quotes: list[Quote]):
    tags = {}
    for quote in quotes:
        for t in quote.tags:
            if t in tags.keys():
                tags[t] = tags[t] + 1
            else:
                tags[t] = 1
    
    return tags

def _dict_to_str(input, prefix='', suffix='\n', limit=0):
    ret = ''
    if limit == 0:
        limit = len(input.keys())
    num = 0
    for k in input.keys():
        if num < limit:
            ret += prefix + str(k) + ' - ' + str(input[k]) + suffix
            num += 1
        else:
            break
    return ret


if __name__ == "__main__":
    main()