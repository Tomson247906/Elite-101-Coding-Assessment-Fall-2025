from library_books import library_books
from datetime import datetime, timedelta



# -------- Level 1 --------
# TODO: Create a function to view all books that are currently available
# Output should include book ID, title, and author


#This allows the user to view all available books in the library
def view_available_books():
    print("Available Books:")
    for book in library_books:
        if book['available']:
            print(f"ID: {book['id']}, Title: {book['title']}, Author: {book['author']}")


# -------- Level 2 --------
# TODO: Create a function to search books by author OR genre
# Search should be case-insensitive
# Return a list of matching books

#allows the user to search for books by author or genre and to see if its id, title, author, genre and if its available
def search_by_author_or_genre(search_term):
    search_term = search_term.strip().lower()
    matching_books = []
    for book in library_books:
        author = book.get('author','').lower()
        genre = book.get('genre','').lower()
        if search_term in author or search_term in genre:
            matching_books.append(book)
    return matching_books

# -------- Level 3 --------
# TODO: Create a function to checkout a book by ID
# If the book is available:
#   - Mark it unavailable
#   - Set the due_date to 2 weeks from today
#   - Increment the checkouts counter
# If it is not available:
#   - Print a message saying it's already checked out

#This function allows the user to check out a book by its ID and lets the
def check_out_book(book_id):
    for book in library_books:
        if book["id"] == book_id:
            if book['available']:
                book["available"] = False
                book["due_date"] = datetime.now() + timedelta(weeks=2)
                book['checkouts'] = book.get('checkouts', 0) + 1
                print(f"You have successfully checked out '{book['title']}'. It is due on {book['due_date'].strftime('%Y-%m-%d')}.")
            else:
                print(f"Sorry, '{book['title']}' is already checked out.")
            return
    print("Book ID not found.")

# -------- Level 4 --------
# TODO: Create a function to return a book by ID
# Set its availability to True and clear the due_date

# TODO: Create a function to list all overdue books
# A book is overdue if its due_date is before today AND it is still checked out


# -------- Level 5 --------
# TODO: Convert your data into a Book class with methods like checkout() and return_book()
# TODO: Add a simple menu that allows the user to choose different options like view, search, checkout, return, etc.

# This function provides a simple text-based menu for the library system
#def guide():
    while True:
        print("\n welcome to the library inventory")
        print("1: view available books")
        print("2: search by genre or author")
        print("3: check out")
        print("4: check in")
        print("5: close program")

        choice = input("pick an opition(1-5): ")

        if choice == "1":
            print("viewing books")
            view_available_books()
        elif choice == "2":
            search = input("searching by genre or author")
            
            
        elif choice == "3":
            print("working progress")
        elif choice == "4":
            print("working progress")
        elif choice == "5":
            print("now closing")
            break
        else:
            print("Invalid option. Please try again.")



# -------- Optional Advanced Features --------
# You can implement these to move into Tier 4:
# - Add a new book (via input) to the catalog
# - Sort and display the top 3 most checked-out books
# - Partial title/author search
# - Save/load catalog to file (CSV or JSON)
# - Anything else you want to build on top of the system!

if __name__ == "__main__":
    # You can use this space to test your functions
    pass


print(check_out_book("B1"))
#print(search_by_author_or_genre("Rick Riordan"))
#view_available_books()
#guide()