**PYTHON MANAGEMENT APPS**
```
python-management-apps/
├── student_report_card/
│   ├── report_card_app.py
│   └── students.json
├── bookstore_inventory/
│   ├── inventory.py
│   ├── bookstore_app.py
│   └── books.json
├── personal_budget/
│   ├── budget_utils.py
│   ├── budget_app.py
│   ├── expenses.json
└── README.md
```

---

```markdown
# Python Terminal Applications Collection

Welcome to the **Python Management App** project! This repository contains three independent, beginner-friendly Python terminal applications, each organized in its own folder.  
All projects use **simple file-based JSON storage** and require only the Python standard library.

---

## Contents

1. [Student Report Card App](#1-student-report-card-app)
2. [Bookstore Inventory System](#2-bookstore-inventory-system)
3. [Personal Budget Tracker](#3-personal-budget-tracker)

---

## 1. Student Report Card App

**Folder:** `student_report_card/`

A terminal-based app to manage student scores, averages, and grades.

- **Features**:
  - Add, view, and update students
  - Calculate and display average and grade per student
  - Data saved to `students.json`
  - Uses `Student` class

**How to run:**
```sh
cd python_management_app/student_report_card
python report_card_app.py
```

---

## 2. Bookstore Inventory System

**Folder:** `bookstore_inventory/`

A simple inventory manager for bookstore stock and pricing.

- **Features**:
  - Add, view, update, and search books
  - Data saved to `books.json`
  - Uses `Book` class and `inventory.py` for logic
  - Rounds prices up to two decimals using `math`

**How to run:**
```sh
cd task_4/bookstore_inventory
python bookstore_app.py
```
---

## 3. Personal Budget Tracker

**Folder:** `personal_budget/`

Track and categorize expenses, view spending summaries.

- **Features**:
  - Add and view transactions with date, category, amount
  - Group and summarize by category
  - Data saved to `expenses.json`
  - Uses `Transaction` class and `budget_utils.py` for calculations

**How to run:**
```sh
cd python_management_app/personal_budget
python budget_app.py
```
---

## Requirements

- Python 3.x  
  (No external dependencies; all code uses the Python standard library.)

---

## Contributing

1. Fork the repository or clone the project.
2. Work inside the relevant subfolder.
3. Follow Python best practices—keep code readable and commit often.
4. If adding features, use feature branches and merge when ready.


Happy coding!
```
