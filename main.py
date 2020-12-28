import os
import base64

from flask import Flask, render_template, request, redirect, url_for, session

from model import Donation, Donor 

app = Flask(__name__)
app.debug = True

@app.route('/')
def home():
    return redirect(url_for('all'))

@app.route('/donations/')
def all():
    donations = Donation.select()
    
    return render_template('donations.jinja2', donations=donations)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        user = request.form['name']
        value = int(request.form['value'])

        try:
            ''' verify donor is existing or not '''
            donor = Donor.get(Donor.name == user)
            Donation(donor=donor.id, value=value).save()
    
        except Donor.DoesNotExist:
            ''' If user not found add to database along with donation '''
            new_donor = Donor(name=user)
            new_donor.save()
            Donation(donor=new_donor.id, value=value).save()
    
        return redirect(url_for('all'))
    
    else:
        return render_template('add.jinja2')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6738))
    app.run(host='0.0.0.0', port=port)

