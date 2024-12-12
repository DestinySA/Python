from flask import Flask, render_template
import requests
from post import Post

app = Flask(__name__)

blog_endpoint = "https://api.npoint.io/c790b4d5cab58020d391"
response = requests.get(blog_endpoint)
posts = response.json()
# posts = []
# for item in data:
#     posts.append(Post(item["id"], item["body"], item["title"], item["subtitle"]))

@app.route('/')
def home():
    return render_template("index.html", posts=posts)

@app.route('/post/<int:blog_id>')
def get_post(blog_id):
    post = next(post for post in posts if post["id"] == blog_id)
    return render_template("post.html", post=post)

if __name__ == "__main__":
    app.run(debug=True)
