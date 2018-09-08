
# coding: utf-8

# In[140]:


import requests
from bs4 import BeautifulSoup


# In[141]:


res= requests.get('https://www.vsni.co.uk/software/genstat/htmlhelp/spread/DateFormats.htm')
soup= bs4.BeautifulSoup(res.content,'html.parser')
datafile = open('WSoutput.txt', 'a')
headers = soup.find_all("td" )
for i in range(len(headers)):
    datafile.write(headers[i].get_text())
    datafile.write('\n')
datafile.close()


# In[142]:



res= requests.get('https://slickdeals.net/')
soup= bs4.BeautifulSoup(res.content,'html.parser')
datafile = open('WSoutput.txt', 'a')
headers = soup.select('.itemPrice   ')
for i in range(len(headers)):
    datafile.write(headers[i].get_text())
datafile.close()   


# In[143]:


res= requests.get('https://www.nitt.edu/home/academics/contact_details/')
soup= bs4.BeautifulSoup(res.content,'html.parser')
datafile = open('WSoutput.txt', 'a')
headers = soup.select("td" )
for i in range(len(headers)):
    datafile.write(headers[i].get_text())
    datafile.write('\n')
datafile.close()


# In[144]:


res= requests.get('https://fakenumber.org/')
soup= bs4.BeautifulSoup(res.content,'html.parser')
datafile = open('WSoutput.txt', 'a')
headers = soup.find_all(lambda tag: tag and tag.get("class") == ["grid_6"])
for i in range(len(headers)):
    datafile.write(headers[i].get_text())
    datafile.write('\n')
datafile.close()


# In[145]:


res= requests.get('http://free-email-database.blogspot.com/2008/12/welcome-to-free-e-mail-database.html')
soup= bs4.BeautifulSoup(res.content,'html.parser')
datafile = open('WSoutput.txt', 'a')
headers = soup.find_all(lambda tag: tag and tag.get("class") == ["entry"] )
brk=str(headers[0]).split('<br/>')
for i in brk:
    soup1= bs4.BeautifulSoup(str(i)+'\n','html.parser')
    datafile.write(soup1.get_text())
datafile.close()

