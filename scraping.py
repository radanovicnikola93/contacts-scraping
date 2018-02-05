from urllib import urlopen
from BeautifulSoup import BeautifulSoup

url = 'https://scrapebook22.appspot.com/'
response = urlopen(url).read()
soup = BeautifulSoup(response)
# open or create CSV file
csv_file = open("email_list.csv", "w")

print soup.html.head.title.string
for link in soup.findAll("a"):
    if link.string == "See full profile":
        person_url = "https://scrapebook22.appspot.com" + link["href"]
        person_html = urlopen(person_url).read()
        person_soup = BeautifulSoup(person_html)
        print person_soup.find("span", attrs={"class": "email"}).string
        # get email and save it into CSV file
        email = person_soup.find("span", attrs={"class": "email"}).string
        csv_file.write(email + "\n")  # \n will create a new line


# close CSV file
csv_file.close()
