


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


