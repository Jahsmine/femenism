from flask import Flask, render_template, flash, redirect, url_for
from services.utils import make_gender_sentence
from models.innermodels import UploadFileModel

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'


# @app.route('/', methods=['GET', 'POST'])
# def start():
#     form = UploadFileModel()
#     if form.validate_on_submit():
#         message, flag = make_gender_sentence(form.picture.data, form.picture.data.filename)
#         flash(message, flag)
#         return redirect(url_for('start'))
#     return render_template(
#         'account.html',
#         title='Распознать гендерное существо',
#         form=form
#     )

@app.route('/', methods=['GET', 'POST'])
def start():
    form = UploadFileModel()
    return render_template(
        'account.html',
        title='Распознать гендерное существо',
        form=form
    )


if __name__ == '__main__':
    app.run()
