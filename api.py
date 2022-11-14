from flask import Flask
from flask import jsonify
import scores

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

@app.route('/', methods=['GET'])
def get_stats_table():
    return jsonify(PremierLeague=scores.stats)

app.run()
