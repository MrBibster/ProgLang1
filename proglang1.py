import re
import requests
def urlcheck(url, megaurl,htmls,emails,goodemails):
    i=0
    r = requests.get(url)
    content = r.content.decode('UTF-8')
    Badhtmls = re.findall("href=\"(http[s]?://[\w+\.]+\w+[[\/\w+]+]?)\"", content)
    emails = re.findall("\w+@\w+\.\w+", content)
    for n in range(len(Badhtmls)):
        if re.match(megaurl, Badhtmls[n]) != None:
            i+=1
    if i==0:
        for n in range(len(emails)):
            if emails[n] not in goodemails:
                goodemails.append(emails[n])
        Badhtmls = re.findall("<a href=\"(/.+/)\">", content)
        for n in range(len(Badhtmls)):
            temp = megaurl+Badhtmls[n]
            if temp not in htmls:
                htmls.append(temp)
                urlcheck(temp, megaurl, htmls, emails, goodemails)
    else:
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