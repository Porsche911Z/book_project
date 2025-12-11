from db.db import engine, Base
from db.crud import create_category, create_book

print("Создание таблиц...")
Base.metadata.create_all(bind=engine)
print("Таблицы созданы.")

from sqlalchemy.orm import Session
with Session(engine) as db:
    print("Добавление категорий...")
    cat1 = create_category(db, "Фантастика")
    cat2 = create_category(db, "Детективы")
    
    print("Добавление книг...")
    create_book(db, "Властелин колец", "Эпическая фантазия", 1000.0, "", cat1.id)
    create_book(db, "Гарри Поттер", "Магическая сага", 800.0, "", cat1.id)
    create_book(db, "Шерлок Холмс", "Классический детектив", 500.0, "", cat2.id)
    create_book(db, "Убийство в Восточном экспрессе", "Агата Кристи", 600.0, "", cat2.id)
    create_book(db, "Девушка с татуировкой дракона", "Триллер", 700.0, "", cat2.id)
print("Данные добавлены.")
