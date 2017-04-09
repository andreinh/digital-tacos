import urllib.request as request
import bs4 as bs
import operator

request_the_verge = request.Request("http://www.theverge.com/science")
sauce_the_verge = request.urlopen(request_the_verge).read().decode('utf-8')
soup = bs.BeautifulSoup(sauce_the_verge, 'html.parser')


def get_article_urls(soup_object):
    list_of_urls = soup_object.find_all('a')
    list_of_a_tag_hrefs = []
    final_list_of_urls = []
    for item in list_of_urls:
        list_of_a_tag_hrefs.append(item.get('href'))
    for element in list_of_a_tag_hrefs:
        element = str(element)
        if element[:27] == 'http://www.theverge.com/201':
            if element in final_list_of_urls:
                pass
            else:
                final_list_of_urls.append(element)
        else:
            pass

    return final_list_of_urls


def get_article_title(article_url):
    request_article = request.Request(article_url)
    sauce_article = request.urlopen(request_article).read().decode('utf-8')
    soup_article = bs.BeautifulSoup(sauce_article, 'html.parser')
    article_title = soup_article.find('title').string

    return article_title[:-12]


def get_comment_counts(list_object):
    tuple_list = []
    for item in list_object[:20]:
        request_article = request.Request(item)
        sauce_article = request.urlopen(request_article).read().decode('utf-8')
        chickennoodle = bs.BeautifulSoup(sauce_article, 'html.parser')
        if type(chickennoodle.find('a', class_="p-comment-notification")) != bs.element.Tag:
            pass
        else:
            comment_count = chickennoodle.find('a', class_="p-comment-notification").find('span').string
        tuple_holder = (item, get_article_title(item), int(comment_count))
        if '#comments' in tuple_holder[0]:
            pass
        else:
            tuple_list.append(tuple_holder)

    return tuple_list


def produce_final_dictionary():
    placeholder = get_comment_counts(get_article_urls(soup))[-5:]
    placeholder.sort(key=operator.itemgetter(2))
    return placeholder
