from bs4 import BeautifulSoup
import requests
import pandas as pd




url = f'https://www.dubizzle.com.lb/properties/apartments-villas-for-sale/'
r = requests.get(url)
page_contents = r.text
doc_type = BeautifulSoup(page_contents, 'html.parser')

span_tags = doc_type.find_all('span', class_='_95eae7db')
p_tags = doc_type.find_all('p')
a_tags = doc_type.find_all('a', title=True)

matched_links = {}

for p_tag in p_tags:
    for a_tag in a_tags:
        if p_tag.text == a_tag['title']:
            matched_links[a_tag['href']] = p_tag.text

span_tags_1 = [tag.text for tag in span_tags]

base_url = 'https://www.dubizzle.com.lb/properties/apartments-villas-for-sale/'
topic_urls = [base_url + href for href in matched_links.keys()]

max_length = max(len(p_tags), len(span_tags), len(topic_urls))
p_tags.extend(['NA'] * (max_length - len(p_tags)))
span_tags_1.extend(['NA'] * (max_length - len(span_tags_1)))
topic_urls.extend(['NA'] * (max_length - len(topic_urls)))

data = {
'title': [],
'description': [],
'url': []
        }

data['title'].extend(p_tags)
data['description'].extend(span_tags_1)
data['url'].extend(topic_urls)


topic_df = pd.DataFrame(data)
print(topic_df)
