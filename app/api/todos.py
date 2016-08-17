from . import api
from ..models import User
from flask_login import login_required

@api.route('/todos/<int:id>')
def get_todos(id):
	todos = User.query.filter_by(id=id).first().todos
	todos = '[{text: "test"}]'
	return todos