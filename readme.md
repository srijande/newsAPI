# NewsAPI
## Setup
​To setup the project, we need to install the following dependencies:

1. Python >=3
2. Redis >=6
3. Virtualenv 20.4.2

To install redis on mac run
```
brew install redis
```
Virtual environment is used to isolate the python dependencies from the system.
To create a virtual environment run
```
python3 -m venv env
```
To activate the virtual environment run
```
source env/bin/activate
```
To install the python dependencies run
```
pip install -r req.txt
```
## Running the project
​To run the project, we need to run the following commands:

we need to start the redis server by running the following command in a new terminal
```
redis-server
```
Then, we need to activate the virtual environment 
```
source env/bin/activate
```
Then, we need to run the following command to start the server at http://localhost:8000/
```
python manage.py runserver
```
To migrate the database run the following commands:
```
python manage.py makemigrations
python manage.py migrate
```
Using superuser we can login to the admin panel at http://localhost:8000/admin/

To create a superuser run: 
```
python manage.py createsuperuser 
```
## API Endpoints
​The following are the API endpoints: 
### GnewsAPI (https://gnews.io/)
Following are the endpoints for the GnewsAPI: this endpoint is used to fetch news from the GnewsAPI and store it in redis for 1 days. Response is cached with the following parameters: query, page, country, lang, sortby, max and category. And return the response from the cache if it exists when it is called again with the same parameters.
- /api/v1/gnews/search/ - POST - To search news
path parameters:
    - query - The search term
    - page - The page number
    - country - The country code (us, in, etc.)
    - lang - The language code (en, hi, etc.)
    - sortby - The sort order (relevance, date)
    - max - The maximum number of results to return
- /api/v1/gnews/headlines/ - POST - To fetch top headlines
    - category - The category to fetch headlines for (business, entertainment, general, health, science, sports, technology)
    - page - The page number
    - country - The country code (us, in, etc.)
    - lang - The language code (en, hi, etc.)
    - sortby - The sort order (relevance, date)
    - max - The maximum number of results to return
