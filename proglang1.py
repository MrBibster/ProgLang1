import re
import requests
def urlcheck(url, megaurl,htmls,emails,goodemails):
    r = requests.get(url)
    content = r.content.decode('UTF-8')
    Badhtmls = re.findall("href=\"(http[s]?://[\w+\.]+\w+[[\/\w+]+]?)\"", content)
    emails = re.findall("\w+@\w+\.\w+", content)
    for n in range(len(emails)):
        if emails[n] not in goodemails:
            goodemails.append(emails[n])
    for n in range(len(Badhtmls)):
        temp = Badhtmls[n]
        if re.match(megaurl, temp) != None:
            if temp not in htmls:
                htmls.append(temp)
                urlcheck(temp, megaurl,htmls,emails,goodemails)

GoodEmails=[]
htmls = []
emails=[]
GoodHtmls = []

url = input('Введите URL')
urlcheck(url,url,GoodHtmls,emails,GoodEmails)
print(GoodHtmls)
print(GoodEmails)