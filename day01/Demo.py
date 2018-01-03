# Author xsj
from urllib import request,parse;
import urllib.error;
import socket;
from  urllib.parse import urlparse;
import requests;
from requests.packages import urllib3;
import re;
from bs4 import BeautifulSoup;
from pyquery import PyQuery as pq
from selenium import webdriver;
pagesnum = 2;
data = {
    'pagesnum':pagesnum
}
response = requests.post("http://www.hshfy.sh.cn/shfy/gweb/ktgg_search_content.jsp",data=data)

content = response.text;
doc = pq(content);
firstTable = doc('table tbody tr').items();
for item in firstTable:
    print(item.text());

# i = 0;
# for iten in tbodys:
#     i+=1;
#     print(iten)
#
# print(i)







# browser = webdriver.Chrome()
# url = 'https://www.zhihu.com/explore'
# browser.get(url)
# logo = browser.find_element_by_id('zh-top-link-logo')
# print(logo)
# print(logo.get_attribute('class'))

# browser = webdriver.Chrome()
# browser.get("http://www.zhihu.com/explore")
# browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
# browser.execute_script('alert("To Bottom")')
# browser.get("http://www.taobao.com")
# input_first = browser.find_element_by_id("q")
# input_second = browser.find_element_by_css_selector("#q")
# input_third = browser.find_element_by_xpath('//*[@id="q"]')
# print(input_first)
# print(input_second)
# print(input_third)
# browser.close()






# help(webdriver);
# browser = webdriver.Chrome()
#
# browser.get("http://www.baidu.com")
# print(browser.page_source)
# browser.close()
# browser = webdriver.Chrome();
# browser.get("http://www.baidu.com");
# print(browser.page_source);
# browser.close()








# html = '''
# <html><head><title>The Dormouse's story</title></head>
# <body>
# <p class="title"><b>The Dormouse's story</b></p>
#
# <p class="story">Once upon a time there were three little sisters; and their names were
# <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
# <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
# <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
# and they lived at the bottom of a well.</p>
# <p class="story">...</p>
# '''

# soup = BeautifulSoup(html,'html');
# print(soup.prettify());
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.title.parent.name)
# print(soup.p)
# print(soup.p["class"])
# print(soup.a)






# response = requests.get("https://book.douban.com/");
# response.encoding = "utf-8";
# content = response.text;
# pattern = re.compile('<li.*?cover.*?href="(.*?)".*?title="(.*?)".*?more-meta.*?author">(.*?)</span>.*?year">(.*?)</span>.*?</li>', re.S)
# results = re.findall(pattern,content);
# print(results);
# for result in results:
#     url,name,author,date = result
#     author = re.sub('\s','',author)
#     date = re.sub('\s','',date)
#     print(url,name,author,date)




# urllib3.disable_warnings();
# response = requests.get("https://www.12306.cn",verify = False);
# print(response.status_code);


# proxies = {
#     "https":"http://127.0.0.1:9999",
#     "https":"https://127.0.0.1:8888"
# }
# response = requests.get("http://www.baidu.com",proxies=proxies);
# response.encoding="utf-8";
# print(response.text);


# heads = {
#
#     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4295.400 QQBrowser/9.7.12661.400'
#
# }
# response = requests.get('http://www.zhihu.com',heads=heads);
# print(response);





# response = requests.get('http://www.baidu.com')
# response.encoding='utf-8';
# print(response.text);
#print(response.content.decode('utf-8'))







# try:
#     response = urllib.request.urlopen('http://github.com',timeout=0.1);
#     print(response.read());
# except urllib.error.URLError as e:
#     if isinstance(e.reason,socket.timeout):
#         print('TIME_OUT');

# response = urllib.request.urlopen("http://www.python.org");
# print(type(response));
# print(response.status);
# print(response.getheaders())

# request = urllib.request.Request('http://baidu.com');
# response = urllib.request.urlopen(request);
# print(response.read().decode('utf-8'));

# result = urlparse("http://www.baidu.com/index.html/user?id=5#commit");
# print(result)