# NASA-Space-App

Installation
1. clone repository: git clone https://github.com/Oleg-tech/NASA-Space-App.git
2. create vertual environment: python -m venv venv
3. install needed packages: pip install -r requirements.txt
4. go to directory with manage.py file: cd water_life
5. python manage.py makemigrations
6. python manage.py migrate 
7. python manage.py runserver - to run application
8. /fill-database - use this endpoint to fill DB with data from U.S. Fish and Wildlife Service(https://ecos.fws.gov/ecp/report/speciesListingsByState)
