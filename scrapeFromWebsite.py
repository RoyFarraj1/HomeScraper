from bs4 import BeautifulSoup
import requests
import pandas as pd 



# for i in range(3):
url=f'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw=iphone+14&_sacat=0'
r = requests.get(url)

html_content = r.text


parsed_html_content = BeautifulSoup(html_content, 'html.parser')
print(parsed_html_content)
#Description = parsed_html_content.find_all('span', role_ = 'heading')
price = parsed_html_content.find_all('span ', class_ = 's-item__price')
#link = parsed_html_content.find_all('a', class_ = 's-item__link')

#print(len(Description))
#Description_texts = [title.get_text() for title in Description]
#price_number = [prices.get_text() for prices in price]



#data = pd.DataFrame.from_dict( Description )

# data.to_excel('ebay.xlsx')

#print(data)

     #for a_tag in doc_type.find_all('a', title=True):
       #  for p_tag in p_tags:
           #  if p_tag.text == a_tag['title']:
             #    matched_links[a_tag['href']] = p_tag.text

    # span_tags_1 = []

    # for tag in span_tags:
    #     span_tags_1.append(tag.text)

    # base_url = 'https://www.dubizzle.com.lb/properties/apartments-villas-for-sale/'
    # topic_urls = [base_url + href for href in matched_links.keys()]

    # max_length = max(len(p_tags), len(span_tags), len(topic_urls))
    # p_tags.extend(['NA'] * (max_length - len(p_tags)))
    # span_tags_1.extend(['NA'] * (max_length - len(span_tags_1)))
    # topic_urls.extend(['NA'] * (max_length - len(topic_urls)))

    # topics_dict= {
    #        'title': span_tags_1 ,
    #        'description': p_tags,
    #         'url': topic_urls
        
        
    #         }

    
    

     
    # topic_dif= pd.DataFrame.from_dict(topics_dict)
    
    # topic_dif.to_excel('dubizlleprices.xlsx')
    # print(topic_dif)
    

 



    


        
    
 