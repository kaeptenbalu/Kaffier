from flask import render_template, request

from . import home
from ..helpers import coffee
from ..models import Product, Beer

@home.route('/')
def homepage():
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


@home.route('/coffee')
def coffeepage():
    """
    Render the dashboard template on the /coffee route
    """
    coffee.initialize()
    on_off = request.args.get('on_off')
    go = request.args.get('go')
    alarm_time = request.args.get('time')

    if go is not None:
        coffee.write_file('/sys/class/gpio/gpio23/direction','out')
        time.sleep(5)
        coffee.write_file('/sys/class/gpio/gpio23/direction','in')
        return 'Hmmmm chafe.. nom nom'

    if on_off is not None:
        coffee.write_file("/sys/class/gpio/gpio22/direction", "out")
        coffee.write_file("/sys/class/gpio/gpio22/value","1")
        time.sleep(5)
        coffee.write_file("/sys/class/gpio/gpio22/value","0")
        return 'haeaseasea...'

    if alarm_time is not None:
        alarm_h = int(alarm_time[:2])
        alarm_m = int(alarm_time[3:])
        timer_thread = Thread(target=coffee.timer, args=(alarm_h, alarm_m,))
        timer_thread.start()
        return render_template('form.html')

    return render_template('home/coffee.html', title="Coffee")
