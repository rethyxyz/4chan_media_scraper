#!/usr/bin/python3
import re, requests, time, sys, os
from requests_html import HTMLSession

def get_links(user_input):
    session = HTMLSession()
    x = session.get(user_input)
    links = x.html.links

    return links

def get_web_content(file_extension, links, photo_counter):
    x = re.compile(".*" + file_extension)
    links = list(filter(x.match, links))

    try:
        for link in links:
            photo_counter = int(photo_counter) + 1

            while (os.path.isfile(str(photo_counter) + "." + file_extension)):
                photo_counter = int(photo_counter) + 1

            req = requests.get('http:' + link)
            with open(str(photo_counter) + "." + file_extension, 'wb') as f:
                f.write(req.content)
    except:
        print(":: Skipped")

def main():
    if (len(sys.argv) <= 1):
        print(":: No args given")
    else:
        file_extensions = ["png", "gif", "jpg", "jpeg", "webm"]
        threads = []
        photo_counter = 0

        for arg in sys.argv:
            threads.append(arg)
            print(arg)
        threads.pop(0)

        for thread in threads:
            print(":: Getting files from", thread)

            links = get_links(thread)

            for extension in file_extensions:
                get_web_content(extension, links, photo_counter)

        print("Done")
        quit()

main()
