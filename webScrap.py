import requests
from bs4 import BeautifulSoup
# import csv
   
URL = "https://www.w3schools.com/html/html_headings.asp"
r = requests.get(URL)
   
soup = BeautifulSoup(r.content, 'html.parser')

heading = soup.find_all('span', class_='color_h1')[0].get_text()
intro = soup.find_all('p', class_='intro')[0].get_text()

print("\n==========PAGE HEADING==============")
print(heading)

print("\n==========INTRODUCTION==============")
print(intro)

print("\n==========ALL SUB HEADINGS==============")
sub_heading = soup.find('hr')
sub_heading = sub_heading.find_next_siblings("h2")
for h in sub_heading:
    if(h.string == 'HTML Exercises'):
        break
    else:
        print(h.string)

print("\n==========INTRO FOR ALL SUB HEADINGS==============")
sub_heading = soup.find('div', id='main')
# print(sub_heading)
sub_heading = sub_heading.find('hr')
# print('===========================\n',sub_heading)
sub_heading = sub_heading.find_next_siblings("p")
# print(sub_heading)
for s in sub_heading:  
    print('\n\n',s)


print("\n==========ALL EXAMPLES FOR SUB HEADINGS==============")
example = soup.select("div.w3-example div.notranslate")
i = 1
for e in example:
    print("\nexample:",i , "=>", e.get_text())
    i += 1



