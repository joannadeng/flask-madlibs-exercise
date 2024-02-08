from flask import Flask, render_template, request,redirect
from flask_debugtoolbar import DebugToolbarExtension
from stories import storyA, storyB, storyC, storyD

app = Flask(__name__)

app.config['SECRET_KEY'] = "my-secret-key"
# debug = DebugToolbarExtension(app)
@app.route('/')
def story_template_option():
    return render_template('option_form.html')

@app.route('/storyAll',methods=["POST"])
def ansall_form():
    """form to fill out words for a story"""
    # print(request.form)
    value = request.form['templates']
    return redirect(value)


@app.route('/storyA')
def ansa_form():
    """form to fill out words for a story"""
    words = storyA.prompts
    return render_template("form.html",form_prompt_words=words)

@app.route('/storyB')
def ansb_form():
    """form to fill out words for a story"""
    words = storyB.prompts
    return render_template("form.html",form_prompt_words=words)

@app.route('/storyC')
def ansc_form():
    """form to fill out words for a story"""
    words = storyC.prompts
    return render_template("form.html",form_prompt_words=words)

@app.route('/storyD')
def ansd_form():
    """form to fill out words for a story"""
    words = storyD.prompts
    return render_template("form.html",form_prompt_words=words)


# @app.route('/new_story', methods=["POST"])
# def new_story():
#     ans = {}
#     words = storyA.prompts
#     for word in words:
#         ans[word] = request.form[word]
#     text = storyA.generate(ans)
#     text = storyA.generate(ans)
#     return render_template("story.html",text=text)

@app.route('/new_story', methods=["POST"])
def new_story():

    ans_dict = request.form.to_dict() #.to_dict()is a built_in method to change an ImmutableMultiDict to a dict
    print (ans_dict)
    text = storyA.generate(ans_dict)
    return render_template("story.html",text=text)