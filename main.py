# Import required modules
from bs4 import BeautifulSoup
import requests
import time

# URL of the job search website
URL = "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=golang&txtLocation="

# Prompt the user to enter a skill that is not familiar
print("Put some skill that is not familiar")
unfamiliar_skill = input(">")
print(f"Filtering out {unfamiliar_skill}")

# Function to find jobs on the specified URL
def find_jobs(URL):
    # Send an HTTP GET request to the specified URL and get the HTML content
    html_text = requests.get(URL).text

    # Create a BeautifulSoup object to parse the HTML content using the "lxml" parser
    soup = BeautifulSoup(html_text, "lxml")

    # Find all job listings on the page with the specified class
    jobs = soup.find_all("li", class_="clearfix job-bx wht-shd-bx")

    # Iterate through each job listing
    for index, job in enumerate(jobs):
        # Extract the published date of the job posting
        published_date = job.find("span", class_="sim-posted").span.text

        # Check if the job was posted recently (using the word "few" in the date)
        if "few" in published_date:
            # Extract company name, skills required, and more info URL
            company_name = job.find("h3", class_="joblist-comp-name").text.replace(" ", "")
            skills = job.find("span", class_="srp-skills").text.replace(" ", "")
            more_info = job.header.h2.a["href"]

            # Check if the unfamiliar skill is not present in the required skills
            if unfamiliar_skill not in skills:
                # Write job details to a text file
                with open(f"posts/job-{index}.txt", "w") as file:
                    file.write(f"Company Name: {company_name.strip()} \n")
                    file.write(f"Required Skills: {skills.strip()} \n")
                    file.write(f"More info: {more_info}")

                # Print a message indicating that the file has been saved
                print(f"File Saved: {index}")

# Main program execution
if __name__ == "__main__":
    # Run the job search function in a loop
    while True:
        find_jobs(URL)

        # Set a time interval to wait before the next job search (in minutes)
        time_wait = 10
        print(f'Waiting {time_wait} Minutes')
        
        # Pause the program for the specified time interval
        time.sleep(time_wait * 60)
