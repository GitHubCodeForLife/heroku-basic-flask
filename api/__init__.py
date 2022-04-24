from flask import Blueprint
from api.user.user import user_blueprint
from api.data.data_controller import data_blueprint
from api.review.review import review_blueprint

api_blueprint = Blueprint('api_blueprint', __name__)


api_blueprint.register_blueprint(user_blueprint, url_prefix='/user')
api_blueprint.register_blueprint(data_blueprint, url_prefix='/data')
api_blueprint.register_blueprint(review_blueprint, url_prefix='/review')
