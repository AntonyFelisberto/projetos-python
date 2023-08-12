import praw
from datetime import datetime,timedelta

reddit = praw.Reddit(user_agent=True,client_id="ID_DO_CLIENT",client_secret="CLIENT_SECRET",username="NAME_USER",password="")
url = "https://www.reddit.com/r/ESTILOZAP/comments/15ikqxj/rel%C3%ADquia_kkkk/"
post = reddit.submission(url=url)
print(post.title)
print(post.selftext)

print(len(post.comments))
for comment in post.comments:
    print(comment.body)

posts_twenty_four_hours = []
def posts_in_last_24_hours():
    subreddit = reddit.subreddit("glassblowing") # is the title at the url example htttps://www.reddit.com/glassblowing
    with open("output.txt","w") as file:
        for post in subreddit.new():
            current_time = datetime.utcnow()
            post_time = datetime.utcfromtimestamp(post.created)
            print(current_time,post_time)

            delta_time = current_time - post_time
            print(delta_time)
            if delta_time <= timedelta(hours=24):
                posts_twenty_four_hours.append((post.title,post.selftext,post.created))
                print(post.title,post.selftext)
                file.write(f"{post.title}\n{post.selftext}\n\n")

    print(posts_twenty_four_hours)

def post_messages():
    subreddit = reddit.subreddit("glassblowing") 
    subreddit.validate_on_submit = True
    title = "my post"
    content = "hey my first post on"
    subreddit.submit(title=title,selftext=content)

def reply_messages():
    subreddit = reddit.subreddit("glassblowing")
    for posts in subreddit.new():
        current_time = datetime.utcnow()
        post_time = datetime.utcfromtimestamp(posts.created)
        delta_time = current_time - post_time
        if delta_time <= timedelta(hours=48):
            if "christmas" in posts.title.lower():
                print(posts.title)
                posts.reply("hey christmas here")
                for comment in posts.comments:
                    if "hey christmas here" in comment.body.lower():
                        comment.reply("yeah")
