# ONLINE TREASURE HUNT
**ONLINE TREASURE HUNT** is a game in which you are to get the answers of few riddles in each level,by each level difficulty level will also increase.You will be provided with a hint in the form of image or audio track.People who will solve maximum riddles in less time will win the game.

## Technologies Used IN ONLINE TREASURE HUNT
- HTML/CSS/JAVASCRIPT
- Django(PYTHON3)

IF you want to work with  you need to follow following steps:

1.It is better to work with *virtual environment* whenver working with any django projects.To create virtual environment use virtual environment need to be installed.
 - To install virtual environment:
 ```
 pip3 install virtualenv

 ```
 - To create virtual enviornment:
 ```
 virtualenv <name of your virtual enviornment>

 ```
2.Now clone the repository from https://github.com/lugnitdgp/online-treasure-hunt.git

3.Before you download any requirements related to project you should activate virtualenv:

#### For Linux/Mac OSX.   
```
source <name of your virtual enviornment> bin/activate

```

#### For Windows
```
.\Scripts\activate

```
4.Install the requirements for this project.
```
pip install -r requirements.txt

```
5.You need to set python-decouple library.
```
pip3 install python-decouple

```
  -Update your **.gitignore** adding the **.env** files,so you dont commit any sensitive data.
  -Now import the library in *online-treasure-hunt/settings.py*
  ```
  from decouple import config

  ```
  SECRET_KEY = config('SECRET_KEY')
  DEBUG = config('DEBUG', default=False, cast=bool)

6.You need to generate your own GoogleOAuth credentials with the following steps:

  + Go to the [Google Developers Console](https://console.developers.google.com/)

  + Create a project and fill in all the details

  + On the right side there is credentials tab, select it .

  + Click on **Create Credentials** then Oauth Client ID. Select application type Webapp , Give any name of your choice.

  + Under Authorized JavaScript origins fill
  `http://localhost:8000`
  Authorized redirect URIs `http://localhost:8000/account/complete/google-oauth2/`

  + Copy the CLient ID and Client Secret
   *Under .gitignore/.env*
   ```
      SOCIAL_AUTH_GOOGLE_OAUTH2_KEY =''  #Paste CLient Key
      SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '' #Paste Secret Key

    ```

7. Generate Facebook login credentials with the following steps:

  + Go to [Facebook Developers Console](https://developers.facebook.com/)

  + Click on **My Apps** and then **Add a New App**.

  + Enter _Display Name_ and _Contact Email_ and click on **Create App Id**.

  + Select **Facebook login** and choose **set up**. Pick **Web** on the next page.

  + Enter `http://localhost:8000` as the _Site Url_ and hit **Save**.

  + Now go to **Settings/Basic** and then in the _App Domains_ just put `localhost` and hit **Save Changes**.


  + Copy the App ID and App Secret and add them to the `.env` file.


8.Migrate the changes you have made to database.


    python3 manage.py makemigrations
    python3 manage.py migrate
    python3 manage.py runserver


9.Now you can open oth with `http://localhost:8000` in your browser. (Opening `http://127.0.0.1:8000` may cause problems with Social Login)

Thank You !!!
