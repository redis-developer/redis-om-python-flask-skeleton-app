# Redis OM Python Flask Starter Application

A starter application for performing CRUD type operations with Redis OM Python ([GitHub](https://github.com/redis/redis-om-python), [Blog Post](https://redis.com/blog/introducing-redis-om-for-python/)) and the [Flask](https://flask.palletsprojects.com/) microframework.

We'd love to see what you build with Redis, RediSearch and Redis OM.  [Join the Redis community on Discord](https://discord.gg/redis) to chat with us about all things Redis OM and Redis.

## Overview

This application demonstrates common data manipulation patterns using Redis OM, an API built with Flask and a simple domain model.

Our entity is a Person, with the following attributes:

* `first_name`: A string, their first or given name.
* `last_name`: A string, their last or surname.
* `age`: An integer, their age in years.
* `personal_statement`: A string, A free text personal statement containing facts or other biographical information.

We'll let Redis OM handle generation of unique IDs, which it does using [ULIDs](https://github.com/ulid/spec).  Redis OM will also handle creation of unique Redis key names for us.

## Getting Started

Let's go...

### Requirements

To run this application you'll need:

* [git](https://git-scm.com/download) - to clone the repo to your machine. 
* [Python 3.9 or higher](https://www.python.org/downloads/).
* A [Redis](https://redis.io) database with the [RediSearch](https://redisearch.io) module version TODO or higher installed.  We've provided a `docker-compose.yml` for this.  You can also [sign up for a free 30Mb database with Redis Enterprise Cloud](https://redis.com/try-free/) - be sure to check the box to install RediSearch when creating your cloud database, follow [this guide](https://developer.redis.com/create/rediscloud/).
* [curl](https://curl.se/), or [Postman](https://www.postman.com/) - to send HTTP requests to the application.  We'll provide examples using curl in this document.
* Optional: [RedisInsight](https://redis.com/redis-enterprise/redis-insight/), a free data visualization and database management tool for Redis.  When downloading RedisInsight, be sure to select version 2.x.

### Get the Source Code

Clone the repository from GitHub:

```bash
$ git clone https://github.com/redis-developer/redis-om-python-flask-skeleton-app.git
$ cd redis-om-python-flask-skeleton-app
```

### Start a Redis Server, or Configure your Redis Enterprise Cloud Credentials

Next, we'll get a Redis Server up and running.  If you're using Docker:

```bash
$ docker-compose up -d
Creating network "redis-om-python-flask-skeleton-app_default" with the default driver
Creating redis_om_python_flask_starter ... done
$ 
```

If you're using Redis Enterprise Cloud, you'll need the hostname, port number, and password for your database.  Use these to set the `REDIS_OM_URL` environment variable like this:

```bash
$ export REDIS_OM_URL=redis://:<password>@<host>:<port>
```

(This step is not required when working with Docker as the Docker container runs Redis on `localhost` port `6379` with no password, which is the default connection that Redis OM uses.)

For example if your Redis Enterprise Cloud database is at port `9139` on host `enterprise.redis.com` and your password is `5uper53cret` then you'd set `REDIS_OM_URL` as follows:

```bash
$ export REDIS_OM_URL=redis://:5uper53cret@enterprise.redis.com:9139
```

Note the `:` before the password.

### Create a Python Virtual Environment and Install the Dependencies

Create a Python virtual environment, and install the project dependencies which are [Flask](https://pypi.org/project/Flask/) and [Redis OM](https://pypi.org/project/redis-om/):

```bash
$ python3 -m venv venv
$ . ./venv/bin/activate
$ pip install -r requirements.txt
```

### Start the Flask Application

Let's start the Flask application in development mode, so that Flask will restart the server for you each time you save code changes in `app.py`:

```bash
$ export FLASK_ENV=development
$ flask run

If all goes well, you should see output similar to this:

```bash
$ flask run
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: XXX-XXX-XXX
```

You're now up and running, and ready to perform CRUD operations on data with Redis, RediSearch and Redis OM for Python!  To make sure the server's running, point your browser at `http://127.0.0.1:5000/`, where you can expect to see the application's basic home page:

![screenshot](server_running.png)

### Problems?

If the Flask server fails to start, take a look at its output.  If you see log entries similar to this:

```python
raise ConnectionError(self._error_message(e))
redis.exceptions.ConnectionError: Error 61 connecting to localhost:6379. Connection refused.
```

then you need to start the Redis Docker container if using Docker, or set the `REDIS_OM_URL` environment variable if using Redis Enterprise Cloud.

If you've set the `REDIS_OM_URL` environment variable, and the code errors with something like this on startup:

```python
raise ConnectionError(self._error_message(e))
redis.exceptions.ConnectionError: Error 8 connecting to enterprise.redis.com:9139. nodename nor servname provided, or not known.
```

then you'll need to check that you used the correct hostname, port, password and format when setting `REDIS_OM_URL`.

## Create, Read, Update and Delete Data

Let's create and manipulate some instances of our data model in Redis.  Here we'll look at how to call the Flask API with curl (you could also use Postman), how the code works, and how the data's stored in Redis.

### Building a Person Model with Redis OM

TODO

### Adding New People

TODO code description

With the server running, add a new person using curl:

```bash
$ curl --location --request POST 'http://127.0.0.1:5000/person/new' \
--header 'Content-Type: application/json' \
--data-raw '{
    "first_name": "Test",
    "last_name": "User",
    "age": 99,
    "personal_statement": "I like dogs, walking, cycling and reading books."
}'
```

Running the above curl command will return the unique ULID ID assigned to the newly created person. For example `01FW40WMHDEWTA4GS301WN0Q69`.

TODO add more people.

### Find a Person by ID

If we know a person's ID, we can retrieve their data.

TODO code description

Try this out with curl, substituting `01FW40WMHDEWTA4GS301WN0Q69` for the ID of a person that you created in your database:

```bash
$ curl --location --request GET 'http://localhost:5000/person/byid/01FW40WMHDEWTA4GS301WN0Q69'
```

The server responds with a JSON object containing the user's data:

```json
{
  "age": 99,
  "first_name": "Test",
  "last_name": "User",
  "personal_statement": "I like dogs, walking, cycling and reading books.",
  "pk": "01FW40WMHDEWTA4GS301WN0Q69"
}
```

### Find People with Matching First and Last Name

Let's find all the people who have a given first and last name...

TODO code description.

Try this out with curl as follows:

```bash
$ curl --location --request GET 'http://127.0.0.1:5000/people/byname/Test/User'
```

The server responds with an object containing `results`, an array of matches:

```json
{
  "results": [
    {
      "age": 99,
      "first_name": "Test",
      "last_name": "User",
      "personal_statement": "I like dogs, walking, cycling and reading books.",
      "pk": "01FW40WMHDEWTA4GS301WN0Q69"
    }
  ]
}
```

### Find People within a Given Age Range

TODO

### Find People using Full Text Search on their Personal Statements

TODO

## Update a Person's Age

TODO

### Delete a Person

TODO

## Shutting Down Redis (Docker)

If you're using Docker, and want to shut down the Redis container when you are finished with the application, use `docker-compose down`:

```bash
$ docker-compose down
Stopping redis_om_python_flask_starter ... done
Removing redis_om_python_flask_starter ... done
Removing network redis-om-python-flask-skeleton-app_default
```
