from flask import Flask, redirect, url_for, render_template, request
import os


app = Flask(__name__)

# INDEX:
@app.route("/")
def home():
    return render_template('index.html')

# @app.route("/", methods=["POST", "GET"])
# def message():
#     if 
#             print(message.sid)

#         return cortana(text, image)
#     else:
#         return render_template('index.html')


# CHAPTER DEMO:
@app.route("/demo")
def chapterDemo():
    return render_template('demo/chapter_demo.html')

@app.route("/demo", methods=["POST", "GET"])
def choice_cd_000():
    callsign = request.form['name']
    processed_callsign = callsign.upper()
    # view = request.input['image']
    return render_template('demo/cd_page_001.html', value=processed_callsign)

@app.route("/cd_001", methods=["POST", "GET"])
def choice_cd_001():
    text = request.form['option']
    processed_text = text.upper()
    if processed_text == "1":
        return render_template('demo/page_002/cd_page_002a.html')
    elif processed_text == "2":
        return render_template('demo/page_002/cd_page_002b.html')
    elif processed_text == "3":
        return render_template('demo/page_002/cd_page_002c.html')
    elif processed_text == "4":
        return render_template('demo/page_002/cd_page_002d.html')

@app.route("/cd_002b", methods=["POST", "GET"])
def choice_cd_002b():
    text = request.form['option']
    if text == "1":
        return render_template('demo/page_002b/cd_page_002b1.html')
    elif text == "2":
        return render_template('demo/page_002b/cd_page_002b2.html')

@app.route("/cd_002b1", methods=["POST", "GET"])
def choice_cd_002b1():
    text = request.form['option']
    if text == "1":
        return render_template('demo/page_002b1/cd_page_002b1a.html')
    elif text == "2":
        return render_template('demo/page_002b1/cd_page_002b1b.html')

@app.route("/cd_002b1a", methods=["POST", "GET"])
def choice_cd_002b1a():
    text = request.form['option']
    if text == "1":
        return render_template('demo/page_002b1/cd_page_002b1a1.html')

@app.route("/cd_end", methods=["POST", "GET"])
def choice_cd_002c():
    text = request.form['option']
    if text == "1":
        return render_template('demo/cd_page_end.html')


# CHAPTER 00:
@app.route("/c00")
def chapter00():
    return render_template('chapter_00/chapter_00.html')

@app.route("/c00", methods=["POST", "GET"])
def choice_00_000():
    text = request.form['option']
    processed_text = text.upper()
    if processed_text == "1":
        return render_template('index.html')
    else:
        return render_template('index.html')


if __name__=="__main__":
    app.run(debug=True)

