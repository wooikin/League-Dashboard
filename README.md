<div align="center">
<img src="https://img.freepik.com/premium-vector/soccer-ball-icon-logo-template-football-logo-symbol_7649-4092.jpg?w=206">
<h1>
  League-Dashboard
</h1>

_A dashboard for ranking table of sport league._
</div>
  

# User Guide


```
1. Select CSV by selecting the "Choose File" Button
2. Proceed to upload by selecting the "Upload CSV" Button
3. The Ranking Table and All Matches from the CSV are now displayed.
4. If user is authorized (login using same name as the team/ superuser), User can "Edit" and "Delete" the match from the list of matches.
5. User can also add new match by selecting the "Add a new match" hyperlink.
6. User is not able to add a match for teams that is not presented in the CSV uploaded in step 1.
```


# Developer Notes

## Setting up your environment

Ensure you have Python installed.

```
python -m venv <path-to-virtualenv-folder>
eg. python -m venv env
```
Reminder: Do not commit/push virtual env folder to git! Add your virtual env folder into .gitignore file

Activate python virtual environment
```
env\Scripts\activate (windows)
source env/bin/activate (linux)
```

Install required packages from requiremnts.txt file
```
pip install -r <path-to>\requirements.txt
```

## To create a superuser

```
python manage.py createsuperuser
```

## Start django server

```
python manage.py runserver
```

## Run Test

```
python manage.py test
```



# Roadmap Items
```
1. Export result to CSV
2. User Interface
3. Enable user to add new team
4. Cross-check in UI/UX- eg. user is able to add match between 2 same teams
5. To enable authentification not only on "Edit" and "Delete" but include "Add a new match" and "Upload CSV"
```