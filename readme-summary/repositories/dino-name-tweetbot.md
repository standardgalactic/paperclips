# dino-name-tweetbot

SUMMARY:
The dino-name-tweetbot is a Python project that generates new dinosaur names using data from Wikipedia's List of Dinosaur Genera. It employs a character-based recurrent neural network built with TensorFlow and Keras to produce realistic-sounding names. The model, stored in dino_model.h5, is trained on 1,648 existing dinosaur names scraped via BeautifulSoup. Generated names are filtered to ensure they differ sufficiently from real names (at least two edits away) using the stringdistance package. These names are then tweeted by @fakedinobot through the Twitter API using Tweepy. The README includes code examples for interacting with the model and generating names, as well as a discussion on how increasing `min_dist` affects name uniqueness and generation attempts.

KEYWORDS:
dino-name-tweetbot project, neural network, TensorFlow, Keras, recurrent neural network, character-based text generation, Wikipedia data scraping, stringdistance filtering, Twitter API integration, Tweepy library, machine learning application.
