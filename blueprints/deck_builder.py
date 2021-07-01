from flask import Blueprint, render_template

blue = Blueprint('deck_builder', __name__, static_folder="static", template_folder="templates")


@blue.route('/<guild>/<user>')
def deck_builder(guild, user):
    return render_template('deck_builder.html', guild=guild, user=user)
