from flask import Blueprint, render_template

blue = Blueprint('collection', __name__, static_folder="static", template_folder="templates")


@blue.route('/<guild>/<user>')
def collection(guild, user):
    return render_template('collection.html', guild=guild, user=user)
