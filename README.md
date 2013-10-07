js-scraper
==========

This is a web scraper to scrap Jobstreet job board admin page for internal advertisement postings to do data analysis.
This page takes a raw HTML file from Jobstreet titled text.txt and scrapes the data and outputs a Microsoft Excel spreadsheet with the information titled demo.xlsx

This Python script uses the BeautifulSoup4 library to parse through the HTML file and XLSXWriter to output the data. This script uses lxml in the BeautifulSoup4 library.
