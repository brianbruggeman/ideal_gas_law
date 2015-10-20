from flask import render_template, flash, redirect, url_for, request
from app import app
from .forms import GasLaw
from .calculator import calculate_ideal_gas


@app.route('/calculated')
def calculated(*args, **kwds):
    data = {k: v for k, v in request.args.iteritems()}

    data, missing_key = calculate_ideal_gas(data)
    return render_template('calculated.html',
                           title='Ideal Gas Law',
                           data=data,
                           missing_key=missing_key)

@app.route('/', methods=['GET', 'POST'])
@app.route('/IdealGasLaw', methods=['GET', 'POST'])
def login():
    form = GasLaw()
    if form.validate_on_submit():
        data = {k: v for k, v in form.data.iteritems() if v}

        return redirect(url_for('calculated', **data))
    else:
        flash('Failed validation')
    return render_template('entry.html',
                           title='Ideal Gas Law',
                           form=form)
