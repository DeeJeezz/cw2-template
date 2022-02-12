from typing import List

from flask import jsonify, Response

from app import app
from repository import Repository, Post


@app.route('/')
def index() -> Response:
    repo: Repository = app.config['repository']

    posts: List[Post] = repo.get_posts_all()

    return jsonify(posts)
