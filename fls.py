from flask import Flask

from flask_restful import Resource, Api

app = Flask(__name__)

api = Api(app)

class Helloworld(Resource):
	def __init__(self):

		pass

	def get(self):

		return {

			"Heaven":"987",
            "Hellu" :"20","Susmi":"ty"

		}

api.add_resource(Helloworld, '/')

if __name__ == '__main__':

	app.run(debug=True)