### Online Treasure Hunt is an online event of the Mukti fest organised by GNU/Linux users group, NIT Durgapur.

## Build Instructions

1. `git clone https://github.com/JayjeetAtGithub/online-treasure-hunt.git`
2. `virtualenv myenv`
3. `cd online-treasure-hunt` & `pip install -r requirements.txt`
4. `touch .env`
5. `In the .env file write the env vars along with the corresponding values : `

    * `SECRET_KEY=abcd`
    * `SOCIAL_AUTH_FACEBOOK_KEY=abcd`
    * `SOCIAL_AUTH_FACEBOOK_SECRET=abcd`
    * `SOCIAL_AUTH_GOOGLE_OAUTH2_KEY=abcd`
    * `SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET=abcd`    

6. `python manage.py makemigrations` & `python manage.py migrate`
7. `python manage.py runserver`


