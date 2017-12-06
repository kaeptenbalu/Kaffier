from flask import render_template, request, current_app, flash

from . import home
from ..helpers import coffee
from ..models import Product, Beer, Senseo
from app import db

@home.route('/')
def shopping():
    """
    Render the homepage template on the / route
    """
    return render_template('home/index.html', title="Welcome to Kaffier")


@home.route('/beer')
def beerpage():
    """
    Render the dashboard template on the /beer route
    """
    products = Product.query.all()
    beers = Beer.query.all()
    return render_template('home/beer.html', title="Beer", products=products, beers=beers)


@home.route('/coffee', methods=['GET'])
def coffeepage():
    """
    Render the dashboard template on the /coffee route
    """
    coffeemachine = Senseo.query.get(1)
    return render_template('home/coffee.html', title="Coffee", status=coffeemachine.status)

@home.route('/coffee', methods=['POST'])
def coffeeaction():
    """
    Action!!!
    """
    error = None
    success = None
    coffeemachine = Senseo.query.get(1)
    if coffee.initialize():
        params = request.form
        if params['power-button']:
            if coffee.on_off():
                if coffeemachine.status:
                    success = "Device is now off."
                    coffeemachine.status = False
                else:
                    success = "Device is now on."
                    Senseo.status = True
                db.commit()
            else:
                error ="Can not turn off/on the device."
    else:
        error = "Could not initialize the coffe machine."
    if error:
        flash(error, "danger")
        current_app.logger.error(error)
    if success:
        flash(success, "success")
        current_app.logger.info(success)
    status = coffeemachine.status

    return render_template('home/coffee.html', title="Coffee", status=status)
