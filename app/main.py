from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from app.db.db import get_db, engine
from app.api.categories import router as categories_router
from app.api.books import router as books_router

app = FastAPI(title="Book API")

# Подключаем роутеры
app.include_router(categories_router)
app.include_router(books_router)

# Health check
@app.get("/health")
def health(db: Session = Depends(get_db)):
    return {"status": "healthy", "db_connection": "ok"}

# Опционально: Проверка подключения к БД при старте
@app.on_event("startup")
def startup():
    # Просто проверяем engine
    with engine.connect() as connection:
        pass  # Если нет ошибки, БД подключена
