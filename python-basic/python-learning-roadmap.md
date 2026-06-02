# Python Learning Roadmap: Beginner To Pro

This roadmap is based on the current files in this folder. You have already started well: variables, input, conditionals, loops, functions, lists, dictionaries, strings, files, JSON, and a password generator project are already present.

## Current Progress Summary

| Area | Current file(s) | Status | Notes |
|---|---|---:|---|
| Variables, print, input | `day1.py` | Done | You can now create values and display them. |
| Type conversion and conditionals | `day2.py` | Done | You used `int()`, `if`, `elif`, and `else`. |
| Loops | `day3.py`, `day3-practice.py`, `day4.py` | Done | You practiced `for`, `while`, `break`, `continue`, ranges, and patterns. |
| Functions | `day5.py` | Started | Calculator is a good first function-based project. |
| Lists | `day6.py` | Started | Todo app is a good list project. Add edit/delete/search next. |
| Dictionaries | `day7.py` | Started | You can store key-value data. Next: nested dictionaries and lists of dictionaries. |
| Strings | `day8.py` | Started | Add slicing, validation, formatting, and common string methods. |
| File handling and errors | `day9.py` | Started | You used `with open()` and `try/except`. Improve path handling and specific exceptions. |
| JSON data | `fake_database.py`, `users.json` | Started | You are saving and loading structured data. Good early database thinking. |
| Mini project | `day9_password_gen.py` | Good progress | Nice use of `secrets`, functions, type hints, and `__main__`. |

## Full Roadmap

| Stage | Topic | What to complete | Practice file/project idea | Done when you can... |
|---:|---|---|---|---|
| 1 | Setup and running Python | Install Python, run files, use terminal, understand `.py` files | `day0_setup_notes.md` | Run any Python file from terminal and explain what happened. |
| 2 | Variables and data types | `str`, `int`, `float`, `bool`, `None`, `type()` | Improve `day1.py` | Store user data and print formatted output. |
| 3 | Input and output | `input()`, `print()`, f-strings, basic formatting | Profile card generator | Ask for user info and display a clean result. |
| 4 | Operators | Arithmetic, comparison, logical operators | BMI calculator | Correctly calculate and compare values. |
| 5 | Conditionals | `if`, `elif`, `else`, nested conditions | Improve `day2.py` | Build decision-based programs without confusion. |
| 6 | Loops | `for`, `while`, `range`, `break`, `continue`, loop `else` | Improve `day3.py` and `day4.py` | Solve counting, sum, pattern, and search problems. |
| 7 | Strings | Indexing, slicing, methods, validation | Username/password validator | Clean, validate, and transform text. |
| 8 | Lists and tuples | Indexing, append, remove, sort, slicing, tuple basics | Upgrade `day6.py` todo app | Add, view, update, delete, and sort items. |
| 9 | Dictionaries and sets | Key-value data, `.items()`, nested data, unique values | Contact book | Store real records and look them up by key. |
| 10 | Functions | Parameters, return values, defaults, scope, small pure functions | Refactor calculator in `day5.py` | Break programs into reusable functions. |
| 11 | Error handling | `try`, `except`, `else`, `finally`, specific exceptions | Safe calculator | Prevent crashes from bad input. |
| 12 | Files | Read, write, append, file paths, context managers | Notes app | Save and load text data reliably. |
| 13 | JSON | `json.load`, `json.dump`, list of dictionaries | Improve `fake_database.py` | Build a small file-based database. |
| 14 | Modules and imports | Standard library, custom modules, import styles | Split password generator into modules | Organize code across multiple files. |
| 15 | Virtual environments and packages | `venv`, `pip`, `requirements.txt` | Create a project environment | Install and freeze project dependencies. |
| 16 | Debugging | Tracebacks, print debugging, debugger basics | Debug old practice files | Read errors and find the broken line calmly. |
| 17 | Code style | PEP 8, naming, formatting, comments, `ruff` or `black` | Format all practice files | Write clean code that is easy to read later. |
| 18 | Testing | `assert`, `unittest` or `pytest`, test cases | Test calculator and password generator | Prove functions work without manually checking every time. |
| 19 | Object-oriented programming | Classes, objects, methods, `__init__`, inheritance basics | Bank account app | Model real-world things with classes. |
| 20 | Dataclasses and typing | `dataclass`, type hints, `list[str]`, `dict`, `Optional` | Typed contact book | Make data structures clearer and safer. |
| 21 | Comprehensions | List, dict, and set comprehensions | Data filtering exercises | Transform collections in concise Pythonic ways. |
| 22 | Iterators and generators | `iter`, `next`, `yield`, lazy processing | Large file reader | Process data without loading everything at once. |
| 23 | Advanced functions | `lambda`, `map`, `filter`, `sorted(key=...)`, closures | Scoreboard sorter | Pass functions as values and sort complex data. |
| 24 | Dates and time | `datetime`, timestamps, formatting dates | Habit tracker | Store and display dates correctly. |
| 25 | Command-line apps | `argparse`, menus, command arguments | CLI todo app | Build terminal tools with commands/options. |
| 26 | APIs and HTTP | `requests`, status codes, JSON APIs | Weather or currency CLI | Fetch data from the internet and handle responses. |
| 27 | Web scraping basics | HTML, `BeautifulSoup`, polite scraping | Simple news/title scraper | Extract public page data responsibly. |
| 28 | Databases | SQLite, tables, CRUD, SQL basics | SQLite user manager | Store data in a real database instead of JSON only. |
| 29 | Web development | Flask or FastAPI, routes, templates/API responses | Todo web app | Build a small backend users can interact with. |
| 30 | Automation | OS paths, folders, CSV, Excel, email/files | File organizer | Automate boring local tasks. |
| 31 | Data work | CSV, pandas, cleaning, grouping, charts | Expense analyzer | Load, analyze, and summarize tabular data. |
| 32 | Async basics | `async`, `await`, concurrent requests | Multi-URL checker | Run waiting tasks efficiently. |
| 33 | Security basics | Secrets, hashing, env vars, input safety | Secure login demo | Avoid storing passwords or secrets carelessly. |
| 34 | Packaging | Project layout, `pyproject.toml`, modules, README | Package one CLI app | Turn code into an installable project. |
| 35 | Git and collaboration | Branches, commits, pull requests, `.gitignore` | Version your projects | Track changes and explain your work. |
| 36 | Deployment | Hosting basics, environment variables, logs | Deploy FastAPI/Flask app | Put a Python app online. |
| 37 | Professional project | Combine files, tests, database, API, docs | Personal finance tracker or learning tracker | Build a complete app from scratch and maintain it. |
| 38 | Interview/problem solving | Lists, strings, dictionaries, recursion, complexity | 100 small problems | Solve common coding problems with clear reasoning. |
| 39 | Specialization path | Choose backend, data, automation, AI, or DevOps | Pick 3 portfolio projects | Go deeper in the Python direction you care about. |
| 40 | Pro habits | Reading docs, refactoring, profiling, logging, architecture | Improve old projects monthly | Make code reliable, readable, tested, and useful. |

