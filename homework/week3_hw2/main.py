from dto import Author, BookStore, BookItem

def val_author(name:str, author_id:str):
    try:
        my_author = Author(name=name, author_id=author_id)        
    except Exception as ve:
        print("demonstrating that the Author name has to be valid")
    else:
        print("\n== My Author ==")
        print(my_author.__dict__)
        return my_author

def main():

    bookitem_list = []

    bookitem_list.append(BookItem(name="Harry Potter", author=val_author("Joanne Rowling", "JOAN-2223"), year_published=1997))
    bookitem_list.append(BookItem(name="Load of the Rings", author=val_author("John Tolkien", "JOTO-1954"), year_published=1954))

    my_bookstore = BookStore(name="Auk Univ Store", book_shelve=bookitem_list)
    print("\n== My BookStore ==")
    print(my_bookstore.__dict__)

if __name__ == "__main__":
    main()