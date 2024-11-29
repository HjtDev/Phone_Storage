# Phone Storage Project

## Overview

The Phone Storage project is an educational and simple application designed to simulate a phone storage system. It allows users to manage a collection of phones, providing functionalities to add, remove, and view phone details. This project serves as a practical example for learning Django and web development concepts, including database management, user interface design, and AJAX functionality.

## Features

- **Live Search**: Quickly find phones in the storage using a live search feature.
- **Export as JSON**: Easily export phone data in JSON format for further processing or sharing.
- **Export as Excel**: Generate and download an Excel file containing the phone data.
- **AJAX-Based Add and Remove**: Add or remove phones dynamically without refreshing the page using AJAX.
- **Optimized Views and Queries**: Efficiently handle data retrieval with optimized database queries.
- **Form Validations**: Ensure data integrity with comprehensive form validations for adding or editing phones.
- **Reports Page**: View detailed reports of available phones organized by brand nationality.
- **Functional Admin Page**: Manage the application through a user-friendly admin interface powered by [Django Jazzmin](https://github.com/fabiocaccamo/django-jazzmin), enhancing the overall look and feel.

## Installation and Setup

### Prerequisites

- Python 3.x
- PostgreSQL (or another database of your choice)

### Instructions

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/HjtDev/Phone_Storage.git
    cd Phone_Storage
    ```

2. **Create a Virtual Environment**:
    ```bash
    python -m venv venv
    ```

3. **Activate the Virtual Environment**:
    - On Windows:
        ```bash
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

4. **Install Requirements**:
    ```bash
    pip install -r requirements.txt
    ```

5. **Set Up PostgreSQL Database**:
    - Create a new PostgreSQL database (e.g., `phone_storage`).
    - Update your `settings.py` file in the Django project to configure the database connection:
        ```python
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': 'phone_storage',
                'USER': 'your_username',
                'PASSWORD': 'your_password',
                'HOST': 'localhost',
                'PORT': '',
            }
        }
        ```

6. **Run Migrations**:
    ```bash
    python manage.py migrate
    ```

7. **(Optional) Load Initial Data**:
    If you want some initial data to work with, you can use the provided `datadump.json` file:
    ```bash
    python manage.py loaddata datadump.json
    ```

8. **Run the Development Server**:
    ```bash
    python manage.py runserver
    ```

9. **Access the Application**:
    Open your web browser and go to `http://127.0.0.1:8000/` to access the Phone Storage application.
