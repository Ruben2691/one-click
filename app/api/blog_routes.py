from flask import Blueprint, jsonify, request
from app.models.blog_post import BlogPost

blog_routes = Blueprint("blog", __name__)

# get all blog posts
@blog_routes.route("/")
def get_all_blog_posts():
    blog_posts = BlogPost.query.all()
    return {"blog_posts": [blog_post.to_dict() for blog_post in blog_posts]}

# get specific blog post
@blog_routes.route("/<int:id>")
def get_blog_post(id):
    blog_post = BlogPost.query.get(id)
    return blog_post.to_dict()

# create new blog post admin only
@blog_routes.route("/", methods=["POST"])
def create_blog_post():
    data = request.json
    new_blog_post = BlogPost(
        title=data["title"],
        content=data["content"],
        author_id=data["author_id"]
    )
    new_blog_post.save()
    return new_blog_post.to_dict()

# update blog post admin only
@blog_routes.route("/<int:id>", methods=["PUT"])
def update_blog_post(id):
    data = request.json
    blog_post = BlogPost.query.get(id)
    blog_post.title = data["title"]
    blog_post.content = data["content"]
    blog_post.save()
    return blog_post.to_dict()

# delete blog post admin only
@blog_routes.route("/<int:id>", methods=["DELETE"])
def delete_blog_post(id):
    blog_post = BlogPost.query.get(id)
    blog_post.delete()
    return {"message": "Blog post deleted successfully"}


