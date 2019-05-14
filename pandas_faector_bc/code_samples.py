from ipywidgets import widgets
from IPython.display import display, clear_output

texts = {
    1: '''import requests\nfrom bs4 import BeautifulSoup''',
    2: '''url = "https://www.eur.nl/en/master/econometrics/study-programme"''',
    3: '''response = requests.get(url)
text = response.text
page_soup = BeautifulSoup(text, 'html.parser')
print(page_soup.prettify())''',
    4: '''- Course Overview
-- Block 1
--- Course X
     |  
     |  
-- Block 4+5
--- Course Y
```

```
- Electives
-- Block 1
--- Elective X
     |  
     |  
-- Block 4
--- Elective Y''',
    5: '''containers = page_soup.find_all("ul", {"class": "accordion-emphasize__content"})''',
    6: '''course_blocks = course_container.find_all("li", {"class": "category-block__item"})''',
    7: '''elective_blocks = elective_container.find_all("li", {"class": "category-block__item"})''',
    8: '''courses = course_blocks[0].find_all('li', {"class":"accordion__item"})''',
    9: '''title = courses[0].find_all('button')[0].text''',
    10: '''a = courses[0].find_all('a')[0]
link = a.attrs["href"]
code = link.split("/")[-1].replace(".htm", "").upper()''',
    11: '''def print_item(item):
    title = item.find_all('button')[0].text
    a = item.find_all('a')[0]
    link = a.attrs["href"]
    code = link.split("/")[-1].replace(".htm", "").upper()
    print(code, title)''',
    12: '''for block in elective_container.find_all("li", {"class": "category-block__item"}):
    for elective in block.find_all('li', {"class":"accordion__item"}):
        print_item(elective)''',
    13: '''for block in course_container.find_all("li", {"class": "category-block__item"}):
    for course in block.find_all('li', {"class":"accordion__item"}):
        print_item(course)''',
    14: '''def print_item(item):
    title = item.find_all('button')[0].text
    a_list = item.find_all('a')
    if len(a_list) > 0:
        a = item.find_all('a')[0]
        link = a.attrs["href"]
        code = link.split("/")[-1].replace(".htm", "").upper()
    else:
        code = None
    print(code, title)''',
}

def add_show_button(index):   
    def on_button_clicked(b):
        clear_output()
        print(texts[index])
           
    button = widgets.Button()
    button.description = "Show"
    button.on_click(on_button_clicked)
    
    display(button)