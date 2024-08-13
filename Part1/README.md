# Recommendation System

## Project Overview
This recommendation system comprises two main services:
- **Generator**: This service generates random numbers based on a provided model name and viewer ID.
- **Invoker**: This service manages recommendations, handling caching and orchestrating calls to the Generator service.

The system utilizes Docker for containerization and Redis for caching, ensuring scalable and efficient handling of requests.

## Prerequisites
To run this project, you will need:
- Docker
- Docker Compose

Make sure Docker and Docker Compose are installed on your system. You can download them from the official Docker website.


## Setup Instructions

### Building and Running the Containers

1. **Clone the Repository**
   Ensure you have cloned the repository and are in the project root directory.

2. **Build the Services**
   Run the following command to build the Docker images and start the containers. This command also starts a Redis container for caching.

   ```bash
   docker-compose up --build

3. **Interacting with the Services**
   Access the Invoker Service: Use a browser or a tool like curl to interact with the Invoker service. For example:
    ```bash
    curl http://localhost:6000/recommend/userSilvia

