from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    req = request.get_json(force=True)
    
    # Extract the Dialogflow intent name
    intent_name = req.get("queryResult", {}).get("intent", {}).get("displayName")

    # 1) Handle the Six Competency Questions (CQ1 - CQ6)
    if intent_name == "CQ1_MainRecommendationEngines":
        response_text = (
            "Our system uses three main recommendation engines: "
            "content-based filtering, rating-based filtering, and clustering-based recommendation. "
            "Each approach uses different data—like book descriptions, user ratings, or clustering algorithms—to suggest books."
        )

    elif intent_name == "CQ2_ContentBasedSimilarity":
        response_text = (
            "Content-based filtering measures similarity by analyzing features of each book, "
            "such as descriptions or text embeddings, often using a metric like cosine similarity."
        )

    elif intent_name == "CQ3_WeightedRatingCalculation":
        response_text = (
            "Rating-based filtering uses a weighted rating formula that combines the average rating "
            "with the number of reviews, ensuring popular books with many reviews get a fair ranking."
        )

    elif intent_name == "CQ4_ClusteringDiversification":
        response_text = (
            "Clustering-based recommendation groups similar books using algorithms like Gaussian Mixture Models (GMM). "
            "By clustering books, we can diversify suggestions and help users explore different categories."
        )

    elif intent_name == "CQ5_NLPFeaturesForContent":
        response_text = (
            "NLP features—like tokenization, embeddings, and named entity recognition—enhance content-based recommendations "
            "by capturing deeper semantic meaning in book descriptions."
        )

    elif intent_name == "CQ6_EvaluationMetrics":
        response_text = (
            "We evaluate the system using metrics like Precision & Recall, F1 Score, Mean Average Precision (MAP), "
            "and Mean Reciprocal Rank (MRR). Each highlights different aspects of recommendation quality."
        )

    # 2) Handle Multi-Turn Prompts (Genre-based Recommendation)
    elif intent_name == "AskGenreIntent":
        # First step: bot asks user which genre they like
        response_text = "Sure! Which genre are you interested in?"

    elif intent_name == "HandleGenreIntent":
        # Second step: user provides a genre parameter
        # e.g., create a @sys.any or custom @genre entity in Dialogflow
        genre = req["queryResult"]["parameters"].get("genre", "some genre")
        response_text = f"Great choice! Here are some {genre} books I recommend."

    else:
        # Fallback if intent is not recognized in this webhook
        response_text = "I'm not sure how to help with that."

    # Return the JSON response for Dialogflow
    return jsonify({"fulfillmentText": response_text})


if __name__ == "__main__":
    # For local testing; on Render, you'll use gunicorn in the Start Command instead
    app.run(host="0.0.0.0", port=5000, debug=True)
