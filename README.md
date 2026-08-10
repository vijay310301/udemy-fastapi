# Udemy - Fast API course notes

# Section 3 - FastAPI Overview

## What is FastAPI?

**FastAPI** is a modern, high-performance **Python web framework** used for building RESTful APIs.

A web framework provides a structured way to build web applications by handling common tasks such as:

- URL routing
- Request handling
- Response generation
- Data validation
- Serialization
- Security
- Documentation

FastAPI is designed to make API development:

- Simple
- Fast
- Scalable
- Extensible
- Production-ready

---

# Why is it called "FastAPI"?

The word **Fast** has two meanings.

## 1. Fast Performance

FastAPI is one of the fastest Python web frameworks available.

It provides:

- Excellent runtime performance
- High request throughput
- Low latency

In addition to speed, FastAPI also includes several built-in features:

- Automatic data validation
- Serialization
- Interactive API documentation
- Type checking
- Security support

---

## 2. Fast Development

FastAPI allows developers to build APIs with very little code.

Instead of writing repetitive boilerplate code, FastAPI handles many common tasks automatically, allowing developers to focus on business logic.

Benefits include:

- Less code
- Faster development
- Easier maintenance
- Faster deployment

---

# Why Use FastAPI?

FastAPI solves many common problems involved in API development.

Instead of implementing everything manually, FastAPI provides built-in support for:

- Request parsing
- Data validation
- Response serialization
- API documentation
- Error handling
- Security features

This allows developers to avoid "reinventing the wheel."

---

# Key Features of FastAPI

## ✅ High Performance

- One of the fastest Python web frameworks
- Suitable for production applications
- Handles high traffic efficiently

---

## ✅ Automatic Data Validation

FastAPI validates incoming request data automatically using Python type hints.

Benefits:

- Fewer bugs
- Reduced human errors
- Cleaner code
- More reliable APIs

The course mentions that this can reduce development bugs by **around 40%**.

---

## ✅ Automatic API Documentation

FastAPI automatically generates interactive API documentation.

Benefits:

- No manual documentation required
- Easy API testing
- Always stays synchronized with the code

---

## ✅ Developer Friendly

FastAPI was designed to improve the developer experience.

It is:

- Easy to learn
- Easy to write
- Easy to maintain

This allows developers to spend more time building features instead of writing infrastructure code.

---

## ✅ Lightweight Installation

FastAPI requires minimal setup.

A basic API can be created and run within minutes.

---

## ✅ Strong Community

FastAPI has an active community and excellent official documentation.

This makes learning, troubleshooting, and finding examples much easier.

---

## ✅ Industry Standards

FastAPI follows modern API standards such as:

- OpenAPI Specification
- JSON Schema

This improves compatibility with tools and makes APIs easier to integrate.

---

# What is a RESTful API?

A **RESTful API** allows applications to communicate over HTTP using standard methods such as:

- GET
- POST
- PUT
- PATCH
- DELETE

FastAPI is primarily designed for building RESTful APIs.

---

# Where Does FastAPI Fit in an Application?

```text
+----------------+
|   Web Browser  |
+----------------+
        |
        | HTTP Request
        ▼
+----------------------+
|     FastAPI Server   |
|----------------------|
| Business Logic       |
| Validation           |
| Authentication       |
| Database Operations  |
+----------------------+
        |
        ▼
+----------------+
|   Database     |
+----------------+
```

### Flow

1. User interacts with a web page.
2. The web page sends an HTTP request.
3. FastAPI receives the request.
4. FastAPI executes business logic.
5. FastAPI communicates with the database or other services.
6. FastAPI returns a response.
7. The web page displays the result to the user.

---

# Business Logic

Business logic refers to the application's core functionality.

Examples:

- User authentication
- Order processing
- Payment validation
- Inventory management
- Permission checking

FastAPI is responsible for executing this logic before returning data to the client.

---

# Can FastAPI Build Full-Stack Applications?

