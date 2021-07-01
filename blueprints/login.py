from flask import Blueprint, request, redirect, url_for, render_template

blue = Blueprint('login', __name__, static_folder="static", template_folder="templates")


@blue.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        guild = request.form["guildInput"]
        user = request.form["userInput"]
        if guild.isnumeric() and user.isnumeric():
            return redirect(url_for('collection.collection', guild=guild, user=user))
    return render_template('login.html')