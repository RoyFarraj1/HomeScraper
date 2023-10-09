from argparse import Namespace
import requests
from bs4 import BeautifulSoup
from argparse import Namespace


r= requests.get('https://www.dubizzle.com.lb/properties/apartments-villas-for-sale/')
page_contents= r.text
doc_type=BeautifulSoup(page_contents, 'html.parser')

base_url = 'https://www.dubizzle.com.lb/'


span_tags = doc_type.find_all('span', class_ = '_95eae7db')


p_tags= doc_type.find_all('p')

matched_links = {}

for a_tag in doc_type.find_all('a', title=True):
    for p_tag in p_tags:
        if p_tag.text == a_tag['title']:
            matched_links[a_tag['href']] = p_tag.text

span_tags_1 = []

for tag in span_tags:
    span_tags_1.append(tag.text)


topic_urls = [base_url + href for href in matched_links.keys()]

  

import pandas as pd 

topics_dict= {
    'title': p_tags,
    'description': span_tags,
    'url': topic_urls
    
    
}

topic_dif= pd.DataFrame(topics_dict)


np= doc_type.find('a', class_ = '_19e1b955') .get('href')

Np_tags = (base_url + np)




print(len(p_tags))
print(len(span_tags))
print(len(topic_urls))

print('hdllpo')