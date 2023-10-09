from bs4 import BeautifulSoup
import requests
import pandas as pd 
import xlsxwriter
all_data = []


for i in range(1,20):
    url=f'https://www.dubizzle.com.lb/properties/apartments-villas-for-sale/?page={i}'
    r = requests.get(url)

    page_contents= r.text

    doc_type =BeautifulSoup(page_contents, 'html.parser')

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

    base_url = 'https://www.dubizzle.com.lb/properties/apartments-villas-for-sale/'
    topic_urls = [base_url + href for href in matched_links.keys()]

    max_length = max(len(p_tags), len(span_tags), len(topic_urls))
    p_tags.extend(['NA'] * (max_length - len(p_tags)))
    span_tags_1.extend(['NA'] * (max_length - len(span_tags_1)))
    topic_urls.extend(['NA'] * (max_length - len(topic_urls)))

    topics_dict= {
           'title': span_tags_1 ,
           'description': p_tags,
            'url': topic_urls
        
        
            }
    topic_data= pd.DataFrame.from_dict(topics_dict)
   
    all_data.append(topic_data)

    final_data = pd.concat(all_data)
    final_data.to_excel('dubizlleprices.xlsx', index=False)
    print(final_data)
    

     
    topic_dif= pd.DataFrame.from_dict(topics_dict)
    

   
    

 



    


        
    
 