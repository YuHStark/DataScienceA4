from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    req = request.get_json(force=True)
    
    intent = req["queryResult"]["intent"]["displayName"]
    
    if intent == "AskGenreIntent":
        return jsonify({"fulfillmentText": "Which genre are you interested in?"})
    
    if intent == "HandleGenreIntent":
        genre = req["queryResult"]["parameters"].get("genre", "a book")
        return jsonify({"fulfillmentText": f"Great! Here are some {genre} books I recommend."})
    
    return jsonify({"fulfillmentText": "I'm not sure how to help with that."})

if __name__ == "__main__":
    app.run(port=5000, debug=True)
