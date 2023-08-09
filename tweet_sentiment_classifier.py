# The intention of this code is to create a sentiment classifier for synthetic (fake, semi-randomly 
# generated) twitter data in a csv file named "project_twitter_data.csv" which has the text, number 
# of retweets and number of replies to that tweet. This sentiment classifier is based on some txt 
# files extracted from https://www.cs.uic.edu/~liub/FBS/sentiment-analysis.html which contain 
# negative and positive words. By counting the number of occurrences of words from those tweets and 
# in the list of sentoment words, we provide a graph of the Net Score vs Number of Retweets, for 
# data analysis.

import pandas as pd
import matplotlib.pyplot as plt


positive_words = [] # Empty list that will store words from a txt

# ISO-8859-1 or Latin_1 are 8 bit character sets
with open("positive_words.txt", "r", encoding="latin-1") as file:
    for i in file.readlines():  # .readlines can be omitted
        if i[0] != ';' and i[0] != '\n': # Avoid ; and \n because of the format of  the txt file
            positive_words.append(i.strip("\n"))


negative_words = [] # Empty list that will store words from a txt

# ISO-8859-1 or Latin_1 are 8 bit character sets
with open("negative_words.txt", "r", encoding="latin-1") as file:
    for i in file.readlines():  # .readlines can be omitted
        if i[0] != ';' and i[0] != '\n': # Avoid ; and \n because of the format of  the txt file
            negative_words.append(i.strip("\n"))


# Function that receives a word and deletes punctuation signs in it
def strip_punctuation(wrd):
    punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
    for i in wrd:
        if i in punctuation_chars:
            wrd = wrd.replace(i, "")
    return wrd


# Function that counts the number of occurrences of words that appear in a list provided
def word_count(words, words_list):
    count = 0
    for i in words.split():
        i = strip_punctuation(i.lower())
        if i in words_list:
            count += 1
    return count


def main():
    # Call for the file where raw data is stored
    with open("project_twitter_data.csv", "r", encoding="latin-1") as tweet:
        # Call for the file where new data is going to be stored
        with open("resulting_data.csv", "w+") as outfile:
            # First, define the headers of the new data frame
            outfile.write(
                "Number of Retweets,Number of Replies,Positive Score,Negative Score,Net Score\n")
            for row in tweet.readlines()[1:]:
                row = row.strip().split(",") # Remove "\n" characters and split by commas 
                (pos_wrds, neg_wrds) = (word_count(row[0], positive_words), word_count(
                    row[0], negative_words))
                # .format based on our defined headers
                new_row = "{},{},{},{},{}\n".format(int(row[1]), int(row[2]), pos_wrds, neg_wrds, pos_wrds - neg_wrds)
                outfile.write(new_row) # Write our new data into the data frame
    
    # Printing data created for comprobation and analysis
    with open("resulting_data.csv", "r") as tweet_analysis:
        for i in tweet_analysis.readlines()[1:]:
            i = i.strip().split(",")
            print("Retweets: {}. Replies: {}. Positive Score: {}. Negative Score: {}. Net Score: {}."
                  .format(i[0], i[1], i[2], i[3], i[4]))
    
    # Scatter plot generator
    data = pd.read_csv("resulting_data.csv")
    plt.scatter(data["Net Score"], data["Number of Retweets"], color="orange", alpha=0.6, s=60)
    plt.title("Number of Retweets vs Net Score", fontweight='bold')
    plt.xlabel("Net Score")
    plt.ylabel("Number of Retweets")
    plt.savefig('Retweets_vs_NetScore.png', dpi=300)
    plt.show()
    

if __name__ == "__main__":
    main()
