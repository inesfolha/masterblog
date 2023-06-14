from flask import Flask, render_template, request, redirect, url_for
import uuid
from masterblog.static import file_handler

app = Flask(__name__)


def id_generator():
    return str(uuid.uuid4())


@app.route('/')
def index():
    blog_posts = file_handler.load_file('blog_posts.json')
    return render_template('index.html', posts=blog_posts)


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        author = request.form.get('author')
        title = request.form.get('title')
        content = request.form.get('content')
        blog_posts = file_handler.load_file('blog_posts.json')
        post_id = id_generator()
        new_post = {
            'id': post_id,
            'author': author,
            'title': title,
            'content': content,
            'likes': 0
        }
        blog_posts.append(new_post)

        file_handler.save_file('blog_posts.json', blog_posts)

        return redirect(url_for('index'))
    return render_template('add.html')


@app.route('/delete/<string:post_id>', methods=['GET', 'POST'])
def delete(post_id):
    blog_posts = file_handler.load_file('blog_posts.json')
    post_to_delete = None
    for post in blog_posts:
        if post['id'] == post_id:
            post_to_delete = post
            break

    if post_to_delete:
        blog_posts.remove(post_to_delete)
        file_handler.save_file('blog_posts.json', blog_posts)
    return redirect(url_for('index'))


@app.route('/update/<string:post_id>', methods=['GET', 'POST'])
def update(post_id):

    blog_posts = file_handler.load_file('blog_posts.json')
    post_to_update = None
    for post in blog_posts:
        if post['id'] == post_id:
            post_to_update = post
            break
    if post_to_update is None:
        return "Post not found", 404

    if request.method == 'POST':

        updated_author = request.form['author']
        updated_title = request.form['title']
        updated_content = request.form['content']

        post_to_update['author'] = updated_author
        post_to_update['title'] = updated_title
        post_to_update['content'] = updated_content

        file_handler.save_file('blog_posts.json', blog_posts)
        return redirect(url_for('index'))

    return render_template('update.html', post=post_to_update)


@app.route('/like/<string:post_id>', methods=['POST'])
def like(post_id):
    blog_posts = file_handler.load_file('blog_posts.json')
    for post in blog_posts:
        if post['id'] == post_id:
            if 'likes' in post:
                post['likes'] += 1
            else:
                post['likes'] = 1
            break
    file_handler.save_file('blog_posts.json', blog_posts)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()
