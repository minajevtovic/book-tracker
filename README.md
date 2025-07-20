# 📚 book-tracker

This is a foundational version of a command-line Book Tracker built in Python.  
It helps you manage your reading list; books you've read, are currently reading, or plan to read.

The project is designed with clean object-oriented architecture and is built to be easily extended into a richer interface in the future (e.g. GUI, web, or Streamlit).

---

## 🚀 Features

- Add new books to your reading list
- Track book status: `to_read`, `reading`, or `read`
- Mark books as finished and rate them (0–5)
- List all books or filter only finished ones
- Remove books from the list
- Interactive menu system via `main.py`

---

## 🧱 Project Structure

```
book_tracker/
├── __init__.py
├── book.py              # Book class definition
├── reading_list.py      # ReadingList class to manage books
├── review.py            # (Optional) Placeholder for user reviews
├── main.py              # CLI logic - run this to use the app
├── unit_tests.py        # Basic unit tests (to be expanded)
├── reading_list.json    # Auto-generated file for persistence
```

---

## 💻 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/book-tracker.git
cd book-tracker
```

### 2. Install dependencies

```bash
poetry install
```

> Make sure you have [Poetry](https://python-poetry.org/docs/#installation) installed.

### 3. Run the app

```bash
poetry run python book_tracker/main.py
```

Follow the interactive menu to add, view, or remove books.

---

## 🧠 Stack Used

- Python 3.10+
- `typing.Literal` for strict value constraints
- `@property`, `__eq__`, and `__repr__` for clean OOP
- Poetry for dependency and environment management

---

## 🛣️ Roadmap

- [x] Add persistence (save/load JSON)
- [ ] Add reviews (`review.py`)
- [ ] Search and filter books by genre/language
- [ ] Add a Streamlit UI version
- [ ] Add unit tests with `pytest`
- [ ] Optional encryption for saved data
