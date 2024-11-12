# Meeple-Matchmaker
A board game recommendation system! 

# The Goal
Provide a hybrid recommendation system that using both **collaborative** and **content-based** recommendations for individual users and groups of users to find the ideal game to play during board game night. 

### Collaborative Filtering
Done Via Surprise

### Content-Based Filtering 
Content based recommendation systems provide users with items with similar features to those they already enjoy. 

#### Using Jaccard Similarity

To determine if a game is **similar** to one a user enjoys, we are using **Jaccard Similarity.**
```
Jaccard Similarity = (number of observations in both sets) / (number in either set)
```
Developed by Paul Jaccard, the Jaccard Similarity returns a value between 0 to 1. The closer to 1, the more similar the two sets of data.

### The Influencer 
In addition to these personalized recommendations, there is a secret agent at play. When a user is recommended a product that is on our 'influencer' list, that product is highlighted to encourage the user to check it out. 

## End Formula


# The Results 

# The Data 

[BoardGameGeek](https://boardgamegeek.com/) (BGG) is a game database with over 125,600 different tabletop games, including European-style board games, wargames, and card games. In addition to the game database, the site allows users to rate games on a 1–10 scale and publishes a ranked list of board games, as rated by the users. 

The dataset being used for this project is from [kaggle](https://www.kaggle.com/datasets/threnjen/board-games-database-from-boardgamegeek), sourced from the BGG API. 

Add graphs here / Tell The Story 

Strengths: 

Limitations: 
- The game descriptions have been pre-processed in a way that has left a lot of bogus words in the corpus. 


# Appendices 
## K-NN
- 
## NLP
- 



