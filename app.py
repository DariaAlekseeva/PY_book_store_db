from utils import database

USER_CHOICE = """
Enter:
- 'a' to add a new book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit

Your choice: """


def menu():
    database.create_book_table()

    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input == 'a':
            prompt_add_book()
        elif user_input == 'l':
            list_books()
        elif user_input == 'r':
            prompt_read_book()
        elif user_input == 'd':
            prompt_delete_book()
        else:
            print('Unknown command. Please try again.')

        user_input = input(USER_CHOICE)

    # if user chooses q
    save = input('Would you like to save your book list? (y/n): ')
    if save == 'y':
        database.save_list()
        print('Your book list has been saved!')


# adds new book
def prompt_add_book():
    name = input('Enter book name: ')
    author = input('Enter author name: ')
    database.add_book(name, author)


# lists all books in library
def list_books():
    books = database.get_all_books()
    for book in books:
        read = 'YES' if book['read'] else 'NO'
        print(f'{book["name"]} by {book["author"]}, read: {read}.')


# marks book as read
def prompt_read_book():
    name = input('Enter book name you just finished reading: ')

    database.mark_book_as_read(name)


# deletes book from a list
def prompt_delete_book():
    name = input('Enter book name you wish to delete: ')

    database.delete_book(name)


# save book list into a file
def save_list():
    with open('book_list.txt', 'w') as file:
        file.write(str(books))


# load books from file
def load_book_list():
    with open('book_list.txt', 'r') as file:
        books = file.read()
        return books


menu()