Yes.

FastAPI can be used in two ways:

## Backend API

- Exposes REST APIs
- Communicates with frontend applications
- Returns JSON responses

## Full-Stack Application

FastAPI can also render HTML pages and work with templating engines, allowing it to serve both the frontend and backend.

---

# Companies Using FastAPI

Some well-known companies using FastAPI include:

- Netflix
- Uber
- Microsoft

This demonstrates that FastAPI is suitable for large-scale, production-grade applications.

---

# Why Use a Web Framework Instead of Writing Everything Yourself?

Although it is technically possible to build everything manually, using a web framework offers many advantages.

### Without a Framework

You would need to implement:

- URL routing
- Request parsing
- Response formatting
- Validation
- Authentication
- Documentation
- Error handling
- Security

### With FastAPI

Most of these features are already provided, allowing developers to focus on solving business problems rather than infrastructure.

---

# Advantages of FastAPI

- High performance
- Minimal boilerplate code
- Automatic validation
- Automatic documentation
- Easy to learn
- Scalable architecture
- Strong community support
- Production-ready
- Built on modern API standards

---

# Interview Notes

### What is FastAPI?

FastAPI is a modern, high-performance Python web framework used to build RESTful APIs quickly and efficiently.

---

### Why is FastAPI called "Fast"?

It is "fast" because:

1. It offers excellent runtime performance.
2. It enables rapid API development with minimal code.

---

### What problems does FastAPI solve?

- Automatic validation
- Serialization
- Documentation
- Security
- Faster API development
- Reduced boilerplate code

---

### What standards does FastAPI follow?

- OpenAPI Specification
- JSON Schema

---

### What is FastAPI mainly responsible for?

FastAPI acts as the backend server that:

- Processes HTTP requests
- Executes business logic
- Interacts with databases
- Returns responses to clients

---

# Summary

FastAPI is a modern Python web framework focused on building RESTful APIs quickly and efficiently. It combines excellent runtime performance with a developer-friendly design by providing built-in features such as automatic validation, documentation, serialization, and security. Following industry standards like OpenAPI and JSON Schema, FastAPI simplifies backend development while remaining suitable for scalable, production-ready applications.

---

# Key Takeaways

- FastAPI is a Python web framework for building REST APIs.
- "Fast" refers to both runtime performance and development speed.
- Automatic data validation reduces bugs and improves reliability.
- Interactive API documentation is generated automatically.
- FastAPI follows OpenAPI and JSON Schema standards.
- It manages backend business logic and communicates with databases.
- It can be used for both REST APIs and full-stack web applications.
- Large organizations such as Netflix, Uber, and Microsoft use FastAPI.
- FastAPI eliminates repetitive boilerplate code, allowing developers to focus on application logic.

# Section 4 - FastAPI Setup and Installation

# Virtual Environments

## What is a Virtual Environment?

A **virtual environment** is an isolated Python environment created for a specific project.

Each virtual environment has its own:

- Installed packages
- Dependency versions
- Python configuration

This isolation ensures that one project's dependencies do not interfere with another project's dependencies.

---

# Why Do We Need Virtual Environments?

Different Python projects often require different libraries and package versions.

For example:

| Project                  | Example Dependencies           |
| ------------------------ | ------------------------------ |
| FastAPI Application      | `fastapi`, `uvicorn`           |
| Artificial Intelligence  | `tensorflow`, `torch`, `numpy` |
| Internet of Things (IoT) | `gpiozero`, `paho-mqtt`        |

Installing all dependencies globally can lead to:

- Package version conflicts
- Unnecessary packages in unrelated projects
- Difficult maintenance

A virtual environment isolates each project's dependencies, ensuring they remain independent.

---

# Dependency Version Isolation

Even two FastAPI projects may require different versions of the same package.

| Project   | FastAPI Version |
| --------- | --------------- |
| Project A | `0.95`          |
| Project B | `0.115`         |

