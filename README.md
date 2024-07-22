# URL Shortener

## Technologies and Frameworks

1. **Flask**: A lightweight WSGI web application framework in Python. Used to build the web application, handle routing, and manage HTTP requests and responses.
2. **SQLite**: A lightweight, disk-based database used to store the original and shortened URLs. It is integrated into the application using Python's `sqlite3` module.
3. **Bootstrap 4**: A popular CSS framework used for styling the application. It provides responsive design and ready-to-use components such as forms, buttons, and tables.
4. **HTML5**: Used for the structure of the web pages. Includes forms for user input and tables for displaying shortened URLs.
5. **JavaScript/jQuery**: Included for additional functionality and interactivity, although not heavily utilized in this particular implementation.

## Algorithms and Functionality

1. **URL Shortening Algorithm**: 
   - **Short ID Generation**: Uses a custom algorithm to generate unique short IDs. It combines uppercase and lowercase letters with digits to create a random string of a specified length (default 6 characters).
   - **Database Storage**: The generated short ID and the original URL are stored in an SQLite database. Each short ID is unique due to database constraints.

2. **Database Schema**:
   - A single table named `urls` with columns:
     - `id`: An auto-incrementing primary key.
     - `original_url`: The original URL provided by the user.
     - `short_id`: The generated short ID that maps to the original URL.

3. **Routing**:
   - **Home Route (`/`)**: Handles both GET and POST requests. On POST, it shortens the URL and displays the result. On GET, it displays a form for URL input and a table of previously shortened URLs.
   - **Redirection Route (`/<short_id>`)**: Redirects users to the original URL based on the short ID. If the short ID does not exist, it displays an error message and redirects to the home page.

## Key Features

- **URL Shortening**: Users can input a long URL, which is then shortened and stored in the database. The shortened URL can be shared and accessed directly.
- **User Feedback**: Uses Flask's `flash` messaging system to provide feedback to the user about the success or failure of their URL shortening request.
- **Responsive Design**: Thanks to Bootstrap, the application is mobile-friendly and adjusts to different screen sizes.

## Setup and Running

1. **Environment Setup**:
   - Create a virtual environment and activate it.
   - Install required packages using `pip install Flask`.

2. **Database Initialization**:
   - The `init_db` function initializes the SQLite database and creates the necessary table if it does not exist.

3. **Running the Application**:
   - Start the Flask development server using `python app.py` or the appropriate command for your environment.