## Recommended Next 20 Practice Tasks

| Order | Task | Main topic | Suggested file |
|---:|---|---|---|
| 1 | Clean up `day5.py` calculator and add repeat menu | Functions, loops | `day10_calculator_v2.py` |
| 2 | Add invalid input handling to todo app | Errors, lists | `day11_todo_v2.py` |
| 3 | Add delete task and mark complete features | Lists, dictionaries | `day12_todo_v3.py` |
| 4 | Build a contact book using list of dictionaries | Dictionaries | `day13_contact_book.py` |
| 5 | Save contact book to JSON | Files, JSON | `day14_contact_json.py` |
| 6 | Add search by name/phone | Loops, strings | `day15_contact_search.py` |
| 7 | Create a login/register demo with JSON | JSON, validation | `day16_login_system.py` |
| 8 | Hash passwords with `hashlib` | Security basics | `day17_password_hashing.py` |
| 9 | Write tests for password generator | Testing | `test_password_gen.py` |
| 10 | Split password generator into module + CLI file | Modules | `password_generator/` |
| 11 | Build a number guessing game | Loops, random | `day18_guess_game.py` |
| 12 | Build a quiz app with score tracking | Lists, dicts | `day19_quiz_app.py` |
| 13 | Build an expense tracker using JSON | Files, data modeling | `day20_expense_tracker.py` |
| 14 | Add monthly summary to expense tracker | Dates, aggregation | `day21_expense_summary.py` |
| 15 | Convert expense tracker to SQLite | Database | `day22_expense_sqlite.py` |
| 16 | Learn classes with a bank account app | OOP | `day23_bank_account.py` |
| 17 | Refactor expense tracker using classes | OOP, design | `day24_expense_oop.py` |
| 18 | Build a command-line app with `argparse` | CLI | `day25_cli_notes.py` |
| 19 | Fetch API data with `requests` | APIs | `day26_api_practice.py` |
| 20 | Create a small FastAPI or Flask todo API | Web backend | `day27_todo_api/` |

## Weekly Study Plan

| Week | Focus | Build | Review |
|---:|---|---|---|
| 1 | Strings, lists, dictionaries | Contact book | Old `day6.py`, `day7.py`, `day8.py` |
| 2 | Functions and error handling | Calculator v2 and todo v2 | `day5.py`, `day6.py`, `day9.py` |
| 3 | Files and JSON | Login/register system | `fake_database.py` |
| 4 | Modules and tests | Tested password generator package | `day9_password_gen.py` |
| 5 | OOP | Bank account app | Refactor one old project |
| 6 | SQLite | Expense tracker database | JSON vs SQLite differences |
| 7 | APIs and CLI | Weather/API terminal app | Error handling and clean output |
| 8 | Web backend | Todo API | Routes, request/response, database |

## Study Rule

Do not only watch tutorials. For every topic, write one small program, then improve it twice:

| Attempt | Goal |
|---|---|
| Version 1 | Make it work. |
| Version 2 | Handle bad input and edge cases. |
| Version 3 | Refactor into functions/classes and add tests. |
