"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file contains the routes for your application.
"""

import os
from app import app, db
from flask import render_template, request, redirect, url_for, flash, send_from_directory
from werkzeug.utils import secure_filename
from app.models import Property
from app.forms import AddPropertyForm

###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Javon Peart")


@app.route('/properties/create', methods=['GET', 'POST'])
def create_properties():
    """Render the website's properties creation page."""
    form = AddPropertyForm()

    if request.method == "POST" and form.validate_on_submit():
        try:
            title = form.title.data
            bedrooms = form.bedrooms.data
            bathrooms = form.bathrooms.data
            location = form.location.data
            price = form.price.data
            type = form.type.data
            description = form.description.data
            imgData = form.photo.data

            image = secure_filename(imgData.filename)
            imgData.save(os.path.join(app.config['IMAGES_FOLDER'], image))

            property = Property(title, bedrooms, bathrooms, location, price, type, description, image)

            db.session.add(property)
            db.session.commit()

            flash('Property successfully added', 'success')
            return redirect(url_for('properties'))
        except Exception as e:
            flash('Invalid Form Data', 'danger')
    
    flash_errors(form)
    return render_template('create_properties.html', form=form)


@app.route('/properties')
def properties():
    """Render a list of all properties in the database."""
    property = Property.query.all()
    return render_template('properties.html', property=property)


@app.route('/properties/<int:prop_id>')
def view_property(prop_id):
    """View an individual property by its specific property id."""
    property = Property.query.get(prop_id)
    return render_template('view_property.html', property=property)


@app.route('/properties/<filename>')
def find_file(filename):
    return send_from_directory(app.config['IMAGES_FOLDER'], filename)









###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404
