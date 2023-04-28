# Python URL Shortener

This is a Python-based URL shortener application that allows you to shorten long URLs into shorter, more manageable links. It is a simple and lightweight solution that you can use to create your own URL shortening service.

## Features

- Shorten long URLs into short, customized links.
- Retrieve the original URL from a shortened link.
- Track the number of clicks on each shortened link.
- Simple and intuitive command-line interface.

## Prerequisites

Before running the application, make sure you have the following requirements met:

- Python 3 installed on your system.
- Python package dependencies installed. You can install them by running the following command:

```bash
pip install -r requirements.txt
```

## Usage

1. Clone this repository to your local machine:

```bash
git clone https://github.com/your-username/url-shortener.git
```

2. Navigate to the project directory:

```bash
cd url-shortener
```

3. Run the following command to start the application:

```bash
python url_shortener.py
```

4. The application will prompt you with options to either shorten a URL or retrieve the original URL from a shortened link. Follow the on-screen instructions to perform the desired action.

## Configuration

You can customize the behavior of the URL shortener application by modifying the `config.py` file. Here are the available configuration options:

- `BASE_URL`: The base URL for the shortened links. You can set this to your own domain or a preferred short link service.
- `DB_PATH`: The path to the SQLite database file that stores the shortened URLs and their corresponding statistics.

## Database

The application uses an SQLite database to store the shortened URLs and their associated information. The database file is created automatically when you run the application for the first time.

