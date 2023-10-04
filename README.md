# MasterBlog
<p id="top"></p>

## Table of Contents
1. [Introduction](#introduction)
2. [Description](#description)
    - [Methods](#functionality)
3. [Installation](#installation)
   - [Prerequisites](#prerequisites)
   - [Installation Steps](#installation-steps)
4. [How does it work?](#how-does-it-work)
5. [Limitations](#limitations)
6. [Contributions](#contributions)



## Introduction                                     
Welcome to MasterBlog, a simple web app to create, read, update and delete blog posts (CRUD).

This project was developed as a training exercise after my first deep dive into the Flask framework. 

MasterBlog uses a simple [JSON](https://github.com/inesfolha/masterblog/blob/main/blog_posts.json) file as storage for all blog posts data and allows you to add new posts, update existing ones and deleting any unwanted post via our customized user interface. You can also add likes to any post without any limitations.

The user interface is entirely built using [HTML](https://github.com/inesfolha/masterblog/tree/main/templates) and [CSS](https://github.com/inesfolha/masterblog/blob/main/static/style.css) and the rest relies entirely on python and the Flask framework. 

This project utilizes HTML templates with Jinja2 templating to dynamically change and render information from Flask routes.

[Back to the Top](#top)

## Description


#### Functionality

| route                    |  method   |                       use                       |
|--------------------------|:---------:|:-----------------------------------------------:|
| /                        |    GET    |      Renders the template with blog posts.      |
| /add                     | GET, POST |     Handles the addition of a new blog post     |
| /delete/<string:post_id> | GET, POST |      Handles the deletion of a blog post.       |
| /update/<string:post_id> | GET, POST |      Handles the updating of a blog post.       |
| /like/<string:post_id>   |   POST    | Handles the increment of likes for a blog post. |
| 404                      |    GET    | Renders the 404.html template in case of error  |

[Back to the Top](#top)
## Installation

### Prerequisites

- Python 3.x installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).
- Flask installed. 

### Installation Steps

1. Clone this repository or download the script file:

```bash
git clone https://github.com/inesfolha/masterblog.git 
```

If you downloaded a ZIP archive, extract its contents to a directory of your choice.

2. Change to the script's directory:

 ```bash
  cd app.py
```
3. To run the script, open your terminal and execute the following command:
```bash
python app.py
```

4. Open a browser tab on:
```bash
http://127.0.0.1:5000/
```

[Back to the Top](#top)

### How does it work?
 * [Watch Demo](https://www.youtube.com/watch?v=YFz7mqcHktY)


### Limitations

* There is no user authentication, so you can add, delete and update any post without any restrictions as well as place an unlimited amount of likes in each post.


* Since the data is stored in a simple json file, there may be some scalability issues. since JSON files are not well-suited for handling large amounts of data. As the app's data grows, reading and writing to a single JSON file can become slow and inefficient. 

[Back to the Top](#top)

## Contributions

Contributions to this project are welcome. If you'd like to contribute, please fork the repository, make your changes, and create a pull request.

[Back to the Top](#top)