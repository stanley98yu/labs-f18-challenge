from flask import Flask, render_template
import requests
import json

app = Flask(__name__)


@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')

@app.route('/pokemon/<query>', methods=['GET'])
def display_pokemon(query):
    try:
        id = int(query)
        url = 'http://pokeapi.co/api/v2/pokemon/{0}'.format(id)
        r = requests.get(url)
        name = r.json()["name"]
        return render_template('id.html', id=id, name=name)
    except ValueError:
        url = 'http://pokeapi.co/api/v2/pokemon/{0}'.format(query)
        r = requests.get(url)
        id = r.json()["id"]
        return render_template('name.html', id=id, name=query)

if __name__ == '__main__':
    app.run()