With virtual environments:

- Each project maintains its own dependency versions.
- Upgrading packages in one project does not affect another.

---

# Benefits of Virtual Environments

- Isolates project dependencies
- Prevents package version conflicts
- Keeps the global Python installation clean
- Makes projects easier to maintain
- Simplifies deployment by using project-specific dependencies

---

# Python Package Manager (pip)

## What is pip?

**pip** is Python's official package manager used to install and manage third-party packages.

Common tasks include:

- Installing packages
- Upgrading packages
- Uninstalling packages
- Managing project dependencies

Examples of Python packages:

- FastAPI
- Uvicorn
- NumPy
- Pandas
- Requests

---

## Checking the pip Version

It is recommended to keep `pip` reasonably up to date.

### macOS / Linux

```bash
python3 -m pip --version
```

### Windows

```bash
python -m pip --version
```

> **Note:** `pip` is installed automatically when Python is installed.

---

# Creating a FastAPI Project

A typical FastAPI project setup consists of the following steps.

## Step 1: Create a Project Directory

Create a new folder for your project.

```text
FastAPI/
```

This directory will contain your application code and project dependencies.

---

## Step 2: Create a Virtual Environment

Python provides a built-in module called **`venv`** to create virtual environments.

No external package is required.

Project structure:

```text
FastAPI/
│
├── venv/
└── application files
```

---

## Step 3: Activate the Virtual Environment

Activate the virtual environment before installing any packages.

Once activated:

- Installed packages are available only within this project.
- Other Python projects remain unaffected.

---

## Step 4: Install Project Dependencies

After activating the virtual environment, install the required packages.

Typical dependencies include:

- FastAPI
- Uvicorn
- Additional libraries required by the project

---

# What is Uvicorn?

**Uvicorn** is an **ASGI (Asynchronous Server Gateway Interface) server** used to run FastAPI applications.

Its responsibilities include:

- Starting the FastAPI application
- Receiving HTTP requests
- Returning HTTP responses

> **Note:** FastAPI defines the application, while Uvicorn runs and serves it.

---

# FastAPI Project Setup Workflow

```text
Create Project Folder
        │
        ▼
Create Virtual Environment
        │
        ▼
Activate Virtual Environment
        │
        ▼
Install FastAPI
        │
        ▼
Install Uvicorn
        │
        ▼
Install Additional Dependencies
        │
        ▼
Start Building the Application
```

---

# Key Concepts

## Virtual Environment

An isolated Python environment dedicated to a single project.

---

## Dependency

A third-party library required by an application.

Examples:

- FastAPI
- Uvicorn
- SQLAlchemy
- Pydantic

---

## pip

Python's package manager used to install, update, and remove packages.

---

## venv

Python's built-in module used to create virtual environments.

---

# Best Practices

- Create a separate virtual environment for every Python project.
- Always activate the virtual environment before installing packages.
- Avoid installing project-specific packages globally.
- Keep `pip` reasonably up to date.
- Install only the dependencies required for the current project.

---

# Summary

A virtual environment provides an isolated Python environment for each project, preventing dependency conflicts and allowing different projects to use different package versions independently. Python's built-in `venv` module is used to create virtual environments, while `pip` is used to manage project dependencies. After creating and activating the virtual environment, packages such as **FastAPI** and **Uvicorn** can be installed to begin developing FastAPI applications.

---

# Key Takeaways

- A virtual environment isolates project dependencies from other Python projects.
- Each Python project should have its own virtual environment.
- `pip` is Python's package manager used to install and manage libraries.
- `venv` is the built-in module used to create virtual environments.
- FastAPI applications typically require **FastAPI** and **Uvicorn**.
- Activate the virtual environment before installing project dependencies.
- Using isolated environments improves maintainability and avoids dependency conflicts.

# Section 4 - Creating a FastAPI Virtual Environment (Windows)

## Overview

