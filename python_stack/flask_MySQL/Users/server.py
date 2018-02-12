from flask import Flask, render_template, request, redirect, flash, session
from mysqlconnection import MySQLConnector
import re
import md5

app = Flask(__name__)
app.secret_key = "ThisSecretKey"
mysql = MySQLConnector(app, 'walldb')

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/users'):


@app.route('/users/new'):


@app.route('users/<id>/edit'):


@app.route('/users/<id>'):


@app.route('/users/create'):


@app.route('/users/<id>/destroy'):


