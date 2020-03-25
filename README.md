# Summary

This repository demonstrates a basic use of docker-compose as a means for containerised development. This manifests as a Flask application that integrates with a Redis instance as a basic in-memory store. In addtion to this the ``/db`` endpoint interacts with a Postgres database containing the ``Persons`` table via a ``SELECT`` statement to return some information to the front end.

## Setup

1. Ensure you have Docker setup on your development machine.

2. Clone the repository and navigate to the root directory of the project in the terminal.

3. Run ``source env.sh``

4. Run ``docker-compose build`` to build the services (web) as a cealn docker image.

5. Run ``docker-compose up`` to spin up the docker compose services.

6. Navigate to ``http://localhost:5000/`` to see the application in action.

## Use Notes

A binding is made between the container and the local development machine to enable code editing, alongside flask refreshing the server when a change is detected.

Each time you modified the original Docker image, you will have to run ``docker-compose build`` once again to enable docker-compose to use the latest version of the service. 

If the DB script is changed, you need to run ``docker-compose down`` and then ``docker-compose up`` again for the change to be reflected in the container.

## Research Notes

Unit testing with docker and docker compose appear to have no clear standards or recommended approaches online. My concern is that if you develop within DC using volumes then how that can accompanied with local unit tests, in an intuitive manner.

Debugging within a container can occur from using an external shell, or using an IDE attachment. With the latter being the most effective approach. Docker Compose also allows evaluating the logs collected from each container.

An analog to doc-comparison for Docker use would be the current implementation in this repository, but executes the ``exemplar.py`` file to run a standalone app.

## Resources

https://docs.docker.com/compose/gettingstarted/
https://docs.docker.com/compose/networking/
https://docs.docker.com/compose/production/

