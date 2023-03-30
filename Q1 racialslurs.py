import re

racial_slurs = {'slur1', 'slur2', 'slur3'}

def calculate_profanity_score(tweet):
    # Split the tweet into individual words
    words = tweet.split()
    # Count the number of racial slurs in the tweet
    num_slurs = len([word for word in words if word.lower() in racial_slurs])
    # Calculate the profanity score as a percentage of the total number of words in the tweet
    score = 100 * num_slurs / len(words)
    return score

def main():
    # Read in the file of tweets
    with open('tweets.txt', 'r') as f:
        tweets = f.readlines()
    # Process each tweet and output the profanity score
    for tweet in tweets:
        score = calculate_profanity_score(tweet)
        print(f'Tweet: {tweet.strip()}')
        print(f'Profanity score: {score:.2f}%')
        print()

if __name__ == '__main__':
    main()
