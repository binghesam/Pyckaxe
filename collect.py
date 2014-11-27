import os
import sys
import json
import argparse
from auth import auth
from databasehandler import CollectionDatabase
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener

DATABASE_PATH = os.path.join(os.path.dirname(__file__), 'database/')

auth = auth('credentials.csv')

consumer_key = auth['consumer_key']
consumer_secret = auth['consumer_secret']

access_token = auth['access_token']
access_token_secret = auth['access_secret']


class CollectListener(StreamListener):
    def __init__(self, db):
        super(CollectListener, self).__init__()
        self.db_path = db
        self.db = CollectionDatabase(self.db_path)

    def on_data(self, data):
        # Collecting id, favorite count, retweet number, text, coordinates, and
        # user.
        try:
            data = json.loads(data.strip())
            id = data['id_str']
            fav_count = data['favorite_count']
            retweets = data['retweet_count']
            text = data['text'].strip()
            coords = str(data['coordinates'])
            user = data['user']
            self.db.add([id, fav_count, retweets, text, coords])

            sys.stdout.write('\rTweets collected: %s -- database size: %s kb' %
                                (self.db.entry_count,
                                 os.path.getsize(self.db_path) >> 10))
            sys.stdout.flush()

        except KeyboardInterrupt:
            print '\nDisconnecting from database...'
            self.db.disconnect_db()
            print 'Done.'
            raise

        except KeyError, ke:
            pass

        except Exception, e:
            raise

    def on_error(self, error):
        pass


def collect():
    parser = argparse.ArgumentParser()
    parser.add_argument('--database', help='Provide a database name.')

    parser.add_argument('terms', nargs='+',
                        help='Collect tweets containing the provided term(s).')

    args = parser.parse_args()

    if not args.database:
        args.database = raw_input('Please provide a database name: ')

    db = os.path.join(DATABASE_PATH, args.database)

    listener = CollectListener(db)
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, listener)
    stream.filter(track=args.terms)


if __name__ == '__main__':
    try:
        runtime = collect()
    except KeyboardInterrupt:
        print 'Exiting.'