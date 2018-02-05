from urllib import urlopen
from BeautifulSoup import BeautifulSoup
import re

url = 'https://scrapebook22.appspot.com/'
response = urlopen(url).read()
soup = BeautifulSoup(response)
# open or create CSV file
csv_file = open("list.csv", "w")

print soup.html.head.title.string
for link in soup.findAll("a"):
    if link.string == "See full profile":
        person_url = "https://scrapebook22.appspot.com" + link["href"]
        person_html = urlopen(person_url).read()
        person_soup = BeautifulSoup(person_html)
        #print person_soup.find("span", attrs={"class": "email"}).string
        # get email and save it into CSV file
        email = person_soup.find("span", attrs={"class": "email"}).string

        name = ''
        name_el = person_soup.findAll('h1')

        for el in name_el:
            if el.string != 'Hello, ninja!':
                name = el.string

        # city = person_soup.find('span', attrs={'data-city': re.compile("[A-Z][a-z]+")}).string
        city = person_soup.find('span', attrs={'data-city': True}).string
        print name, email, city
        person_string = '{name},{email},{city}\n'.format(name=name, email=email, city=city)
        csv_file.write(name + "," + email + "," + city + "\n")  # \n will create a new line


# close CSV file
csv_file.close()
