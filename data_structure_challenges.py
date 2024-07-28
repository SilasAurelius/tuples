#Task 1: Update the system by adding new books and ensuring no duplicates.

def add_book(library, new_book):
    # Check if the new_book is already in the library
    if new_book in library:
        print(f"The book '{new_book[0]}' by {new_book[1]} is already in the library.")
    else:
        library.append(new_book)
        print(f"The book '{new_book[0]}' by {new_book[1]} has been added to the library.")

library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

# Example Usage
new_book_1 = ("1984", "George Orwell")
add_book(library, new_book_1)

new_book_2 = ("Brave New World", "Aldous Huxley")  
# Duplicate book
add_book(library, new_book_2)

print("\nCurrent Library Collection:")
for book in library:
    print(f"Title: {book[0]}, Author: {book[1]}")
