# Django oAuth Template
 An example of how to create a Django web app with SSO support using oAuth.

 ## Installation

 1. Download or clone the source code from the website: `git clone git@github.com:kuan51/djcal.git`
 2. Create a python3 virtual environment: `python3 -m venv [name_of_your_virtual_environment]`
 3. Install dependencies: `pip install -r requirements.txt`
 4. Migrate databases and applications: `python ./manage.py migrate`
 5. Sync databases: `python ./manage.py migrate --run-syncdb`
 6. Create admin user: `python ./manage.py createsuperuser`
 7. Run server: `python ./manage.py runserver`
 8. Browse to `localhost:8000` and login with the username and password from step 6.

 ## Configure oAuth

 You will need to repeat this guide for each social media application you have.

 1. Browse to `localhost:8000/admin` and login with your admin user.
 2. Go to Social Applications > Add Social Application
 3. Login to your oAuth account (i.e. Github, Google, Reddit, etc) and find your client id and secret.
 4. Select the oAuth app you want to configure from the dropdown and assign a name.
 5. Enter the client id and secret from step 3 and save.
 6. Go back to the main admin page: `localhost:8000`
 7. Go to Sites > Click on the example site name.
 8. Change the domain name to localhost and save.
 9. Browse to Social Applications > Click on the name of your oAuth account
 10. Under sites, add localhost to the right column "Chosen Sites" and save.
 11. Logout and test the oAuth login, it should automatically create a user based on the username from the oauth application. It only requests your username and email, and no other information.
