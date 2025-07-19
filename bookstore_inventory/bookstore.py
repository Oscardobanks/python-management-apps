from inventory import Book, save_books, load_books, search_books


def add_book(books):
    title = input("Title: ")
    author = input("Author: ")
    try:
        price = float(input("Price: "))
        stock = int(input("Stock: "))
    except:
        print("Invalid price or stock.")
        return
    books.append(Book(title, author, price, stock))
    print("Book added.")


def view_books(books):
    if not books:
        print("No books in inventory.")
    for b in books:
        print(f"{b.title} by {b.author} | ₦{b.price:.2f} | Stock: {b.stock}")


def update_stock(books):
    title = input("Enter book title to update: ")
    for b in books:
        if b.title.lower() == title.lower():
            try:
                new_stock = int(input(f"New stock (old: {b.stock}): "))
                b.stock = new_stock
                print("Stock updated.")
            except:
                print("Invalid input.")
            return
    print("Book not found.")


def search_inventory(books):
    term = input("Enter search term: ")
    results = search_books(books, term)
    if not results:
        print("No matching books found.")
    for b in results:
        print(f"{b.title} by {b.author} | ₦{b.price:.2f} | Stock: {b.stock}")


def main():
    books = load_books()
    while True:
        print(
            "\n1. Add book\n2. View books\n3. Update stock\n4. Search books\n5. Save & Exit")
        op = input("Choose: ")
        if op == "1":
            add_book(books)
        elif op == "2":
            view_books(books)
        elif op == "3":
            update_stock(books)
        elif op == "4":
            search_inventory(books)
        elif op == "5":
            save_books(books)
            print("Saved. Bye!")
            break
        else:
            print("Invalid.")


if __name__ == "__main__":
    main()
