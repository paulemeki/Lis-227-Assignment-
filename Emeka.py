class LibraryManagement:
    def __init__(self):
        self.books = {}
        self.users = {}

    def add_book(self, book_id, title, author):
        self.books[book_id] = {'title': title, 'author': author, 'status': 'available'}

    def remove_book(self, book_id):
        if book_id in self.books:
            del self.books[book_id]
        else:
            print("Book not found!")

    def add_user(self, user_id, name):
        self.users[user_id] = {'name': name, 'borrowed_books': []}

    def remove_user(self, user_id):
        if user_id in self.users:
            del self.users[user_id]
        else:
            print("User not found!")

    def borrow_book(self, user_id, book_id):
        if book_id in self.books and self.books[book_id]['status'] == 'available':
            if user_id in self.users:
                self.users[user_id]['borrowed_books'].append(book_id)
                self.books[book_id]['status'] = 'borrowed'
                print("Book borrowed successfully!")
            else:
                print("User not found!")
        else:
            print("Book not available!")

    def return_book(self, user_id, book_id):
        if book_id in self.books and self.books[book_id]['status'] == 'borrowed':
            if user_id in self.users:
                if book_id in self.users[user_id]['borrowed_books']:
                    self.users[user_id]['borrowed_books'].remove(book_id)
                    self.books[book_id]['status'] = 'available'
                    print("Book returned successfully!")
                else:
                    print("Book not borrowed by this user!")
            else:
                print("User not found!")
        else:
            print("Book not borrowed or not found!")

    def display_borrowed_books(self, user_id):
        if user_id in self.users:
            borrowed_books = self.users[user_id]['borrowed_books']
            if borrowed_books:
                print("Borrowed Books:")
                for book_id in borrowed_books:
                    book = self.books[book_id]
                    print(f"Book ID: {book_id}, Title: {book['title']}, Author: {book['author']}")
            else:
                print("No books borrowed by this user.")
        else:
            print("User not found!")

def main():
    library = LibraryManagement()

    while True:
        print("\nLibrary Management System")
        print("1. Add User")
        print("2. Remove User")
        print("3. Add Book")
        print("4. Remove Book")
        print("5. Borrow Book")
        print("6. Return Book")
        print("7. Display Borrowed Books")
        print("8. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            user_id = input("Enter user ID: ")
            name = input("Enter user name: ")
            library.add_user(user_id, name)
            print("User added successfully!")
        elif choice == "2":
            user_id = input("Enter user ID to remove: ")
            library.remove_user(user_id)
        elif choice == "3":
            book_id = input("Enter book ID: ")
            title = input("Enter title: ")
            author = input("Enter author: ")
            library.add_book(book_id, title, author)
            print("Book added successfully!")
        elif choice == "4":
            book_id = input("Enter book ID to remove: ")
            library.remove_book(book_id)
        elif choice == "5":
            user_id = input("Enter user ID: ")
            book_id = input("Enter book ID: ")
            library.borrow_book(user_id, book_id)
        elif choice == "6":
            user_id = input("Enter user ID: ")
            book_id = input("Enter book ID: ")
            library.return_book(user_id, book_id)
        elif choice == "7":
            user_id = input("Enter user ID: ")
            library.display_borrowed_books(user_id)
        elif choice == "8":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