Before developing a FastAPI application, it is recommended to create a **virtual environment**. A virtual environment isolates the project's dependencies from the global Python installation, ensuring that packages installed for one project do not affect others.

This guide demonstrates how to create, activate, and manage a virtual environment on **Windows**.

---

# Step 1: View Globally Installed Packages

Before creating a virtual environment, you can view the packages installed globally on your machine.

```bash
pip list
```

This displays all packages installed in the global Python environment.

> **Observation:** Before installing FastAPI, packages like `fastapi` and `uvicorn` should not appear in the global package list (unless previously installed globally).

---

# Step 2: Create a Project Directory

Navigate to the location where you want to create your project.

Example:

```bash
cd Documents
```

Create a new project folder:

```bash
mkdir FastAPI
```

Move into the project directory:

```bash
cd FastAPI
```

Verify the directory contents:

```bash
dir
```

Initially, the directory will be empty.

---

# Step 3: Create a Virtual Environment

Python provides the built-in **`venv`** module for creating virtual environments.

Command:

```bash
python -m venv fastapi-env
```

### Command Breakdown

| Part          | Description                                       |
| ------------- | ------------------------------------------------- |
| `python`      | Runs the Python interpreter                       |
| `-m`          | Executes a Python module                          |
| `venv`        | Built-in module for creating virtual environments |
| `fastapi-env` | Name of the virtual environment folder            |

> **Note:** The virtual environment name can be anything. Using a descriptive name such as `fastapi-env` makes its purpose clear.

After creation, verify that the folder exists:

```bash
dir
```

Example structure:

```text
FastAPI/
│
└── fastapi-env/
```

---

# Step 4: Activate the Virtual Environment

Activate the virtual environment before installing any dependencies.

On **Windows (Command Prompt):**

```bash
fastapi-env\Scripts\activate.bat
```

Once activated, the command prompt changes to:

```text
(fastapi-env) C:\Users\...\FastAPI>
```

The environment name in parentheses indicates that the virtual environment is currently active.

---

# Step 5: Verify the Virtual Environment

Check the installed packages:

```bash
pip list
```

A newly created virtual environment contains only a few default packages, such as:

- `pip`
- `setuptools` (depending on the Python version)

Notice that **FastAPI** and **Uvicorn** are not installed yet.

---

# Step 6: Install FastAPI

Install FastAPI using pip.

```bash
pip install fastapi
```

This installs FastAPI and its required dependencies inside the virtual environment.

---

# Step 7: Install Uvicorn

Install Uvicorn with the standard optional dependencies.

```bash
pip install "uvicorn[standard]"
```

### Why `standard`?

The `standard` extra installs additional packages that improve the development experience, such as:

- Better performance
- Automatic reload support
- Additional networking features

---

# Step 8: Verify Installed Packages

Run:

```bash
pip list
```

You should now see packages including:

- FastAPI
- Uvicorn
- Pydantic
- Starlette
- Other dependencies installed automatically

---

# Step 9: Deactivate the Virtual Environment

When you finish working on the project, deactivate the virtual environment.

```bash
deactivate
```

The environment name disappears from the command prompt, indicating that you have returned to the global Python environment.

---

# Step 10: Verify the Global Environment

Run:

```bash
pip list
```

Since FastAPI was installed only inside the virtual environment, it will not appear in the global package list (unless it was installed globally earlier).

This demonstrates that the project dependencies are isolated from the system-wide Python installation.

---

# Complete Workflow

```text
Create Project Folder
        │
        ▼
Navigate to Project
        │
        ▼
Create Virtual Environment
        │
        ▼
Activate Virtual Environment
        │
        ▼
Verify Installed Packages
        │
        ▼
Install FastAPI
        │
        ▼
Install Uvicorn
        │
        ▼
Verify Installation
        │
        ▼
Develop Your Application
        │
        ▼
Deactivate Environment
```

---

# Common Commands

