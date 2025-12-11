from db.db import engine
from db.crud import read_all_categories, read_all_books
from sqlalchemy.orm import Session

with Session(engine) as db:
    categories = read_all_categories(db)
    print("Категории:")
    for cat in categories:
        print(f"ID: {cat.id}, Title: {cat.title}")
    
    books = read_all_books(db)
    print("\nКниги:")
    for book in books:
        print(f"ID: {book.id}, Title: {book.title}, Desc: {book.description}, Price: {book.price}, Cat ID: {book.category_id}")
