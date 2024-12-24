import requests

# fetch posts
def fetch_posts(subreddit, sort="hot", limit=10):
    url = f"https://www.reddit.com/r/{subreddit}/{sort}.json?limit={limit}"
    headers = {"User-Agent": "Anonymous User Script"}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None

#fetch comments
def fetch_comments(permalink):
    comments_url = f"https://www.reddit.com{permalink}.json"
    headers = {"User-Agent": "Anonymous User Script"}
    response = requests.get(comments_url, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching comments: {response.status_code}")
        return None

subreddit = "IOENepal"
data = fetch_posts(subreddit, sort="new", limit=25)

posts_data = []

if data:
    for post in data["data"]["children"]:
        post_data = post["data"]
        post_info = {
            "title": post_data['title'],
            "description": post_data.get('selftext', '')[:200],
            "url": post_data['url'],
            "comments": []
        }
        
        # Fetch top comments
        comments_data = fetch_comments(post_data["permalink"])
        if comments_data:
            for comment in comments_data[1]["data"]["children"]:
                if "body" in comment["data"]:
                    post_info["comments"].append(comment["data"]["body"])
        
        posts_data.append(post_info)

print(posts_data)