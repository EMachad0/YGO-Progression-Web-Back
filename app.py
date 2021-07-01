from flask import Flask, render_template, url_for, redirect, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        guild = request.form["guildInput"]
        user = request.form["userInput"]
        if guild.isnumeric() and user.isnumeric():
            return redirect(url_for('collection', guild=guild, user=user))
    return render_template('login.html')

@app.route('/collection/<guild>/<user>')
def collection(guild, user):
    return render_template('collection.html', guild=guild, user=user)

@app.route('/deck_builder/<guild>/<user>')
def deck_builder(guild, user):
    return render_template('deck_builder.html', guild=guild, user=user)


if __name__ == '__main__':
    app.run(debug=True)