| Purpose                        | Command                            |
| ------------------------------ | ---------------------------------- |
| List installed packages        | `pip list`                         |
| Create project folder          | `mkdir FastAPI`                    |
| Change directory               | `cd FastAPI`                       |
| Show directory contents        | `dir`                              |
| Create virtual environment     | `python -m venv fastapi-env`       |
| Activate virtual environment   | `fastapi-env\Scripts\activate.bat` |
| Install FastAPI                | `pip install fastapi`              |
| Install Uvicorn                | `pip install "uvicorn[standard]"`  |
| Deactivate virtual environment | `deactivate`                       |

---

# Notes

- Always create a virtual environment before starting a new Python project.
- Activate the virtual environment before installing dependencies.
- Install project-specific packages inside the virtual environment instead of globally.
- Use descriptive names for virtual environments (e.g., `fastapi-env`, `venv`).
- Deactivate the environment when you are finished working on the project.

---

# Summary

Creating a virtual environment is one of the first steps in setting up a FastAPI project. The `venv` module creates an isolated environment where project-specific packages such as **FastAPI** and **Uvicorn** can be installed without affecting the global Python installation. Activating the environment ensures all package installations remain local to the project, while deactivating it returns you to the global Python environment.

Creating a FastAPI Virtual Environment (Windows)

# Section 5 - FastAPI Request Method Logic

# Books Project Introduction

## Project Overview

The **Books Project** is the first practical project used to learn the fundamentals of FastAPI and HTTP request methods.

The project will start with a simple collection of books and gradually implement the basic operations required to manage them.

The main goal is to understand how FastAPI handles:

- HTTP requests
- HTTP responses
- CRUD operations
- Request methods
- Retrieving data
- Creating data
- Updating data
- Deleting data

---

# Books Data

The application will contain a list of books.

Each book will contain key-value pairs such as:

```text
title
author
category
```

Example:

```python
books = [
    {
        "title": "Title 1",
        "author": "Author 1",
        "category": "science"
    },
    {
        "title": "Title 2",
        "author": "Author 2",
        "category": "history"
    },
    {
        "title": "Title 3",
        "author": "Author 3",
        "category": "math"
    }
]
```

The example project will contain books with titles and authors numbered from `1` to `5`, along with categories such as:

- Science
- History
- Math

---

# CRUD Operations

The application will use **CRUD operations** to manage books.

CRUD stands for:

| Operation | Meaning                 |
| --------- | ----------------------- |
| Create    | Add a new book          |
| Read      | Retrieve existing books |
| Update    | Modify an existing book |
| Delete    | Remove a book           |

These operations form the basic functionality of many backend applications.

---

## Create

Create is used to add a new book to the collection.

Example:

```text
Create Book
     │
     ▼
Add new book to books list
```

---

## Read

Read is used to retrieve information.

Examples:

- Get all books
- Get a specific book
- Get books belonging to a category

---

## Update

Update is used to modify an existing book.

For example:

```text
Title 1
Author 1
Science
```

could be updated to:

```text
Title 1
Author 10
Science
```

---

## Delete

Delete removes a book from the collection.

```text
Book
 │
 ▼
Delete
 │
 ▼
Book removed from collection
```

---

# Request and Response

A fundamental concept in API development is **request and response**.

The communication generally looks like this:

```text
+-------------+                     +----------------+
|             |      Request        |                |
| Web Client  | ------------------> | FastAPI Server |
|             |                     |                |
|             |      Response       |                |
|             | <------------------ |                |
+-------------+                     +----------------+
```

### Request

The client sends a **request** to the FastAPI server.

The request tells the server what operation the client wants to perform.

For example:

```text
"Give me book 2"
```

### Response

FastAPI processes the request and sends a **response** back to the client.

Example:

```json
{
  "title": "Title 2",
  "author": "Author 2",
  "category": "history"
}
```

---

# HTTP Request Methods

Clients communicate their intended operation to the server using **HTTP request methods**, also commonly called HTTP verbs.

