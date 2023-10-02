# MasterBlog

## Table of Contents
1. [Introduction](#introduction)
2. [Description](#description)
    - [Methods](#functionality)
3. [Installation](#installation)
   - [Prerequisites](#prerequisites)
   - [Installation Steps](#installation-steps)
4. [Usage](#usage)
5. [Limitations](#limitations)

<div id="top"></div>

## Introduction                                     
Welcome to MasterBlog, a simple web app to create, read, update and delete blog posts (CRUD).

This project was developed as a training exercise after my first deep dive into the Flask framework. 

MasterBlog uses a simple JSON file as storage for all blog posts data and allows you to add new posts, update existing ones and deleting any unwanted post via our customized user interface. You can also add likes to any post without any limitations.

The user interface is entirely built using HTML and css and the rest o relies entirely on python and the Flask framework. 

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

### Usage
 * [Watch Demo](https://www.youtube.com/watch?v=YFz7mqcHktY)


### Limitations

* There is no user authentication, so you can add, delete and update any post without any restrictions as well as place an unlimited amount of likes in each post.


* Since the data is stored in a simple json file, there may be some scalability issues. since JSON files are not well-suited for handling large amounts of data. As the app's data grows, reading and writing to a single JSON file can become slow and inefficient. 

[Back to the Top](#top)

