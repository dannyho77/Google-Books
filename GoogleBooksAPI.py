import json
import requests

class GoogleBooks:
  def __init__(self):
    self.list = []

  def search(self):
    title = input("Search for a book by title: ").strip()
    query = f'intitle:{title}'
    params = {"q": query}
    url = r'https://www.googleapis.com/books/v1/volumes'
    response = requests.get(url, params=params)

    response_dict = response.json()
    listcount = 0

    if response_dict['items']:
        for i in range(len(response_dict['items'])):
            if listcount == 5:
                break

            if 'publisher' not in response_dict['items'][i]['volumeInfo']:
                print(str(i+1) + ". " + "Title: " + response_dict['items'][i]['volumeInfo']['title'] + "; " + "Author: " + response_dict['items'][i]['volumeInfo']['authors'][0] + "; " + "Publisher: N/A")
            else:
                print(str(i+1) + ". " + "Title: " + response_dict['items'][i]['volumeInfo']['title'] + "; " + "Author: " + response_dict['items'][i]['volumeInfo']['authors'][0] + "; " + "Publisher: " + response_dict['items'][i]['volumeInfo']['publisher'])

            listcount += 1

        self.save_to_list(response_dict['items'])

    else:
        print('No available results -- try another search')

    if self.list:
        print('SAVED BOOKS')
        for i, book in enumerate(self.list):
            if 'publisher' not in book:
                print(str(i+1) + ". " + "Title: " + book['title'] + "; " + "Author: " + book['authors'][0] + "; " + "Publisher: N/A")
            else:
                print(str(i+1) + ". " + "Title: " + book['title'] + "; " + "Author: " + book['authors'][0] + "; " + "Publisher: " + book['publisher'])
    
    self.search()

    
  def save_to_list(self, searchlist):
    booknum = input("To save a book to your list, enter its item #: ").strip()

    if int(booknum) < 1 or int(booknum) > 5:
        print("Please re-enter a valid book item # from your recent search!")
        self.save_to_list(searchlist)
    elif searchlist[int(booknum)-1]['volumeInfo']:
        self.list.append(searchlist[int(booknum)-1]['volumeInfo'])


if __name__ == '__main__':
  booksearch = GoogleBooks()
  booksearch.search()