from flask import request, url_for
from flask_api import FlaskAPI, status, exceptions
from flask_api.decorators import set_renderers
from flask_api.renderers import JSONRenderer
from mainHandler import *
from appData import *
from page import *
from comma import *
from reader import *
from scrawled import *
from gentleman import *
app = FlaskAPI(__name__)

access_token = 'EAAEEMTLF8KQBAIqaTI8lEXQUQZC4xLPbTuFbgYfrcyZCWXFfNa8liNPuRthZAZB64gZBxJPqF4AtOgvVfxXbYYb5ZAaoOJK6wlp6KNMO0xIQUHBZAzit8iWcZBrpXbB1ZCbZCZBZCAKTZCy0GVm0oZCgqnwBZB7VasJYtar58kZD'

gread = App("176546272754384", "9ce4f9725d90f6a3090903e806d731fa")
# access_token = gread.id + "|" + gread.secret

# @app.route("/notes", methods = ['GET', 'POST'])
# def next_feed():
#     if request.method == 'POST':
#         response = {"1": "11111"}
#         return response, status.HTTP_201_CREATED
#     else:
#         return {'5':'something'}, status.HTTP_201_CREATED
#
# @app.route("/feedPage", methods=['GET', 'POST'])
# @set_renderers(JSONRenderer)
# def notes_list():
#     """
#     List or create notes.
#     """
#     if request.method == 'POST':
#         dataId = request.form['id']
#         id = getPageId(dataId)
#         response = getData(id, access_token)
#         response = json.loads(response)
#         return response, status.HTTP_201_CREATED
#


@app.route("/feed", methods=['GET', 'POST'])
@set_renderers(JSONRenderer)
def notes():
    """
    List or create not es.
    """
    if request.method == 'POST':
        dataId = request.form['id']
        id = getPageId(dataId)
        response = getData(id, access_token)
        response = json.loads(response)
        return response, status.HTTP_201_CREATED



def getPageId(dataId):
    if '1' == dataId:
        return comma_id
    if '2' == dataId:
        return reader_id
    if '3' == dataId:
        return scrawled_id
    if '4' == dataId:
        return gentleman_id
if __name__ == "__main__":
    app.debug=True
    app.run(host='127.0.0.1', port=5000)