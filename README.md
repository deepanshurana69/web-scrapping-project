# web-scrapping-project
Web Scraping

 Overview

The Web Scraping project demonstrates how Python can be used to collect structured information from a website.

The project uses Requests to retrieve web pages and BeautifulSoup to parse the HTML structure and extract useful information.

For this project, book information is collected from Books to Scrape, a website designed for practicing web scraping.


 Objectives
Retrieve HTML pages using Python.
Parse HTML content using BeautifulSoup.
Extract useful information from web pages.
Convert the extracted information into structured data.
Store the collected information in CSV format.

 
 Technologies Used
Python
Requests
BeautifulSoup
CSV
Pathlib

 
 Data Collected

The scraper collects information such as:

Book title
Price
Rating
Availability
Page number


Project Structure
Task1_Web_Scraping/
│
├── scrape_books.py
│
├── data/
│   └── books.csv
│
└── output/


How to Run

From the project root:

python Task1_Web_Scraping/scrape_books.py

The program collects the book information and saves the resulting dataset as:

Web_Scraping/data/books.csv

Key Learning Outcomes

Understanding HTML structure
Working with HTTP requests
Extracting information from HTML
Automating data collection
Creating structured datasets from web pages
