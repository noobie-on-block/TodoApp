from flask import jsonify

from . import api


@api.route('/todos')
def todos():
    return jsonify([
        {'title': 'one', 'completed': False},
        {'title': 'two', 'completed': True}
    ])
