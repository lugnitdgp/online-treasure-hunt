# Online Treasure Hunt is an online event of the Aavishkar fest organised by GNU/Linux users group, NIT Durgapur.


## Build Instructions :

1. Clone the repo `git clone https://github.com/JayjeetAtGithub/online-treasure-hunt.git`
2. Start a new virtualenv `virtualenv myenv`
3. Install the dependencies `cd online-treasure-hunt` & `pip install -r requirements.txt`
4. Create a .env file `touch .env`
5. Create apps in Facebook and Google and then in the .env file write the env vars along with the corresponding values :

    * `SECRET_KEY=abcd`
    * `SOCIAL_AUTH_FACEBOOK_KEY=abcd`
    * `SOCIAL_AUTH_FACEBOOK_SECRET=abcd`
    * `SOCIAL_AUTH_GOOGLE_OAUTH2_KEY=abcd`
    * `SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET=abcd`    

6. Complete the migrations `python manage.py makemigrations` & `python manage.py migrate`
7. Create a superuser `python manage.py createsuperuser`
8. Run the server `python manage.py runserver`


