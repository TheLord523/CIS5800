from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json

#this file is a blueprint of our application (bunch of routes/URLS defined in it)
views = Blueprint('views', __name__)

@views.route('/home-faculty', methods = ['GET', 'POST'])
@login_required
def home_faculty():
    if request.method == 'POST':
        note = request.form.get('note')
        if len(note) < 1:
            flash("Note is too short!", category = 'error')
        else:
            new_note = Note(data=note, user_id = current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash("Note added!", category = 'success')
    return render_template("home_faculty.html", user = current_user)


@views.route('/', methods = ['GET', 'POST'])
@login_required
#for the home page, this is the route
def home():
    if request.method == 'POST':
        note = request.form.get('note')
        if len(note) < 1:
            flash("Note is too short!", category = 'error')
        else:
            new_note = Note(data=note, user_id = current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash("Note added!", category = 'success')
    return render_template("home.html", user = current_user)

@views.route('/delete-note', methods = ['POST'] )
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})