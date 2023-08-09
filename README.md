# Twitter Sentiment Analysis

This Python script aims to create a sentiment classifier for synthetic (fake, semi-randomly generated) Twitter data stored in a CSV file named "project_twitter_data.csv". The code utilizes a list of positive and negative words obtained from external sources and performs sentiment analysis on the tweets. The primary goal is to generate a graph displaying the relationship between the Net Score (positive score minus negative score) and the number of retweets for data analysis.

## How it Works

1. **Data Loading**: The code reads the positive and negative words from separate text files ("positive_words.txt" and "negative_words.txt") and stores them in corresponding lists.

2. **Data Preprocessing**: The script defines functions to clean words from punctuation and to count occurrences of sentiment words within tweets.

3. **Sentiment Analysis**: The script reads the "project_twitter_data.csv" file, calculates the positive and negative scores for each tweet, and calculates the Net Score.

4. **Data Storage**: The new data is written to a CSV file named "resulting_data.csv" with headers: "Number of Retweets", "Number of Replies", "Positive Score", "Negative Score", and "Net Score".

5. **Data Display**: The script prints the newly created data for verification and analysis purposes.

6. **Data Visualization**: The script generates a scatter plot showing the relationship between the Net Score and the Number of Retweets using the Pandas library and Matplotlib. The plot is saved as "Retweets_vs_NetScore.png".

## How to Use

1. Place the CSV file containing synthetic Twitter data named "project_twitter_data.csv" in the script's directory.
2. Place the text files "positive_words.txt" and "negative_words.txt" in the same directory.
3. Install the required libraries: `pandas` and `matplotlib`.
4. Copy and paste the provided code into your Python environment.
5. Run the script.
6. Examine the printed sentiment analysis data and the generated scatter plot.

## Dependencies

- [Pandas](https://pandas.pydata.org/docs/getting_started/install.html)
- [Matplotlib](https://matplotlib.org/stable/users/installing.html)

## Resources

The sentiment analysis is based on external sources of positive and negative words. These words are stored in the "positive_words.txt" and "negative_words.txt" files.

Feel free to modify the code, experiment with different sentiment words, and analyze the generated scatter plot to draw insights about the relationship between sentiment scores and the popularity of Twitter posts!