from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from stories import storyA, storyB, storyC, storyD

app = Flask(__name__)

app.config['SECRET_KEY'] = "my-secret-key"
# debug = DebugToolbarExtension(app)
@app.route('/')
def story_template_option():
    return render_template('option_form.html')



@app.route('/storyA')
def ans_form():
    """form to fill out words for a story"""
    words = storyA.prompts
    return render_template("form.html",form_prompt_words=words)

@app.route('/storyB')
def ans_form():
    """form to fill out words for a story"""
    words = storyB.prompts
    return render_template("form.html",form_prompt_words=words)

@app.route('/storyC')
def ans_form():
    """form to fill out words for a story"""
    words = storyC.prompts
    return render_template("form.html",form_prompt_words=words)

@app.route('/storyD')
def ans_form():
    """form to fill out words for a story"""
    words = storyD.prompts
    return render_template("form.html",form_prompt_words=words)


@app.route('/new_story', methods=["POST"])
def new_story():
    ans = {}
    words = story.prompts
    for word in words:
        ans[word] = request.form[word]
    text = story.generate(ans)
    return render_template("story.html",text=text)

# @app.route('/story')
# def story():
#     return;


