'''import time

#Fibonacci Sequence using recursion
print("Recursion Method")
num=int(input("Enter the number of terms: "))
def Fibonacci(idx):
    if idx<=1:
        return 1
    else:
        return Fibonacci(idx-1)+Fibonacci(idx-2)
for i in range(num):
    print(Fibonacci(i),end="\t")
rec=time.time()

print("Speed:- ",float(time.time()-rec))

print("\n")

#Fibonacci series using iteration
print("Iteration Method")
def fibonacci(idx):
    seq=[0,1]
    for i in range(idx):
        seq.append(seq[-1]+seq[-2])
    return seq[-1]
for i in range(num):
    print(fibonacci(i),end="\t")

it=time.time()

print("Speed:- ",float(time.time()-it))'''
import requests
import bs4 
res=requests.get("http://quotes.toscrape.com/")
print(res.text)
soup=bs4.BeautifulSoup(res.text,'lxml')
print(soup)
print(soup.select('.author'))
authors=set()
for name in soup.select(".author"):
    authors.add(name.text)
print(authors)
print(soup.select('.text'))
quotes=[]
for quote in soup.select('.text'):
    quotes.append(quote.text)
print(quotes)
print(len(soup.select('.tag-item')))
for item in soup.select('.tag-item'):
    print(item.text)
url='http://quotes.toscrape.com/page/'
#print(url+str(10))
authors=set()
for page in range(1,10):
    page_url=url+str(page)
    res=requests.get(page_url)
    soup=bs4.BeautifulSoup(res.text,'lxml')
    for name in soup.select("author"):
        authors.add(name.text)
print(authors)
page_url=url+str(999999999999)
res=requests.get(page_url)
soup=bs4.BeautifulSoup(res.text,'lxml')
print(soup)
print(res.text)
print("No quotes found!" in res.text)
page_still_valid=True 
authors=set()
page=1 
while page_still_valid:
    page_url=url+str(page)
    res=requests.get(page_url)
    if "No quotes found!" in res.text:
        break 
    soup=bs4.BeautifulSoup(res.text,"lxml")
    page+=1 
print(authors)
