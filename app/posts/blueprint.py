from flask import Blueprint, render_template, request, redirect, url_for

from app import db
from models import Post, Tag
from .forms import PostForm


posts = Blueprint(name='posts', import_name=__name__, template_folder='templates')


@posts.route('/create', methods=['POST', 'GET'])
def create_post():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']

        try:
            post = Post(title=title, body=body)
            db.session.add(post)
            db.session.commit()
        except Exception as e:
            print(e)
            print('Something wrong')
        return redirect(url_for('posts.index'))

    form = PostForm()
    return render_template('posts/create_post.html', form=form)


@posts.route('/')
def index():
    query = request.args.get('query')
    if query:
        posts = Post.query.filter(Post.title.contains(query) | Post.body.contains(query)).all()
    else:
        posts = Post.query.order_by(Post.created.desc())

    return render_template('posts/index.html', posts=posts)


@posts.route('/<slug>')
def post_detail(slug):
    post = Post.query.filter(Post.slug == slug).first()
    tags = post.tags
    return render_template('posts/post_detail.html', post=post, tags=tags)


@posts.route('/tag/<slug>')
def tag_detail(slug):
    tag = Tag.query.filter(Tag.slug == slug).first()
    posts = tag.posts.all()
    return render_template('posts/tag_detail.html', tag=tag, posts=posts)
