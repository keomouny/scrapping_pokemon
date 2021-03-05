from flask import Flask, request, render_template, jsonify, redirect
from flask_cors import CORS
from pokemon import pokemon, pprint
from db import *
import requests
from setup_logger import logger
import json

app = Flask(__name__)
CORS(app)


@app.route('/create_table/<tablename>')
def create_table(tablename):

    db = DB()
    try:
        db.execute_query(db.create_table, tablename)
        pokemon.message = 'SUCCESS'
    except:
        pokemon.message = 'impossible to create table'
        app.logger.error('impossible to create table')
    db.__disconnect__()
    return redirect('/admin')


@app.route('/remove_table/<tablename>')
def delete_table(tablename):
    db = DB()
    try:
        db.execute_query(db.delete_table, tablename)
        pokemon.message = 'SUCCESS'
    except:
        pokemon.message = 'impossible to remove table'
        app.logger.error('impossible to remove table')
    db.__disconnect__()
    return redirect('/admin')


@app.route('/remove_data/<tablename>')
def delete_all_data(tablename):
    db = DB()
    try:
        db.execute_query(db.delete_data, tablename)
        pokemon.message = 'SUCCESS'
    except:
        pokemon.message = 'impossible to remove all data'
        app.logger.error('impossible to remove all data')
    db.__disconnect__()
    return redirect('/admin')


@app.route('/api/query_data/<query>')
def get_pokemon_list(query):
    try:
        db = DB()
        data_pokemon = db.select_from_db(query)
        db.__disconnect__()
        return jsonify(data_pokemon)
    except:
        pokemon.message = 'ERROR'
        return redirect('/admin')


@app.route("/api/query_data/all_data")
def page_data_all():
    try:
        data_all = {}
        for i in pokemon().scrap_type:
            data = requests.get(
                f'{request.url_root}api/query_data/{i}').text
            data_all[i] = json.loads(data)
        return jsonify(data_all)
    except:
        message = 'ERROR'
        return redirect('/admin')


@app.route('/insert_data/<tablename>')
def insert_data(tablename):
    db = DB()
    try:
        db.insert_data(tablename, pokemon().scrap_data(tablename))
        pokemon.message = 'SUCCESS'
    except:
        logger.error('impossible to insert data')
        pokemon.message = 'ERROR'
    db.__disconnect__()
    return redirect('/admin')


@app.route("/admin")
def page_admin():
    return render_template("admin.html", message=pokemon.message)


@app.route("/ma_page_data/<tablename>")
def page_data(tablename):
    data_list = requests.get(
        f'{request.url_root}api/query_data/{tablename}').text
    data_list_json = json.loads(data_list)
    return render_template(pokemon().scrap_type[tablename][3], data=data_list_json)


@app.route("/")
def page_all_data():
    logger.info('go to main page with all data')
    try:
        data_list = requests.get(
            f'{request.url_root}api/query_data/all_data').text
        data_list_json = json.loads(data_list)
    except:
        logger.error('no data from database')
        data_list_json = []
    return render_template("page_principal.html", data=data_list_json)
