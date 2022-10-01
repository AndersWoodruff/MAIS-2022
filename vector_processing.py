import cohere

""" (list) -> list
Takes a list of strings tweets, embeds them, and returns the average vector user_average.
"""
def get_average_vector(user_tweets):
    co = cohere.Client("sLnFhVPzbaU4jWGV838B1CvfX2d9SDkQ5qOg10uS")

    embedded_tweets = co.embed(model="small", texts=user_tweets)
    user_average = [0 for dimension in embedded_tweets.embeddings[0]]

    for dimension in range(len(embedded_tweets.embeddings[0])):
        dimensional_sum = 0
        for vector in embedded_tweets.embeddings:
            dimensional_sum += vector[dimension]
        user_average[dimension] = dimensional_sum / len(embedded_tweets.embeddings)

    return user_average
