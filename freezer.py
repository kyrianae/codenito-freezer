#!/usr/bin/python3.8
from flask import Flask, json, request, Response
import random
import datetime
from loguru import logger

app = Flask("pizzaiolo")
name="Freeze"
def str_now():
    return str(datetime.datetime.now())

@app.route('/hello', methods=['GET'])
def hello():
    logger.info (str_now()+"\t"+name+"\tsays: Hello World")
    return str_now()+"\t"+name+"says: Hello World\n"

@app.route('/pie', methods=['GET'])
def pie():
    logger.info (str_now()+"\t"+name+"\tpie")
    return str_now()+"\t"+name+"\tpie\n"

@app.route('/cheese', methods=['GET'])
def cheese():
    logger.info (str_now()+"\t"+name+"\tcheese")
    return str_now()+"\t"+name+"\tcheese\n"

@app.route('/tomato', methods=['GET'])
def tomato():
    logger.info (str_now()+"\t"+name+"\ttomato")
    return str_now()+"\t"+name+"\ttomato\n"

@app.route('/ham', methods=['GET'])
def ham():
    logger.info (str_now()+"\t"+name+"\tham")
    return str_now()+"\t"+name+"\tham\n"

@app.route('/mushroom', methods=['GET'])
def mushroom():
    logger.info (str_now()+"\t"+name+"\tmuhsroom")
    return str_now()+"\t"+name+"\tmushroom\n"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8084)