HTTP methods describe what type of operation the client wants to perform.

The basic methods used in this project are:

| CRUD Operation | HTTP Method |
| -------------- | ----------- |
| Create         | `POST`      |
| Read           | `GET`       |
| Update         | `PUT`       |
| Delete         | `DELETE`    |

---

# CRUD to HTTP Method Mapping

```text
CRUD Operation       HTTP Method

Create       ───────► POST
Read         ───────► GET
Update       ───────► PUT
Delete       ───────► DELETE
```

This mapping is a useful way to understand how REST APIs represent common data operations.

---

# GET Request

The first HTTP method covered in the project is **GET**.

`GET` is used to retrieve information from the server.

For example:

```text
Client
  │
  │ GET /books
  ▼
FastAPI
  │
  │ Returns books
  ▼
Client
```

A GET request should generally be used for reading data rather than modifying data.

---

# Swagger UI

FastAPI automatically provides interactive API documentation using **Swagger UI**.

Swagger UI allows developers to:

- View available API endpoints
- See HTTP request methods
- Understand the API structure
- Send requests directly from the browser
- Inspect API responses

When running a FastAPI application locally, Swagger UI is available at:

```text
/docs
```

For example:

```text
http://127.0.0.1:8000/docs
```

The exact host and port may vary depending on how the FastAPI application is started.

---

# Why Swagger UI is Useful

Instead of manually creating requests using tools such as Postman or `curl`, Swagger UI provides a browser-based interface for interacting with the API.

For example, after creating:

```http
GET /books
```

Swagger UI can display the endpoint and allow you to execute the request directly.

The response can then be inspected immediately.

---

# Books Project Learning Path

The project will progressively implement the CRUD operations.

```text
Books Application
       │
       ├── GET
       │    └── Read books
       │
       ├── POST
       │    └── Create books
       │
       ├── PUT
       │    └── Update books
       │
       └── DELETE
            └── Delete books
```

The first implementation will focus on the **GET request** and retrieving book information from the FastAPI application.

---

# Key Concepts

## API Request

A message sent by a client to a server asking it to perform an operation or provide information.

---

## API Response

The result returned by the server after processing a request.

---

## HTTP Method

An HTTP method specifies the intended operation of a request.

Common methods include:

- `GET`
- `POST`
- `PUT`
- `DELETE`

---

## CRUD

CRUD represents the four fundamental data operations:

- **Create**
- **Read**
- **Update**
- **Delete**

---

## Swagger UI

An interactive API documentation interface automatically available in FastAPI.

FastAPI's Swagger UI is available at:

```text
/docs
```

---

# Summary

The Books Project introduces the fundamental concepts required to build APIs with FastAPI. The application manages a collection of books and uses **CRUD operations** to create, read, update, and delete them.

Clients communicate with the FastAPI server through HTTP requests, and FastAPI returns HTTP responses. CRUD operations map naturally to HTTP methods: `POST` for Create, `GET` for Read, `PUT` for Update, and `DELETE` for Delete.

FastAPI also provides **Swagger UI** automatically at `/docs`, making it easy to explore and test API endpoints directly from a browser.

The first request method to implement in this project is **GET**, which will be used to retrieve book information.

All right.

Now that we've created our virtual environments, let's now go ahead and open up our directory of fast

API.

And let's create our first fast API application and API endpoint.

So let's go ahead and say open on PyCharm.

Let's go to our directory wherever we created that fast API and where we have our fast API environment

inside.

And let's go ahead and say open.

Now when you click open, we're going to see that we have our fast API directory with our fast API environment

within that directory where we're going to be creating our application.

Now the very first thing we need to do is go down to our bottom right hand corner where it says no interpreter.

Or it might create an interpreter for you, but we want to change that.

So let's go down here and say add new interpreter.

And we're going to say add local interpreter.

Let's go over here and say existing.

And inside here we want to change it to our fast API interpreter that we created using our virtual environment.

