from . import view
from flask import render_template


@view.app_errorhandler(404)
def view_not_found(err):
    return render_template('not_found.html')


@view.errorhandler(500)
def internal_error(err):
    return err.description


@view.errorhandler(404)
def not_found(err):
    return err.description