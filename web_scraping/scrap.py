import requests
from bs4 import BeautifulSoup
# import csv
   
URL = "https://www.w3schools.com/html/html_headings.asp"
# URL = "https://www.w3schools.com/html/html_paragraphs.asp"
# URL = "https://www.w3schools.com/html/html_styles.asp"

r = requests.get(URL)
   
soup = BeautifulSoup(r.content, 'html.parser')
subHeading, subHeadingList  =([] for i in range(2))
subHeadingIntro, subHeadings, allEaxmples =([] for i in range(3))

#convert list into string
def listIntoString(lists):    
    str1 =''
    for ele in lists:         
        str1 += ele  
    return str1

# here all p tags are passed which includes text all other headings also
# so here exatracting only needed text for 
def filterSubHeadingIntro(subHeadingIntro):
    removeStr = len(subHeadingIntro)
    i = -1
    subIntro = []
    lastItem = ""
    while removeStr > 0:   
        if( len(subHeadingIntro[i]) != 0 ):
            if(len(subIntro) == 0):
                subIntro.append(subHeadingIntro[i])
                lastItem = subHeadingIntro[i]
            else:
                subIntro.append(subHeadingIntro[i].replace(lastItem, ""))
                lastItem = subHeadingIntro[i]           
        i -= 1
        removeStr -= 1
    subIntro.reverse()
    return subIntro


# print("\n==========PAGE HEADING==============")
heading = soup.find_all('span', class_='color_h1')[0].get_text()

# print("\n==========INTRODUCTION==============")
intro = soup.find_all('p', class_='intro')[0].get_text()

# print("\n==========ALL SUB HEADINGS==============")
sub_heading = soup.find('hr')
sub_heading = sub_heading.find_next_siblings("h2")
for h in sub_heading:
    if(h.string == 'HTML Exercises'):
        break
    else:
        subHeadings.append(h.get_text())
 

# print("\n==========INTRO FOR ALL SUB HEADINGS==============")
sub_heading_intro = soup.find('div', id='main')
length = len(sub_heading_intro.find_all('hr'))
i=0
while i < length:
    sub = sub_heading_intro.find_all('hr')[i]
    sub = sub.find_next_siblings("p")
    for k in sub:      
        if(k.get_text() == intro):
            continue
        if(k.get_text().__contains__("W3Schools' tag reference contains")):
            continue
        else:  
            subHeadingList.append(k.get_text()) 
    str1 = listIntoString(subHeadingList)
    subHeadingList.clear()  
    if(str1 not in subHeadingIntro):
        subHeadingIntro.append(str1)               
    i += 1
# sending data for filtering
subHeadingIntro = filterSubHeadingIntro(subHeadingIntro)
        

# print("\n==========ALL EXAMPLES FOR SUB HEADINGS==============")
example = soup.select("div.w3-example div.notranslate")
for e in example:
    allEaxmples.append(e.get_text())

print(subHeadings)   

print("\n==========PAGE HEADING==============")
print(heading)

print("\n==========INTRODUCTION==============")
print(intro)

print("\n==========SUB HEADING +++ INTRO +++ EXAMPLES==============")
counter = 0
for head in subHeadings:
    print("\nSUB HEADING", counter+1)
    print("subHeadings => ",subHeadings[counter])
    print("subHeadingIntro =>", subHeadingIntro[counter])
    print("Eaxmples =>", allEaxmples[counter])
    counter += 1
    


  
