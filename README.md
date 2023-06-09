# Django GIS Project

This Django project demonstrates the usage of Django GIS features and provides API endpoints for managing and querying geospatial data.

## Features

- CRUD operations for managing places with geospatial information (name, description, and coordinates)
- API endpoint to find the closest place based on given latitude and longitude coordinates
- Integration with Swagger for API documentation and testing
- Presentation: https://www.loom.com/share/77893d9fc3aa4b74b8de3419084ff13f

## Installation()

1. Clone the repository:

   ```
   git clone https://github.com/oksana-feshchenko/geo-app.git
   ```
2. If you are using PyCharm - it may propose you to automatically create venv for your project and install requirements in it, but if not:
```
python -m venv venv
venv\Scripts\activate (on Windows)
source venv/bin/activate (on macOS)
```
3. Install the required dependencies:

```
pip install -r requirements.txt
```

4. Configure settings in .env file
```
DB_NAME=DB_NAME
DB_USER=DB_USER
DB_PASSWORD=DB_PASSWORD
DB_HOST=DB_HOST
DB_PORT=DB_PORT
DJANGO_SECRET_KEY=DJANGO_SECRET_KEY
```

5. Run database migrations:

```
python manage.py migrate
```


## Usage
Start the development server:

```
python manage.py runserver
```

# Run with docker:
1. Install docker.
2. Run this commands.
```
docker-compose build
docker compose up
```
Open your browser and navigate to http://localhost:8000/ to verify that everything is working properly.

### API documentation
1. Access the API documentation:

Open your web browser and navigate to http://localhost:8000/swagger-ui/. You will see the Swagger UI interface with the available API endpoints and their documentation.

2. Explore and interact with the API endpoints:

Use the provided endpoints for CRUD operations on places.

Use the "Closest Place" endpoint to find the closest place based on given latitude and longitude coordinates.

# To run locally(additional info):

## Prerequisites

- Python 3.x
- Django 3.x
- Django REST Framework
- GeoDjango
- PostgreSQL (with PostGIS extension)

### Installation of dependencies
You could use official documentation https://docs.djangoproject.com/en/4.2/ref/contrib/gis/install/ for GeoDjango installation.
### More detailed information for Windows users:

#### Step 1.: Install OSGeo4W
Download the OSGeo4W installer from the official website.
Run the installer and select "Express Web-GIS Install" option.
In the "Select Packages" list, make sure "GDAL" is selected. You can uncheck any other packages that are not required by GeoDjango.
Proceed with the installation, accepting the license agreements when prompted.
After the installation is complete, you can exit the installer.
#### Step 2: Modify Windows Environment
In order to use GeoDjango, you need to add the OSGeo4W directories to your Windows system Path and create two environment variables: GDAL_DATA and PROJ_LIB.

Open a command prompt (cmd.exe) as an administrator.
Execute the following commands to set up the environment variables:
```
set OSGEO4W_ROOT=C:\OSGeo4W
set GDAL_DATA=%OSGEO4W_ROOT%\apps\gdal\share\gdal
set PROJ_LIB=%OSGEO4W_ROOT%\share\proj
set PATH=%PATH%;%OSGEO4W_ROOT%\bin
reg ADD "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Environment" /v Path /t REG_EXPAND_SZ /f /d "%PATH%"
reg ADD "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Environment" /v GDAL_DATA /t REG_EXPAND_SZ /f /d "%GDAL_DATA%"
reg ADD "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Environment" /v PROJ_LIB /t REG_EXPAND_SZ /f /d "%PROJ_LIB%"
```
Restart your computer for the new environment variables to take effect.
#### Step 3: Modify Django's libgdal.py File
To ensure Django uses the correct GDAL library binding file, you need to modify the libgdal.py file in your virtual environment.

Locate the libgdal.py file in your virtual environment. The path should be similar to: [virtual_environment_path]/Lib/site-packages/django/contrib/gis/gdal/libgdal.py.
Open the libgdal.py file with a text editor.
Find the line that starts with lib_names = ["gdal204", ...] (the line number may vary depending on the Django version).
Add the GDAL library version (e.g., "gdal307") to the beginning of the lib_names list, separated by commas.
Example: lib_names = ["gdal307", "gdal204", ...]
Save the changes to the libgdal.py file.
#### Step 4: Configure Environment Variables
Create the .env file in your project directory and add the following line to it:
``` 
GDAL_LIBRARY_PATH = "C:\\OSGeo4W\\bin\\gdal307.dll"
```
Replace C:\OSGeo4W\bin\gdal307.dll with the actual path to the GDAL library file.




