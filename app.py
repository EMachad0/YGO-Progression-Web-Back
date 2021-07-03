from flask import Flask, url_for, redirect

import blueprints

app = Flask(__name__)
app.register_blueprint(blueprints.login)
app.register_blueprint(blueprints.collection, url_prefix="/collection")
app.register_blueprint(blueprints.deck_builder, url_prefix="/deck_builder")

@app.route('/')
def index():
    return redirect(url_for('login.login'))


if __name__ == '__main__':
    app.run(debug=True)
