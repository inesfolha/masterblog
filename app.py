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
            'content': content
        }
        blog_posts.append(new_post)

        file_handler.save_file('blog_posts.json', blog_posts)

        return redirect(url_for('index'))
    return render_template('add.html')

@app.route('/delete/<string:id>', methods=['GET', 'POST'])
def delete(id):
    blog_posts = file_handler.load_file('blog_posts.json')
    post_to_delete = None
    for post in blog_posts:
        if post['id'] == id:
            post_to_delete = post
            break

    if post_to_delete:
        blog_posts.remove(post_to_delete)
        file_handler.save_file('blog_posts.json', blog_posts)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()
