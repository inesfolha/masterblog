from flask import Flask, render_template, request, redirect, url_for
import json
from masterblog.static import file_handler

app = Flask(__name__)


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
        new_post = {
            'author': author,
            'title': title,
            'content': content
        }
        blog_posts.append(new_post)

        file_handler.save_file('blog_posts.json', blog_posts)

        return redirect(url_for('index'))
    return render_template('add.html')


if __name__ == '__main__':
    app.run()
