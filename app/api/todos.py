from . import api
from ..models import User
from .. import db
from flask import request
from flask_login import login_required

@api.route('/todos', methods=['PUT'])
@login_required
def edit_todos():
	id = request.json['id']
	todos = request.json['todos']
	User.query.filter_by(id=id).first().todos = str(todos)
	db.session.commit()

	return 'HELLO'