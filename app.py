from flask import Flask, render_template, request

app = Flask(__name__)

users = {
    'rubix': 'cube'
}

@app.route('/', methods=['GET', 'POST'])
def index():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users and users[username] == password:
            return render_template('success.html', username=username)
        else:
            error = 'Invalid username or password'

    return render_template('index.html', error=error)

if __name__ == '__main__':
    app.run(debug=True)