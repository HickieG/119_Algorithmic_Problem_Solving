from catalog_data import BOOKS, validate_book_ids


def scan_lookup(records, book_id):
    for book in records:
        if book["id"] == book_id:
            return book
    return None


def build_index(records):
    index = {}

    for book in records:
        index[book["id"]] = book

    return index


def indexed_lookup(index, book_id):
    return index.get(book_id)


def display_book(book):
    if book is None:
        print("Book not found.")
    else:
        print(
            f"ID: {book['id']}, "
            f"Title: {book['title']}, "
            f"Author: {book['author']}"
        )


def main():
    validate_book_ids(BOOKS)

    index = build_index(BOOKS)

    print("Scan Lookup for B1:")
    display_book(scan_lookup(BOOKS, "B1"))

    print("\nIndexed Lookup for B4:")
    display_book(indexed_lookup(index, "B4"))

    print("\nLookup for B99:")
    display_book(scan_lookup(BOOKS, "B99"))
    
    print("\nIndexed Lookup for empty input:")
    display_book(indexed_lookup(index, ""))


if __name__ == "__main__":
    main()