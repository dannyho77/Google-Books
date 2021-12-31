import requests
import re

class GoogleBooks:
    def __init__(self):
        self.list = []
        self.listcount = 0

    def search(self):
        title = input("Search for a book by title: ").strip()
        # title = re.sub(r'[^\w]', ' ', title)
        if not title:
            print("Your search input cannot be empty. Please conduct a valid search that includes alphanumeric characters.")
            self.search()
        
        query = f'intitle:{title}'
        params = {"q": query}
        url = r'https://www.googleapis.com/books/v1/volumes'
        response = requests.get(url, params=params)

        response_dict = response.json()

        if 'items' not in response_dict:
            print("No available results -- try another search")
        elif response_dict['items']:
            self.show_search_results(response_dict['items'])
            self.search_or_save(response_dict['items'])

        if self.list:
            self.show_saved_list()
        
        self.search()


    def show_search_results(self, query_result):
        self.listcount = 0
        
        for i in range(len(query_result)):
            if self.listcount == 5:
                break

            if 'publisher' not in query_result[i]['volumeInfo'] and 'authors' not in query_result[i]['volumeInfo']:
                print(str(i+1) + ". " + "Title: " + query_result[i]['volumeInfo']['title'] + "; " + "Author: N/A" + "; " + "Publisher: N/A")
            elif 'publisher' not in query_result[i]['volumeInfo']:
                print(str(i+1) + ". " + "Title: " + query_result[i]['volumeInfo']['title'] + "; " + "Author: " + query_result[i]['volumeInfo']['authors'][0] + "; " + "Publisher: N/A")
            elif 'authors' not in query_result[i]['volumeInfo']:
                print(str(i+1) + ". " + "Title: " + query_result[i]['volumeInfo']['title'] + "; " + "Author: N/A" + "; " + "Publisher: " + query_result[i]['volumeInfo']['publisher'])
            else:
                print(str(i+1) + ". " + "Title: " + query_result[i]['volumeInfo']['title'] + "; " + "Author: " + query_result[i]['volumeInfo']['authors'][0] + "; " + "Publisher: " + query_result[i]['volumeInfo']['publisher'])

            self.listcount += 1

    
    def search_or_save(self, query_result):
        choice = input("If you would like to start a new search, please enter '1'. If you would like to save a book from this search result, please enter '2'. ").strip()
        if choice not in ['1', '2']:
            print("Please enter a valid input (i.e. '1' or '2').")
            self.search_or_save(query_result)
        elif choice == '1':
            self.search()
        elif choice == '2':
            self.save_to_list(query_result)

    def save_to_list(self, searchlist):
        booknum = input("To save a book to your Reading List, enter its item #: ").strip()

        if int(booknum) < 1 or int(booknum) > self.listcount:
            print("Please re-enter a valid book item # from your recent search!")
            self.save_to_list(searchlist)
        elif searchlist[int(booknum)-1]['volumeInfo']:
            self.list.append(searchlist[int(booknum)-1]['volumeInfo'])


    def show_saved_list(self):
        print('=== YOUR READING LIST ===')
        for i, book in enumerate(self.list):
            if 'publisher' not in book and 'authors' not in book:
                print(str(i+1) + ". " + "Title: " + book['title'] + "; " + "Author: N/A" + "; " + "Publisher: N/A")
            elif 'publisher' not in book:
                print(str(i+1) + ". " + "Title: " + book['title'] + "; " + "Author: " + book['authors'][0] + "; " + "Publisher: N/A")
            elif 'authors' not in book:
                print(str(i+1) + ". " + "Title: " + book['title'] + "; " + "Author: N/A" + "; " + "Publisher: " + book['publisher'])
            else:
                print(str(i+1) + ". " + "Title: " + book['title'] + "; " + "Author: " + book['authors'][0] + "; " + "Publisher: " + book['publisher'])


if __name__ == '__main__':
    booksearch = GoogleBooks()
    booksearch.search()