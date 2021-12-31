# Google-Books

## Background
Google-Books is a command line application that allows users to search the Google Books library for books, and to save specified books to a personal list.

## Getting Started
Before running Google-Books, we need to make sure to install certain technologies on your system -- namely: python3 and the 'requests' module for python.
- Install python3 on your system by following the instructions [here](https://realpython.com/installing-python)
- Using the code editor of your choice (e.g. Visual Studio Code), open this repository (which you should have downloaded as a zip file and extracted on your system locally) and enter the following command in your terminal: ``` py -m pip install requests ```
You should now be all set up to run Google-Books! Just run the application by entering the following in your terminal: ``` py GoogleBooksAPI.py  ```, and follow the simple prompts that appear in the terminal.

## Features

### Fighter List Module
- BoxStats features a side module, listing the top 50 active boxers (according to their current BoxRec 'pound-for-pound' rankings).
- Users can click on a fighter's name from the module to render their bio and fight stats. 

### Career Stats
- A fighter's career stats will appear at the bottom of the page simultaneously with the rendering of the aforemention fighter bio/snapshot.
- Career Stat charts consist of four distinct charts (career: (1)bouts, (2)rounds, (3)K.O.%, (4)win%), each of which can be viewed by clicking on the respective chart type in a dropdown menu.
- the currently selected fighter's career bar is highlighted orange to distinguish it from the other top fighters.
