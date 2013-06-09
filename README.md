Find That Box!
==============

This is a simple service for finding the most recent IP address of a box. Useful for being able to SSH into embedded devices that move around a lot.

The client just sends a request to a checkin server with a list of its local interfaces and its [unique id](https://pypi.python.org/pypi/snowflake). The checkin server records the public IP address of the request and saves it to the datastore. The API is also simple:

    GET /checkin/<uuid>: Perform a checkin
    GET /status/<uuid>: Return a JSON representation of the given machine's last checkin
    GET /status: Return a JSON representation of all checkins (admin only)