So let's go ahead and go into our documents our fast API our fast API environment and inside our bin

folder, if you are a mac user or inside your scripts folder, if you are a windows user, let's go

ahead and select our Python 3.11 or whatever your newest version of Python is.

And then let's go ahead and say okay, okay again.

And now we have our fast API environment working on our IDE.

So that's exactly what we wanted.

All right.

Now inside our directory let's go ahead and say right click new new Python file.

And we're going to name this file books.

Now the very first thing we need to do in books is import fast API.

So we can say from fast API.

Import fast API.

Now the very next thing we need to say is app equals fast API.

This allows Uvicorn to identify that hey, we are creating a new application of fast API, and this

is importing all of the resources that we got from the very top.

Then we want to say async def first API.

And return a dictionary of message.

Hello, Eric.

And now that we have this function, we now need fast API to acknowledge that, hey, this is an API

endpoint.

How can we now call this using our appropriate API verbs?

Well, right above this function we need to create a decorative and we're going to say at app dot get

parentheses slash.

So let's recap what we did right here.

We imported fast API from fast API.

We are acknowledging that this is going to be a fast API application, where we're setting app to what

we're importing.

For fast API, we created our own Python function of async, which stands for asynchronous dev, which

is our function call first API.

And we're going to return a message of hello Eric.

And we added this annotation at the top, which then allows fast API to know that at this path we are

going to be returning this method.

So let's open up our terminal.

Make sure your fast API environment is activated.

And in here we are going to say Uvicorn books, Colon App, Dash, Dash, reload and Books is coming

from the name of this file where our app is living.

So books.py and our app is living inside this.

So we're saying books is our app.

We're going to reload and we're going to be calling our Uvicorn.

So let's go ahead and press enter.

When we do this we get this URL where our application is running.

If we click this it's going to show us.

Hello Eric.

So if I zoom in a little bit we can see that it's going to print.

Hello Eric.

And that's because at our URL we have a slash at the end, which is exactly what our application is

looking for of our URL with just an empty slash of a Get which is going to return message.

Hello, Eric.

Now, one thing to point out, if we remove asynchronous and we save, we can see our application reran

and we reopen up our URL and we refresh.

We can still see that it says message.

Hello Eric.

So the async is fairly optional for fast API.

Now we can stop the server by clicking control C and that will stop our server from running.

And there's a new way to be able to run fast API applications.

If you have the newest version of fast API installed.

And we can do this by saying fast API.

Run and then the Python file you're trying to start.

So books.py.

This will start up the production mode of your fast API cli which will do the exact same thing.

Or we could also go ahead and say dev if we type in dev right here, it's going to just bring up our

development mode.

And it's saying development mode and production mode because we can set up different instances within

our code.

But mostly for this course I'm going to be using Uvicorn.

So we're going to be doing Uvicorn books, colon app, dash dash, reload.

And that's because underneath our fast API run, um, the file it's going to be running this behind

the scenes.

So I'm going to run the course from this command right here of the Uvicorn main colon app.

Dash dash.

Reload.

One thing to point out is that this slash is just going to be the end of our URL and port, and let's

go ahead.

Instead of just doing an empty slash, let's go ahead and just say API endpoint.

All right.

So now if we save the application and we open up our browser again.

We can see if we refresh the page we're going to get detail not found at this slash.

So what we need to do now is just go ahead and say slash API endpoint.

And now we're going to get our message of hello Eric back.

And now we can see that it's our URL, our port on our computer.

And then slash API endpoint.

Just like right here we are running fast API on that URL and port and then slash API endpoint.

All right.

And now with that this will wrap up this lecture on creating your first fast API application and our

first API endpoint.

So what are path parameters?

Well, path parameters are request parameters that have been attached to the URL.

Path parameters are usually defined as a way to find information based on location.

So let's think of a computer file system.

You can identify the specific resource based on the file in the path you are in.

