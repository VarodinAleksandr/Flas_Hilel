from flask import Flask, request
from faker import Faker
import requests
import csv

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/requirements/", methods=['GET'])
def upload_file():
    if request.method == 'GET':
        with open('requirements.txt') as file:
            text = file.read()
            return text


@app.route("/generate-users/", methods=['GET'])
def user_list():
    fake = Faker()
    user_dict = {}
    count = 100
    args = request.args
    if args.get('count'):
        count = int(args.get('count'))
    for i in range(count):
        name = fake.name()
        short_name = name.lower().split()
        user_dict[name] = f'{short_name[0][0]}{short_name[1]}@example.com'
    return user_dict


@app.route("/mean/", methods=['GET'])
def weight():
    weight_total = 0
    height_total = 0
    count = 0
    with open('hw.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for i in csv_reader:
            if count != 0:
                weight_total += float(i[2])
                height_total += float(i[1])
                count += 1
            else:
                count += 1
        average_height = height_total * 2.54 / count
        average_weight = weight_total * 0.453592 / count
        return {'average_height': average_height, 'average_weight': average_weight}


@app.route("/space/", methods=['GET'])
def space_1():
    r = requests.get('http://api.open-notify.org/astros.json')
    result = r.json()
    a = result['number']
    return f'Number of cosmonauts - {a}'
