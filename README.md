# Google-Books

## Background
Google-Books is a command line application that allows users to search the Google Books library for books, and to save specified books to a personal list.

## Getting Started
Before running Google-Books, we need to make sure to install certain technologies on your system -- namely: python3 and the 'requests' module for python.
- Install python3 on your system by following the instructions [here](https://realpython.com/installing-python)
- Using the code editor of your choice (e.g. Visual Studio Code), open this repository (which you should have downloaded as a zip file and extracted on your system locally) and enter the following command in your terminal: ``` py -m pip install requests ```    

You should now be all set up to run Google-Books! Just run the application by entering the following in your terminal: ``` py GoogleBooksAPI.py  ```, and follow the simple prompts that appear in the terminal.

## Functionality
- Upon running Google-Books, enter any part of the title of a book you want to search for.
- The search results will be limited to 5 results. You may elect to conduct a new search or save a book from the current query result to a personal list.
- Upon successfully saving a book to your list, the terminal should also now print your personal list of saved books.
- After saving a book, the application will prompt you to start another search, while retaining your saved books list.
