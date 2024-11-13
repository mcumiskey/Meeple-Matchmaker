# Meeple Matchmaker
## A board game recommendation system! 

![Shelves of Board Games](https://images.unsplash.com/photo-1719494206741-79831f9f4d51?w=900&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTIyfHxib2FyZCUyMGdhbWVzfGVufDB8fDB8fHww)

# The Goal
Provide a hybrid recommendation system that using both **collaborative** and **content-based** recommendations for individual users and groups of users to find the ideal game to play during board game night. 

buy-in: This could be useful for board 

# The Data 

[BoardGameGeek](https://boardgamegeek.com/) (BGG) is a game database with over 125,600 different tabletop games, including European-style board games, wargames, and card games. In addition to the game database, the site allows users to rate games on a 1–10 scale and publishes a ranked list of board games, as rated by the users. 

The dataset being used for this project is from [kaggle](https://www.kaggle.com/datasets/threnjen/board-games-database-from-boardgamegeek), sourced from the BGG API. 

**Add graphs here / Tell The Story**
- Key Features (Rating theme mechanics)
- Highest Rated
- Avg. Ratings per User 
- Common Themes / Mechanics


Strengths:
- Wide variety of games & features 

Limitations: 
- The game descriptions have been pre-processed in a way that has left a lot of bogus words (ie 'aaaaaaaaa' and 'zeeegeme') in the corpus. 
- VERY wide (over 300 features)
- Analysis from 1960 to 2021 

# The Process 
![](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fmiro.medium.com%2Fmax%2F1064%2F1*mz9tzP1LjPBhmiWXeHyQkQ.png&f=1&nofb=1&ipt=ade22d99e80603cf66b316c3ff0d6ebee32347cfbea21eec5e049cf044431b97&ipo=images)
add source 
### Collaborative Filtering
Collaborative filtering is a recommendation technique that predicts a user's preferences based on the past interactions of similar users. It leverages user-item ratings to identify patterns and make personalized recommendations without requiring explicit knowledge of the items themselves. 

The Surprise library is a Python library built specifically for building and evaluating recommendation systems, particularly for collaborative filtering.

### Content-Based Filtering 
Content-based filtering is a recommendation technique that suggests items to users based on the attributes of the items and the user's past preferences. It analyzes features such as keywords, genres, or other item characteristics to recommend similar items to those the user has interacted with previously.

#### Using Jaccard Similarity

Board Game similarity was determined via  **Jaccard Similarity** between the themes and mechanics. 

```
Jaccard Similarity = (number of observations in both sets) / (number in either set)
```
Developed by Paul Jaccard, the Jaccard Similarity returns a value between 0 to 1. The closer to 1, the more similar the two sets of data.

### The Influencer 
In addition to these personalized recommendations, there is a secret agent at play. When a user is recommended a product that is on our 'influencer' list, that product is highlighted to encourage the user to check it out. 


# Hybrid function: Combine collaborative and content-based scores

The Alpha represents the 'Weight' of the collaborative score. 

```
        score = alpha * collaborative_score + (1 - alpha) * content_based_score
```

# The Results 
![Meeple Circus](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.boardgamequest.com%2Fwp-content%2Fuploads%2F2017%2F12%2FMeeple-Circus-Game-Experience.jpg&f=1&nofb=1&ipt=827b94c331489562e5ca20b0953e612c8d9927a2b4c81cc08c7e4446a4beca49&ipo=images)

ADD ONCE IN
## Users 


# Appendices 
## [EDA](Appendices/EDA.ipynb) 
Dove deeper into the different features 
View [here](Appendices/EDA.ipynb)

## [K-NN](Appendices/KNN-and-Pyspark.ipynb)
K-Nearest Neighbors (KNN) is a machine learning algorithm used for classification and regression, which makes predictions based on the closest training examples in the feature space. In classification, KNN assigns a class to a data point by finding the "K" nearest points and choosing the most frequent class among them, while in regression, it predicts the average of the values of the K nearest neighbors

Created neighbors for predictions [here](Appendices/KNN-and-Pyspark.ipynb)

## [NLP](Appendices/NLP.ipynb) 
Natural Language Processing (NLP) for classification involves using algorithms to automatically analyze and categorize text data into predefined categories or labels. This typically involves preprocessing text (e.g., tokenization, stemming, removing stop words), converting it into numerical representations (such as TF-IDF, word embeddings, or bag-of-words), and then training a machine learning model (like Naive Bayes, SVM, or deep learning models) to predict the category of a given text based on its content. 

Attempted to categorize similar games [here](Appendices/NLP.ipynb) 


