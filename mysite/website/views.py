from django.shortcuts import render,render_to_response
import urllib.request as request
import bs4 as bs
from . import Scrape_Titles_Politics as politics
from . import Scrape_Titles_Science as science
from . import Scrap_Titles_Business as business


request_bloomberg = request.Request('https://www.bloomberg.com/markets')
sauce_bloomberg = request.urlopen(request_bloomberg).read().decode('utf-8')
business_soup = bs.BeautifulSoup(sauce_bloomberg, 'html.parser')

politics_list = politics.produce_final_dictionary()
science_list = science.produce_final_dictionary()
business_list = business.get_articles(business_soup)

def index(request):
    top_stories = top_list(politics_list,science_list,business_list)
    context = {'topstories':top_stories}
    return render(request,'header.html',context)

def top_list(politics_list,science_list,business_list):
    new_list = [15]
    for i in range(5):
        new_list.append(politics_list[i])
        new_list.append(science_list[i])
        new_list.append(business_list[i])
    return new_list
