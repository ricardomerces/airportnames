#Copia da main.py -->Dockerfile

import logging

from flask import Flask
from flask import request
from airports import Airports

app = Flask(__name__)
airport_util = Airports()

@app.route('/airportName', methods=['GET'])
def airportName():
    """Given an airport IATA code, return that airport's name."""
    iata_code = request.args.get('iataCode')
    if iata_code is None:
      return 'No IATA code provided.', 400
    maybe_name = airport_util.get_airport_by_iata(iata_code)
    if maybe_name is None:
      return 'IATA code not found : %s' % iata_code, 400
    return maybe_name, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
