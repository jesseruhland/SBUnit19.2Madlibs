from flask import Flask, request, render_template
from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = "randomkey"

@app.route("/")
def display_home():
    story_words = story.prompts 
    return render_template("home.html", story_words=story_words)


@app.route("/story")
def display_story():
    story_words = request.args
    complete_story = story.generate(story_words)
    return render_template("story.html", complete_story=complete_story)