# anomaly webserver

This is a webserver written by Paradox, paradox neutral dev.

There is no connection between this product and any other entity.

## Background

Http 1, 2, and 3 are different specs that should be considered 
different individually. However, they need to share the same ports
for initially establishing the connections and the processing of
requests are similar for similar features. Idealy, the server should
have a uniform structure with a request handlers with a uniform api
where the using application does not care regarding which protocol is
being used, only that data is being recieved and sent.

## Structure

The central parts of the application will be the Listener, live 
connections, workers, and connection handlers / dispatchers.

## Features

For the simplest version of this application, static content server,
proxy services, load balancing and proxy caching should be supported.

Multitenancy should be supported.

TLS is needed for all three versions of http 1/2/3.

### Modularity at its core

Due to the size of this project, the application will be built in steps.
Each step may include inefficient, insecure algorithms that must be replaced
later. Therefore, the internal apis between components must be established and
obeyed. Components will then be swapped as needed.

### Performance

Inspite of the modularity, the application needs to perform its duties with the
most number of clients with the least latency possible. Therefore, inspite of the
prior statement, all parts of the application need to be considered for optimizations
to ensure maximum performance.

### Monitorable

Inspite of performance, the webserver needs to have good monitoring capabilities. 

### Configurable

The user should not need to jump through hoops to configure the server.

### The Core is a library

This should be able to be used as an application server. Primary ideas are js, lua, python,
and java. Three of these languages are scripting languages. Why do they need a fast webserver?
The answer: Why do they need a slow webserver? Ideally, the webserver will be able to efficiently
provide access to internal structures for retrievable or generate structures in the desired language
to reduce the time the application language spends handling the text. Hopefully, this will allow for
more concurrent users with overall reduced latency per request.

## Requirements

## Development Requirements

The tests are written using Python 3. As developed its python 3.12.

The partial statemachine generator is written in python 3.12.

