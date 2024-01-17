# Web Scraping Beautiful Soup Automation 🤖

This project consists of two Python scripts that automate the job search process on a specified website. The scripts utilize the BeautifulSoup library for web scraping.

## `local.py` 🕵️‍♂️

The `local.py` script is designed to parse an HTML file (`index.html`) locally and extract information about courses. The main functionalities include:

- Reading the content of the HTML file.
- Creating a BeautifulSoup object to parse the HTML content.
- Searching for specific HTML elements (e.g., `<h5>` and `<div class="card">`).
- Extracting and printing information from the parsed HTML.

You can uncomment specific lines in the script to enable different functionalities, such as printing raw HTML content or searching for specific elements.

## `main.py` 🚀

The `main.py` script automates the job search process on the TimesJobs website. Key features of the script include:

- Sending an HTTP GET request to the specified job search URL.
- Extracting job details (company name, required skills, more info URL) using BeautifulSoup.
- Filtering out jobs that require a specific skill provided by the user.
- Saving relevant job details to text files for further review.

The script runs in an infinite loop, periodically conducting job searches with a specified time interval between searches.

## Instructions 🛠️

1. **Requirements:**

   Install the required Python libraries using:

   ```
        pip install beautifulsoup4 requests
   ```

2. **Run `local.py`:**

   Modify the `index.html` file or use your own HTML file.
   Uncomment specific lines to enable different functionalities.

   ```
        python local.py
   ```

3. **Run `main.py`:**
   Enter a skill that you want to filter out from job listings when prompted.
   The script will continuously search for Golang-related jobs on TimesJobs.

    ```
        python main.py
    ```

## Closing Notes 📝

Feel free to adjust the configuration, and if you encounter any issues or have suggestions for improvement, please open an issue or submit a pull request.

Happy coding! 🚀👨‍💻
