# Summary

This repository demonstrates a basic use of docker-compose as a means for containerised development. This manifests as a Flask application that integrates with a Redis instance as a basic in-memory store.

## Setup

1. Ensure you have Docker setup on your development machine.

2. Clone the repository and navigate to the root directory of the project in the terminal.

3. Run ``source .env``

3. Run ``docker-compose up`` to build the application.

4. Navigate to ``http://localhost:5000/`` to see the application in action.

A binding is made between the container and the local development machine to enable code editing, alongside flask refreshing the server when a change is detected.

## Notes

Production Guidance - https://docs.docker.com/compose/production/

Unit testing with docker and docker compose appear to have no clear standards or recommended approaches online. My concern is that if you develop within DC using volumes then how that can accompanied with local unit tests?

Debugging within a container can occur from using an external shell, or using an IDE at this stage. With the latter being the most effective approach. Docker Compose also allows evaluating the logs collected from each container.



## Resources

https://docs.docker.com/compose/gettingstarted/
https://docs.docker.com/compose/networking/

