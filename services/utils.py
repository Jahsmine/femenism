import random
import os
from flask import current_app
from PIL import Image
from nerual.gender import resolve


def make_gender_sentence(picture, picture_path_saved):
    save_picture(picture)
    picture_path = os.path.join(
        'static/profile_pics',
        picture_path_saved
    )
    out_sentence = resolve(picture_path)
    gender_quotes, flag = None, None
    if out_sentence[0] == "male":
        gender_quotes = "male"
        flag = "danger"
    if out_sentence[0] == "female":
        gender_quotes = "female"
        flag = "success"
    if len(out_sentence) == 0:
        flag = "info"
        return "Это точно человек?", flag
    with open(gender_quotes, "r") as f:
        lines = f.read().splitlines()
    gender_sentence = random.choice(lines)
    os.remove(picture_path)
    return gender_sentence, flag


def save_picture(file_picture):
    picture_period_path = os.path.join(
        current_app.root_path,
        'static/profile_pics',
        file_picture.filename
    )
    saved_image = Image.open(file_picture)
    saved_image.save(picture_period_path)
    return file_picture
