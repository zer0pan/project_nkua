# Data Management Application

A desktop application built with Python 3 and PyQt5 for managing, searching, and storing personal data records.

## Features

* **Data Entry**: Add new records (Name, Surname, City, Number). The system automatically assigns a unique 6-digit code to each person.
* **Search Functionality**: Retrieve saved records instantly using their unique 6-digit code.
* **Persistent Storage**: Save newly added data and their corresponding unique codes to local text files (`save.txt` and `code_set.txt`).
* **Graphical User Interface**: Simple and practical interface powered by PyQt5.

## Project Structure

* `main.py`: The entry point of the application. It initializes the GUI and handles user interactions.
* `person.py`: Contains the `Person` class, which models the data entities.
* `file_handler1.py`: Manages all Input/Output (I/O) operations, including reading from and writing to the local `.txt` files.


## Prerequisites

* **Python**: Version 3.x
* **PyQt5**: Python bindings for the Qt application framework

## Installation and Usage

### 1. System Dependencies (Linux Only)
If you are running a Linux distribution that uses the **Wayland** display server (e.g., modern Ubuntu/Debian), you must install the following system package to prevent Qt platform plugin errors (`xcb` not found):

```bash
sudo apt-get update
sudo apt-get install qtwayland5 
pip install PyQt5
```

### 2. For Windows or Mac 

```bash
pip install PyQt5
```
### Usage

To start the application, open your terminal, navigate to the root directory of the project 
and run the main script:

For Linux/Mac:

```bash
python3 main.py
```
For Windows:

```bash
python main.py
```
### Basic Workflow

* **Fill in the "Name", "Surname", "City", and "Number" fields.**

* **Click add to stage the data in the program's memory.**

* **Click save to write the staged data to save.txt.**

* **To find a record, enter its unique 6-digit code in the "Data Search" field and click search.**

* **Click clear to empty all input fields**