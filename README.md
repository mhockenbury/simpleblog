simpleblog
===
An inventively named small web app to display blog articles and allow strangers to yell at each other.

Setup
===
Note: Developed on Python 3.8.3

- Run `./setup_and_run.sh` to install dependencies, generate and run migrations, and start the dev server
- Visit `localhost:8000/articles` in a browser

Potential Enhancements
===
- better usage of partials/advanced templating for more reusable frontend components
- a more customer presentation/bookmark friendly url scheme
- localize display of comment timestamps to client
- source secrets from environment rather than hardcoded (e.g. Django secret key)
