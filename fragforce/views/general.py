from fragforce import app
from flask import Blueprint, render_template, session, redirect, url_for, \
        request, abort

mod = Blueprint('general', __name__)

@mod.route('/')
def index(name=None):
  return render_template('general/index.html', name=name)
@mod.route('/contact')
def contact(name=None):
  return render_template('general/contact.html', name=name)
@mod.route('/donate')
def donate(name=None):
  return render_template('general/donate.html', name=name)
@mod.route('/join')
def join(name=None):
  return render_template('general/join.html', name=name)
