def analyze(search_str):
    import tweepy
    import os
    from textblob import TextBlob

    api_key = os.environ.get('API_KEY')
    api_secret = os.environ.get('API_SECRET')

    access_token = os.environ.get('ACCESS_TOKEN')
    access_token_secret = os.environ.get('ACCESS_TOKEN_SECRET')

    auth = tweepy.OAuthHandler(api_key, api_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    tweets_to_search = 100
    public_tweets = api.search(q=search_str, count=tweets_to_search, result_type="Popular")
    sum = 0.0
    
    for i in range(tweets_to_search):
        try:
            analysis = TextBlob(public_tweets[i].text)
        except IndexError:
            return -2;
        sum = sum + float(analysis.sentiment.polarity)
    return sum/tweets_to_search