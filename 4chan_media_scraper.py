import re, requests, time, os, readline
from requests_html import HTMLSession

def get_links(user_input):
    session = HTMLSession()
    x = session.get(user_input)
    links = x.html.links
    return links

def download_content(file_extension, links, photo_counter):
    try:
        x = re.compile(".*" + file_extension)
        links_on_page = list(filter(x.match, links))

        for x in links_on_page:
            photo_counter = photo_counter + 1
            req = requests.get('http:' + x)
            with open(str(photo_counter) + "." + file_extension, 'wb') as f:
                f.write(req.content)
    except:
        print(":: broken link. skipping...")

def main():
    file_extensions = ["png", "gif", "jpg", "jpeg"]

    photo_counter = 0

    while (True):
        user_input = input("Insert URL(s)\nDelimit multiple links by using a space\n(Press Return to quit)\n> ")

        if (not user_input):
            print(":: ensure you remove downloaded images from current folder to avoid accidental overwrites")
            quit()

        threads = user_input.split(" ")

        for x in threads:
            print(":: getting files from", x)
            links = get_links(x)

            for x in file_extensions:
                download_content(x, links, photo_counter)

            print("Done")

main()
