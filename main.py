#Задание 1:

#Однопоточный вариант:

import requests

urls = ['https://www.google.com', 'https://www.yahoo.com', 'https://www.bing.com', 'https://www.amazon.com', 'https://www.apple.com', 'https://www.microsoft.com', 'https://www.wikipedia.org', 'https://www.twitter.com', 'https://www.facebook.com', 'https://www.instagram.com']

for url in urls:
    response = requests.get(url)
    print(response.content)

#Многопоточный вариант:

import requests
import threading

urls = ['https://www.google.com', 'https://www.yahoo.com', 'https://www.bing.com', 'https://www.amazon.com', 'https://www.apple.com', 'https://www.microsoft.com', 'https://www.wikipedia.org', 'https://www.twitter.com', 'https://www.facebook.com', 'https://www.instagram.com']

def get_content(url):
    response = requests.get(url)
    print(response.content)

threads = []

for url in urls:
    t = threading.Thread(target=get_content, args=(url,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

#Задание 2:

#Однопоточный вариант:


def search_files():
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.txt'):
                with open(os.path.join(root, file), 'r') as f:
                    if 'key' in f.read():
                        print(os.path.join(root, file))

search_files()

#Многопоточный вариант:

import os
import threading

def search_files(root, file):
    with open(os.path.join(root, file), 'r') as f:
        if 'key' in f.read():
            print(os.path.join(root, file))

def search_files_multithreaded():
    threads = []
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.txt'):
                t = threading.Thread(target=search_files, args=(root, file))
                threads.append(t)
                t.start()

    for t in threads:
        t.join()

search_files_multithreaded()