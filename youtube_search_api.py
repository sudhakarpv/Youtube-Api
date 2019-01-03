# Youtube-Api
from flask import Flask
from flask_restful import Api, Resource
from apiclient.discovery import build
app = Flask(__name__)
api = Api(app)


@app.route('/')
def index():
    return "Hello World"


@app.route("/youtube_searchs", methods=['GET', 'POST'])
class Youtube(Resource):
    def get(self, search):
        api_key = "your api key"
        youtube = build('youtube', 'v3', developerKey=api_key)
        req = youtube.search().list(part='snippet', type='video', maxResults=20, q=search)
        titles = []
        res = req.execute()
        for item in res['items']:
            title = item['snippet']['title']
            titles.append(title)
        return res


api.add_resource(Youtube, '/youtube_search/<string:search>')

if __name__ == '__main__':
    app.run(debug=True)