So if you went to slash users slash coding with RGB documents, Python Fast API, section one, you

would expect to see section one in this path.

So let's say we have a request.

Our get request method of localhost port 8000 books.

Well, if we look at our function, we can see app.get slash books, async def, read all books and

we're going to return all the books.

Well, we can see is that the path at the end of the URL matches the path that we're expecting in our

fast API application.

Now, this is a static path because books and books within the fast API application cannot be changed.

We are deliberately saying slash books.

However, in fast API you can make dynamic path parameters.

So let's go ahead and say we have a request of read slash get and we have a new URL that's going to

say localhost port 8000 slash books.

Slash book one.

Now Book one is what the user is typing in, but the user could also say book two or book three or book

four or book all the way up to how many books are in application.

Now, based on each book, we don't want to have to create a new API endpoint for book one and book

two and book three.

We want to be able to consume a dynamic path parameter that will return whatever information the user

passes in.

So let's say we have our application of app.get slash books, but this time we have a function that

says async def, read all books and we have a dynamic param as our parameter for a read all books function.

And then we say return dynamic param and we're going to pass in the dynamic param that's passed in as

a parameter.

Well in our API endpoint we can say slash curly brackets dynamic param.

Now let's pay attention to what's going on when a request comes in of slash books.

Slash book one.

We can see that our API endpoint is slash books, slash curly brackets, dynamic param.

So that means anything that's at the end of slash books or matches this URL.

Let's grab that last variable and let's transform that into the dynamic param that we're passing in

as a parameter.

Now one thing that we need to note is that the API endpoint dynamic param that's in curly brackets needs

to match the naming convention that we have as our parameter in our read all books function.

So when we do this, we're going to get a response from fast API of dynamic Param Colon Book one, and

that's because Book one is getting passed in as an API endpoint.

We're going to grab that dynamic RAM, which is book one.

We are then just going to be passing that variable of book one and calling it dynamic param, and then

we're going to be returning that which is going to return book one.

So dynamic parameters are used often and we're going to be creating them in this application.

Now, one thing to note is that order matters with path parameters.

So we have our request of localhost port 8000 slash books, slash my book.

Well, if we have a function first, that is slash book slash dynamic param.

And then underneath this we say app.get book.

Slash my book.

Well, the very first thing that's going to happen is my book is going to be transformed into the dynamic

param of our first function.

So our second function will never get called because the first function is accepting the exact same

parameter list.

So what we need to do is always have the static or the smaller APIs in front, because fast API looks

in a chronological order from top to bottom to see what matches the URL that's coming in.

So what we need to do is reverse the order and say books, my book.

And then the second function can be the dynamic param.

So if my book matches the first function of book, slash my book, well then we're going to return book

title of my favorite book.

And if the last variable in the path is something other than my book, well then the dynamic param is

going to catch it.

So if it's not my book, the dynamic parameter is going to catch it.

And if it is my book, well then the very first static parameter is going to catch it.

So we have our path parameters and right now we're just returning either the static or dynamic data

that's getting passed in as the URL.

But what we actually want to do is return books.

So we have this books list, which is going to have all the books inside.

So we're going to call the request by the title and then return that book when we type in a request

that needs a space.

We are going to use percent 20.

So we can see our localhost slash books slash title percent 24.

Now this essentially just means title space for so in an API URL you can't have spaces.

So the encoding for a space is percent 20.

So when we say book slash title 24, we're going to have our function that takes in a book title.

We're going to explicitly say that this book title is going to be of type string.

So we're going to say app dot, get slash books, slash curly brackets of book title, which is our

dynamic parameter async def read book book title of type string, and then for book and book.

So we're going to loop through all of the books.

If book get titlecase fold and case fold is just a stronger lower function which will turn everything

to lowercase equals book title case fold.

So we're just making sure that we have matches on our strings.

Then we're going to return that book.

So the response is going to be that specific book of title for author for with our category of math.
