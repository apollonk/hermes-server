# Description
This is the server-side implementation of the
Hermes project.

# Code

## hermesmodel.py:
The data model for Hermes. This is the internal 
representation of the FAD data for the purposes
of server-side persistence and processing. Includes
some tests in __main__(), intended to be used as
a library.

## flask-rest.py:
This presents a RESTful service for clients to 
authenticate against and execute CRUD operations
with.
