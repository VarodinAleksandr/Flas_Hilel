from .db import get_db
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from flask_bootstrap import Bootstrap


bp = Blueprint('track', __name__)


@bp.route("/names/", methods=['GET'])
def artist_number():
    if request.method == 'GET':
        number = get_db().execute('SELECT COUNT(DISTINCT artist) FROM tracks;').fetchone()
        return render_template('track/names.html', name=number[0])


@bp.route("/tracks/", methods=['GET'])
def tracks_number():
    if request.method == 'GET':
        args = request.args
        genre = args.get('genre')
        if genre:
            number = get_db().execute('SELECT COUNT(*) FROM tracks WHERE genre = ?', (genre,)).fetchone()
            return render_template('track/genre.html', number=number[0], genre=genre)
        else:
            number = get_db().execute('SELECT COUNT(*) FROM tracks;').fetchone()
            return render_template('track/tracks.html', number=number[0])


@bp.route("/tracks-sec/", methods=['GET'])
def track_time():
    if request.method == 'GET':
        tracks = get_db().execute('SELECT title, length_track FROM tracks')
        return render_template('track/trackstime.html', tracks=tracks)


@bp.route("/tracks-sec/statistics/", methods=['GET'])
def track_statistic():
    if request.method == 'GET':
        all_time = get_db().execute('SELECT SUM(length_track) FROM tracks;').fetchone()
        average = get_db().execute('SELECT AVG(length_track) FROM tracks;').fetchone()
        return render_template('track/statistics.html', all_time=all_time[0], average=average[0])
