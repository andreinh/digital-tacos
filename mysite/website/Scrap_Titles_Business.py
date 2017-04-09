import urllib.request as request
import bs4 as bs

request_bloomberg = request.Request('https://www.bloomberg.com/markets')
sauce_bloomberg = request.urlopen(request_bloomberg).read().decode('utf-8')
soup = bs.BeautifulSoup(sauce_bloomberg, 'html.parser')


def get_articles(soup_object):
    final_list = []
    big_article = soup.find('a', class_="hero-v2-big-story__headline-link")
    big_article_url = big_article.get('href')

    big_article_tuple = (big_article_url, big_article.string)
    final_list.append(big_article_tuple)

    list_of_doubles_articles = soup.find('a', class_="two-up-story__headline-link")
    for item in list_of_doubles_articles:
        doubles_article_tuple = (item.get('href'), item.string)
        if doubles_article_tuple in final_list:
            pass
        else:
            final_list.append(doubles_article_tuple)

    return final_list
