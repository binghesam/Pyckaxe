Data mining using the Twitter Streaming API
===========================================

This project utilizes the [Twitter Streaming API](https://dev.twitter.com/streaming/overview)
and [Tweepy](http://www.tweepy.org/) to collect potentially large amounts of
tweets from the public stream and store them in a database.

Usage
-----

1. Create an application on Twitter and obtain your consumer/access tokens. (for
more information on creating a new application, see [here](https://dev.twitter.com/)).

2. Once you have obtained your tokens, place them in a CSV file,
"credentials.csv" with the following format:

   ```
   consumer_key,YOUR_CONSUMER_KEY_HERE
   consumer_secret,YOUR_CONSUMER_SECRET_HERE
   access_token,YOUR_ACCESS_TOKEN_HERE
   access_secret,YOUR_ACCESS_SECRET_HERE
   ```

   If you are using [Plotly][https://plot.ly/] for any data graphing, include
   the following lined in the "credentials.csv" file:

   ```
   plotly_username,YOUR_PLOTLY_USERNAME_HERE
   plotly_api_key,YOUR_PLOTLY_API_KEY_HERE
   ```

   *Warning: Keep your keys/tokens a secret!*

3. From the command line, run collect.py with the terms you wish to collect
   tweets about:
    ```
    python collect.py "YOUR SEARCH TERMS HERE"
    ```

4. Collect tweets for however long you wish. Tweets collected since running and
   database file size (in KB) will be shown at the command line.

5. Run one of the parsing scripts to parse/graph the data.


TODO
----

1. (Optional) Take collection time as argument
2. Script/function for clearing database.
3. Clean up directory structure.
