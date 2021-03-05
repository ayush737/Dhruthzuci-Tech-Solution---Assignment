# dependencies
from flask import Flask, jsonify, request

# Flask App configuration
app = Flask(__name__)

@app.route("/find_symbols_in_names", methods=['POST'])
def find_symbols_in_names():
    chemicals = request.json['chemicals']
    symbols = request.json['symbols']
    result = []

    for chemical in chemicals:
        for symbol in symbols:
            index = chemical.find(symbol)
            if(index!=-1):
                result.append(chemical[0:index]+"["+symbol+"]"+chemical[index+len(symbol):])
                
    
    return jsonify({"result":result})


if __name__ == '__main__':
    app.run(debug=True)