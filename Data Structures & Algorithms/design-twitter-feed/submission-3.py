class Twitter:

    class User:
        def __init__(self, userId):
            self.userId = userId
            self.tweets = []
            self.followers = set()
            self.following = set()
                 
    class Tweet:
        def __init__(self, tweetid, userId, time):
            self.tweetid = tweetid
            self.userId = userId
            self.time = time

    def __init__(self):
        self.twitter = {}
        self.clock = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.clock = self.clock + 1
        tweet = self.Tweet(tweetid = tweetId, userId = userId, time = self.clock)
        if(self.twitter.get(userId)):
            user = self.twitter.get(userId)
            user.tweets.append(tweet)
        else:
            user = self.User(userId = userId)
            user.tweets.append(tweet)
            self.twitter[user.userId] = user

    def getNewsFeed(self, userId: int) -> List[int]:
        tweets = []
        heapq.heapify(tweets)
        user = self.twitter.get(userId)
        for tweet in user.tweets:
            heapq.heappush(tweets, (-tweet.time, tweet))

        for friendId in user.following:
            friend = self.twitter.get(friendId)

            for tweet in friend.tweets:
                heapq.heappush(tweets, (-tweet.time, tweet))

        ans = []

        while tweets and len(ans) < 10:
            _, tweet = heapq.heappop(tweets)
            ans.append(tweet.tweetid)

        return ans




    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        if followerId not in self.twitter:
            self.twitter[followerId] = self.User(followerId)

        if followeeId not in self.twitter:
            self.twitter[followeeId] = self.User(followeeId)

        self.twitter[followerId].following.add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:

        followee = self.twitter.get(followeeId)
        user = self.twitter.get(followerId)

        if followee:
            followee.followers.discard(followerId)

        if user:
            user.following.discard(followeeId)
        
            
