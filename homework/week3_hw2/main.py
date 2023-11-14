from dto import Author, BookStore, BookItem

def main():

    bookitem_list = []
    bookitem_list.append(BookItem(name="Harry Potter", author="Joanne Rowling", year_published=1997))
    bookitem_list.append(BookItem(name="Load of the Rings", author="John Tolkien", year_published=1954))

    my_bookstore = BookStore(name="Auk Univ Store", book_shelve=bookitem_list)
    print("== My BookStore ==")
    print(my_bookstore.__dict__)

    try:
        my_author = Author(name="Joanne Rowling", author_id="JOAN-2223")        
    except Exception as ve:
        print("demonstrating that the Author name has to be valid")
    else:
        print("\n== My Author ==")
        print(my_author.__dict__)

if __name__ == "__main__":
    main()