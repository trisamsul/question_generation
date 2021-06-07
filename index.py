import json
from pipelines import pipeline
from flask import Flask, request, make_response

app = Flask(__name__)


@app.route("/generate-questions", methods=['GET', 'POST'])
def generate_questions():
    # getting the request data
    data = request.json
    text = data['text']

    nlp = pipeline("multitask-qa-qg", model="valhalla/t5-small-qa-qg-hl")
    result = nlp(text)

    response = make_response({
        'status': True,
        'message': 'Success',
        'data': result
    })
    response.mimetype = 'application/json'

    return response
