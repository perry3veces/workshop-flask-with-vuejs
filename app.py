from flask import Flask
from flask_restplus import Resource, Api

app = Flask(__name__)
api = Api(app)
PRE_URL = '/api/v1/'


@api.route(PRE_URL + 'signup')
class Signup(Resource):

    def post(self):
        return {'hello': 'world'}


@api.route(PRE_URL + 'login')
class Login(Resource):

    def post(self):
        return {'hello': 'world'}


@api.route(PRE_URL + 'login')
class Logout(Resource):

    def get(self):
        return {'hello': 'world'}


@api.route(PRE_URL + 'news')
class News(Resource):

    def get(self):
        return {'hello': 'world'}

    def post(self):
        return {'hello': 'world'}


@api.route(PRE_URL + 'news/<int:id>')
class News_single(Resource):

    def get(self, id):
        return {'hello': id}


@api.route(PRE_URL + 'news/<int:id>/comments')
class Comments(Resource):

    def get(self, id):
        return {'hello': 'world'}

    def post(self, id):
        return {'hello': 'world'}


if __name__ == '__main__':
    app.run(debug=True)

