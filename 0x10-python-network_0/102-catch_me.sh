#!/bin/bash
# make a request to 0.0.0.0:5000/catch_me sending a response
curl -sL 0:5000/catch_me -X PUT -H "You got me!"