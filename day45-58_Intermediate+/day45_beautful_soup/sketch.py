# from bs4 import BeautifulSoup

# with open('website.html') as file:
#     contents = file.read()

# soup = BeautifulSoup(contents, "html.parser")
# # print(soup.title.string)
# # print(soup.prettify())

# all_anchors = soup.find_all(name='a')

# # for tag in all_anchors:
# #     print(tag.getText())
# #     print(tag.get('href'))


# company = soup.select_one(selector='p a')
# print(company)

# headings = soup.select('.heading')
# print(headings)


from bs4 import BeautifulSoup
import requests

response = requests.get('https://news.ycombinator.com/news')
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, 'html.parser')
# link = soup.select_one(selector='.title a')
# link = soup.find(name='a', class_='storylink')

# article_tag = soup.find(name='a', class_='storylink')
# print(article_tag)

# article_text = article_tag.getText()
# print(article_text)

# article_link = article_tag.get('href')
# print(article_link)

# upvote_tag = soup.find(name='span', class_='score')
# article_upvote = upvote_tag.getText()

# print(article_upvote)


article_tags = soup.find_all(name='a', class_='storylink')
article_texts = []
article_links = []



for article in article_tags:
    new_text = article.getText()
    article_texts.append(new_text) 
    new_link = article.get('href')
    article_links.append(new_link)


article_upvotes = [int(score.getText().split()[0])for score in soup.find_all(name='span', class_='score')]
# article_upvote = upvote_tag.getText()

print(article_upvotes)
# max = 0
# for n in article_upvotes:
#     if n > max:
#         max = n
#         position = article_upvotes.index(n)
#         print(max)
#         print(position)

largest_num = max(article_upvotes)
position = article_upvotes.index(largest_num)

print(article_texts[position])
print(article_links[position])
# print(article_texts)
# print(article_links)
