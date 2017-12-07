import random
import process_reddit as process
import os
import json
import markovify


JSON_PATH = 'markov_data/donald_latest_json'
MARKOV_MODEL_DIR = "markov_models"
PROJECT_DIR = os.environ['FLASKBB_DIR']

THREAD_TO_POST_RATIO = 0.90

def model_fname(subreddit_name):
    return "./models/{}.json".format(subreddit_name)


# def parse_json(fname):
def create_reddit_model(subreddit):
    json_path = "./{}".format(subreddit)
    text = process.get_posts_text(json_path)
    create_model_from_text(text, model_fname(subreddit))

def generate_body(text_model):
    max_paragraphs = 2
    max_paragraph_size = 4
    post_content = generate_paragraphs(text_model, max_paragraphs, max_paragraph_size)
    return post_content

def generate_paragraphs(text_model, max_paragraphs, max_paragraph_size):
    post_content = ""
    max_paragraphs = random.randint(1, max_paragraphs)
    for i in range(0, max_paragraphs):
        post_content += generate_paragraph(text_model, max_paragraph_size)

    return post_content


def generate_paragraph(text_model, max_paragraph_size):
    post_content = ""
    max_paragraph_size = random.randint(1, max_paragraph_size)

    for i in range(0, max_paragraph_size):
        post_content += text_model.make_sentence(test_output=False)
        post_content += " "


    post_content += "\n/p"

    return post_content


def load_model(data_fname):
    with open(data_fname) as data_file:
        model_json = json.load(data_file)

    return markovify.Text.from_json(model_json)

def create_model_from_text(text, output_fname):
    # Build the model.
    text_model = markovify.Text(text)
    model_json = text_model.to_json()
    with open(output_fname, "w") as f:
        json.dump(model_json, f)

    return text_model

def create_model_from_file(data_fname, output_fname):
    with open(data_fname, "r") as f:
        text = f.read()
    # Build the model.
    text_model = markovify.Text(text)
    model_json = text_model.to_json()
    with open(output_fname, "w") as f:
        json.dump(model_json, f)

    return text_model

create_reddit_model("Buffalo")
create_reddit_model("Existentialism")
create_reddit_model("hockey")
buffalo_model = load_model('./models/Buffalo.json')
hockey_model = load_model('./models/hockey.json')
existentialism_model = load_model('./models/Existentialism.json')
str = ""
for i in range(0, 1000):
    r = random.random()
    if r < 0.33:
        body = generate_body(buffalo_model)
    elif r < 0.66:
        body = generate_body(existentialism_model)
    else:
        body = generate_body(hockey_model)
    str = str + body

str = str.encode("utf8")
text_file = open("./buffalo.txt", "w")
text_file.write(str)
text_file.close()
