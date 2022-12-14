from flask import Flask, request, render_template
from stories import story, story_list

app = Flask(__name__)
app.config['SECRET_KEY'] = "randomkey"

@app.route("/")
def display_home():
    """Display the home page with the story dropdown menu"""
    return render_template("home.html", story_list=story_list)

@app.route("/selected_story")
def display_story():
    """Display the prompts for the chosen story in a form"""
    chosen_story = story_list[f"{request.args['story']}"]
    story_name = request.args['story']
    story_words = chosen_story.prompts 
    return render_template("selected_story.html", story_words=story_words, story_name=story_name)


@app.route("/story")
def completed_story():
    """Display the completed story with the input from the prompt form"""
    chosen_story = story_list[f"{request.args['story']}"]
    story_words = request.args
    complete_story = chosen_story.generate(story_words)
    return render_template("story.html", complete_story=complete_story)