## Cow management REST service 

### Requirements

The Cow management REST service will serve as a CRUD solution for Cows in a farm. Requirements:

- API design should follow the OpenAPI specification (https://spec.openapis.org/oas/v3.1.0).
- It should offer these endpoints:
  - Get cows: It will get all cows from a Database.
  - Insert cows: It will receive a cow definition and it will insert it into the Database
  - Update cow: It will update a cow in the Database based on a cow ID and a Cow definition
  - Delete cow: It will delete a cow from a cow ID

Desired DB will be a NoSQL, like MongoDB.

Additionally, on the `Get cows` endpoint, a query language will be implemented so that the results are filtered out.
(note: Enhance proposal: Use NoSql filtering mechanisms to get the benefits of returning only the desired records from the DB)

### Persistence

MongoDB instance has been selected for simplicity and lack of requirements on ACID needs. 
We assume BASE for this POC and ease of use and scalability.

## Query filtering

Custom implementation with format:

`http://<HOST>:<PORT>/<VERSION>/cows?q=querystatement:value;querystatement2:value2`

has been implemented. It's considered technical debt moving this implementation towards MongoDB format: https://www.mongodb.com/docs/compass/current/query/filter/

## Deployment

Building the project:

`python setup.py install`

This will generate a distributable Python Egg under `/dist/`.

## Local execution

### Running tests locally

From the rest-service folder run:

`python -m pytest tests`

### Running the app locally

`flask --app controller/controller.py run --port 8080`

### Running MongoDB (Mac M1 chip)

- Install MongoDB following these instructions: `https://www.mongodb.com/docs/manual/administration/install-community/`

- Run a daemon MongoDB instance:
  - `mongod --config /opt/homebrew/etc/mongod.conf --fork`

- Run MongoDB shell for troubleshooting / querying data:
  - `mongosh`

- Stop MongoDB instance
  - `kill -9 <MONGODB_PID>`