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

        if response_dict['items']:
            self.show_search_results(response_dict['items'])

            self.save_to_list(response_dict['items'])
        else:
            print('No available results -- try another search')

        if self.list:
            self.show_saved_list(self.list)
        
        self.search()


    def show_search_results(self, query_result):
        listcount = 0

        for i in range(len(query_result)):
            if listcount == 5:
                break

            if 'publisher' not in query_result[i]['volumeInfo']:
                print(str(i+1) + ". " + "Title: " + query_result[i]['volumeInfo']['title'] + "; " + "Author: " + query_result[i]['volumeInfo']['authors'][0] + "; " + "Publisher: N/A")
            else:
                print(str(i+1) + ". " + "Title: " + query_result[i]['volumeInfo']['title'] + "; " + "Author: " + query_result[i]['volumeInfo']['authors'][0] + "; " + "Publisher: " + query_result[i]['volumeInfo']['publisher'])

            listcount += 1

    
    def save_to_list(self, searchlist):
        booknum = input("To save a book to your Reading List, enter its item #: ").strip()

        if int(booknum) < 1 or int(booknum) > 5:
            print("Please re-enter a valid book item # from your recent search!")
            self.save_to_list(searchlist)
        elif searchlist[int(booknum)-1]['volumeInfo']:
            self.list.append(searchlist[int(booknum)-1]['volumeInfo'])


    def show_saved_list(self, list):
        print('=== YOUR READING LIST ===')
        for i, book in enumerate(self.list):
            if 'publisher' not in book:
                print(str(i+1) + ". " + "Title: " + book['title'] + "; " + "Author: " + book['authors'][0] + "; " + "Publisher: N/A")
            else:
                print(str(i+1) + ". " + "Title: " + book['title'] + "; " + "Author: " + book['authors'][0] + "; " + "Publisher: " + book['publisher'])


if __name__ == '__main__':
    booksearch = GoogleBooks()
    booksearch.search()