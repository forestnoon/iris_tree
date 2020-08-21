from flask import Flask, render_template, request, url_for
from sklearn.tree import DecisionTreeClassifier
import numpy as np
import joblib
from form import iris_form
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret key'
app.config['WTF_CSRF_ENABLED'] = True

# ブラウザのキャッシュを更新させる関数
@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                     endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)


@app.route('/')
def index():
    form = iris_form(request.form)
    return render_template('index.html', form=form)

@app.route('/',methods=['POST'])
def tree():
    form = iris_form(request.form)
    if request.method == "POST":
        if form.validate() == False:
            message = "you false"
            return render_template('index.html', form = form, message=message)

        if form.validate() == True:
            result = ''
            sepal_length = request.form.get('sepal_length', type=float)
            sepal_width = request.form.get('sepal_width', type=float)
            petal_length = request.form.get('petal_length', type=float)
            petal_width = request.form.get('petal_width', type=float)
    
            # load the model
            model = joblib.load('model.pickle')
            # predict

            result_data = {0:'setosa', 1:'versicolor', 2:'virginica'}

            test = np.array([[sepal_length,sepal_width,petal_length,petal_width]])
            result_ans = model.predict(test)
    
            # result_ans = result

            if result_ans == [0]:
                resultmessage =result_data[0]
            if result_ans == [1]:
                resultmessage = result_data[1]
            if result_ans == [2]:
                resultmessage = result_data[2]

        return render_template('index.html',form=form, resultmessage=resultmessage, result="アヤメの種類は{}です" .format( resultmessage))


if __name__ == '__main__':
    # app.run()
    app.debug = True
    app.run(host='localhost')
