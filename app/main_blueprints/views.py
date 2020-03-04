from random import random
from flask import render_template, abort
from . import view


@view.route('/')
def index():
    number = random()
    if number < 0.99:
        if number < 0.2:
            abort(404, 'I just decided that this view doesn\'t exist')
        return render_template('index.html', message="Welcome!")
    else:
        abort(500,
              'Aborting - a uniformly distributed pseudo random number came out greater than 0.99')
