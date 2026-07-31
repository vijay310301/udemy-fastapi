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
