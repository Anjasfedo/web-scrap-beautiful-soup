# Import the BeautifulSoup class from the bs4 (Beautiful Soup 4) library
from bs4 import BeautifulSoup

# Open the HTML file named "index.html" in read-only mode
with open("index.html", "r") as html_file:
    
    # Read the content of the HTML file
    content = html_file.read()
    # Uncomment the line below to print the raw HTML content
    # print(content)

    # Create a BeautifulSoup object to parse the HTML content using the "lxml" parser
    soup = BeautifulSoup(content, "lxml")

    # Uncomment the line below to print the prettified HTML content
    # print(soup.prettify())

    # Search for the first occurrence of the HTML element with tag "h5"
    # Uncomment and modify the line below to search for a specific element
    # tags = soup.find("h5")

    # Get all HTML elements with tag "h5"
    # Uncomment and modify the line below to retrieve all matching elements
    # tags = soup.find_all("h5")

    # Uncomment the line below to find and print all HTML elements with tag "h5"
    # courses_html_tags = soup.find_all("h5")
    # for course in courses_html_tags:
    #     print(course.text)

    # Find all HTML elements with class "card" within a <div> tag
    course_cards = soup.find_all("div", class_="card")

    # Iterate through each course card and extract relevant information
    for course in course_cards:
        # Extract and print the text content of the <h5> tag within the course card
        course_name = course.h5.text

        # Extract the text content of the <a> tag within the course card,
        # split the text by spaces, and get the last element (presumably the price)
        course_price = course.a.text.split()[-1]

        # Print the course name and its corresponding price
        print(f"{course_name} costs {course_price}")
