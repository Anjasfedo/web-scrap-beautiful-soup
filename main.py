from bs4 import BeautifulSoup

with open("index.html", "r") as html_file:
    content = html_file.read()
    # print(content)
    
    soup = BeautifulSoup(content, "lxml")
    
    # print(soup.prettify())
    
    # Search first element that found
    # tags = soup.find("h5")
    
    # Get all element
    # tags = soup.find_all("h5")
    
    courses_html_tags = soup.find_all("h5")
    
    for course in courses_html_tags: 
        print(course.text)
    
