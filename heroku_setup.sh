git init
heroku create
pip install gunicorn psycopg2-binary
pip freeze > requirements.txt
echo "web: gunicorn main:app" > Procfile
git add .; git commit -a -m "Initial commit"
git push heroku master
heroku addons:create heroku-postgresql:hobby-dev
heroku run python setup.py
heroku open