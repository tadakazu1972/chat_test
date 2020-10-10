import json
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index_chat.html')

@app.route('/post', methods=['GET','POST'])
def get_request():
    value = request.args.get('text', '')
    callback = request.args.get('callback', '')

    if (value.find('おはよう') != -1):
        value = 'おはようございます。<br>お元気ですか？'

    if (value.find('元気') != -1):
        value = '元気でよかったです。私も元気です。'

    if (value.find('さようなら') != -1):
        value = 'またお越しください。'

    dic = {'output' : [{'type' : 'text', 'value' : value }] }
    contents = callback + '(' + json.dumps(dic) + ')'
    return contents

if __name__ == "__main__":
    app.run(debug=True)
