from flask import Blueprint, request, jsonify
from api.review.test import demo

review_blueprint = Blueprint('review_blueprint', __name__)


@review_blueprint.route('/', methods=['GET'])
def index():
    return 'review'


@review_blueprint.route('/', methods=['POST'])
def create():
    json = request.get_json()
    print(json)
    return 'review'


@review_blueprint.route('/test', methods=['GET'])
def test_a():
    return demo()
