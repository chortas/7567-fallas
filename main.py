from experta import *
from beer_decider import BeerDecider
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/beer")
def get_beer():

    initial_gravity = request.args.get('initial_gravity')
    final_gravity = request.args.get('final_gravity')
    color = request.args.get('color')
    alcohol_graduation = request.args.get('alcohol_graduation')
    bitterness = request.args.get('bitterness')

    print(f"""
    Params
        initial_gravity={initial_gravity}
        final_gravity={final_gravity}
        color={color}
        alcohol_graduation={alcohol_graduation}
        bitterness={bitterness}
    """)

    engine = BeerDecider()
    engine.reset()
    info_beer = Fact(
        initial_gravity=initial_gravity,
        final_gravity=final_gravity,
        color=color,
        alcohol_graduation=alcohol_graduation,
        bitterness=bitterness
    )
    engine.declare(info_beer)
    engine.run()

    data = {
        "beers": engine.get_beers(),
    }
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
