import os
import pandas as pd
import numpy as np
import flask
import pickle
from jotform import JotformAPIClient
from googletrans import Translator
import re
import tensorflow_text as tf_text
import tensorflow as tf
import pathlib
from flask import Flask, request, render_template, session, redirect
import numpy as np
import pandas as pd


app = Flask(__name__)


@app.route('/')
def index():
    return flask.render_template("index.html")


def ValuePredictor(to_predict_list):
    to_predict = np.array(to_predict_list).reshape(1, 4)
    loaded_model = pickle.load(open("model.pkl", "rb"))
    result = loaded_model.predict(to_predict)
    return result[0]


def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext


@app.route('/predict', methods=("POST", "GET"))
def result():
    if request.method == 'POST':
        codes = {
            "Turkish": "tr",
            "Italian": "it",
            "Arabic": "ar",
            "Bulgarian": "bg",
            "Dutch": "nl",
            "Portuguese": "pt",
            "Serbian": "sr",
            "Finnish": "fi",
            "French": "fr",
            "Spanish": "es",
            "Ukrainian": "uk",
            "Hungarian": "hu",
            "Indonesian": "id",
            "Hungarian": "hu",
            "German": "de"
        }
        # variable declarations
        translator = Translator()
        path = os.path.dirname(os.path.abspath(__file__))
        input_sentences = []
        apikey = "7f8ce90b8d898a20bebcb12c3d8b52be"
        jotformAPI = JotformAPIClient(apikey)

        # getting input
        user_input = request.form.to_dict()
        formid = user_input['formid']
        language = user_input['langs']
        option = codes[language]
        language = path + '\\models\\' + language
        reloaded = tf.saved_model.load(language)

        # getting form elements
        questions = jotformAPI.get_form_questions(formid)
        for i in questions:
            try:
                text = questions[i]['text']
                clean_text = cleanhtml(text)
                if(clean_text == "Page Break"):
                    continue
                input_sentences.append(clean_text)
            except KeyError:
                pass

        print(input_sentences)
        input_text = tf.constant(input_sentences)

        result = reloaded.tf_translate(input_text)
        decoded = []

        for tr in result['text']:
            decoded.append(tr.numpy().decode())

        # google translate for checking the output
        google = []
        for example in input_sentences:
            gt = translator.translate(example, src=option)
            google.append(gt.text)

        output = pd.DataFrame(
            {'Input Sentences': input_sentences,
             'Jotform Tanslation Tool': decoded,
             'Google Translate': google
             })

        pd.set_option('max_colwidth', 800)
        pd.set_option('max_rows', 20)
        output
        prediction = output

    return render_template('predict.html',  tables=[output.to_html(classes='data', header="true")])


if __name__ == "__main__":
    app.run(debug=True)
