


from base64 import standard_b64decode
from urllib import response
import webbrowser # web browser module to open websites

# list of urls: python
url_lists = [
    #'http://www.python.org',
    #'https://www.linkedin.com/in/fuad-hassan-18854a221/',
    #'https://github.com/fuadh246',
    #'https://twitter.com/Asabeneh',
]

# opens the above list of websites in a different tab
for url in url_lists:
    webbrowser.open_new_tab(url)

# Reading from URL

'''
We will see get, status_code, headers, text and json methods in requests module:

get(): to open a network and fetch data from url - it returns a response object
status_code: After we fetched data, we can check the status of the operation (success, error, etc)
headers: To check the header types
text: to extract the text from the fetched response object
json: to extract json data Let's read a txt file from this website, https://www.w3.org/TR/PNG/iso_8859-1.txt.

'''

import requests
url = 'https://www.w3.org/TR/PNG/iso_8859-1.txt'

response = requests.get(url)
response = requests.get(url) # opening a network and fetching a data
print(response)
print(response.status_code) # status code, success:200
print(response.headers)     # headers information
#print(response.text)

print()
print()


import requests

url = 'https://restcountries.com/v3.1/all'
response = requests.get(url)
print(response)
print(response.status_code)
countries = response.json()
#print(countries[0])


# how to use package

from mypacakge import greet
print(greet.greet_person('Fuad','hassan'))


print()
print()

import requests
url =  'http://www.gutenberg.org/files/1112/1112.txt'
words = dict()
response = requests.get(url)
if response.status_code == 200:
    list_of_words = response.text.split()
    for word in list_of_words:
        if word not in words:
            words[word] = 1
        else:
            words[word] += 1
words = dict(sorted(words.items(), key=lambda item: item[1],reverse=True)).items()
print(list(words)[:10])

#[{"weight":{"imperial":"7  -  10","metric":"3 - 5"}

import requests
from statistics import *
url = 'https://api.thecatapi.com/v1/breeds'
#cats_dict = dict()
response = requests.get(url)
#print(response.headers)
cats_dict = response.json()
weight_list =[]
print(type(cats_dict))
for cat in cats_dict:
    weight = cat['weight']['metric'].split()
    #mean(int(weight[0]))
    weight = cat['weight']['metric'].split()
    weight_list.append(int(weight[0]))
print(f'Mean : {mean(weight_list)}')
print(f'Max : {max(weight_list)}')
print(f'Min : {min(weight_list)}')
print(f'Median : {median(weight_list)}')





