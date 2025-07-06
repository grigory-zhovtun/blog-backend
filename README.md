# Blog Backend

A minimal Django-based blog engine. The project is used in educational tasks at [Devman](https://dvmn.org).

## Features

- CRUD models for posts and comments
- Like tracking for posts
- Interactive map on the contact page powered by Folium
- Django admin interface for content management

## Quickstart

1. Ensure you have Python 3 installed.
2. Clone the repository.
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. (Optional) Create an `.env` file next to `manage.py` to override default settings. See the configuration section below.
5. Apply migrations and start the development server:

   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

Visit <http://127.0.0.1:8000> in your browser to see the site.

## Configuration

Settings can be supplied via environment variables or an `.env` file. The defaults defined in `sensive_blog/settings.py` allow the project to run without customization. Available variables include:

- `DEBUG` — debug mode (`True`/`False`). Default: `True`.
- `SECRET_KEY` — Django secret key. Default: `REPLACE_ME`.
- `ALLOWED_HOSTS` — comma-separated hosts. Default: empty.
- `STATIC_URL` — URL prefix for static files. Default: `/static/`.
- `STATIC_ROOT` — directory for collected static files. Default: `None`.
- `MEDIA_URL` — URL prefix for uploaded media. Default: `/media/`.
- `MEDIA_ROOT` — directory for uploaded media. Default: `media`.

## Project Goals

This repository is for educational purposes as part of the [Devman](https://dvmn.org) curriculum. It demonstrates basic Django functionality and is not intended for production use.

## Contributing

Contributions are welcome. Please open an issue or submit a pull request if you have suggestions or improvements.
