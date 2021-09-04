""" Steven Sousa 02-19-21
This program is only to explain the basics of API for myself."""

# import module request. It allows us to interact with websites and other servers across the world.
import requests

# First thing needed is an API to work with. I'll be using this basic one that gives pictures of foxes.

# Create an object that will store all the content from API. (Usually called response)
# To get the data, type requests.get(API Link). This will package all of the information and store in object.
response = requests.get("https://randomfox.ca/floof")

# There are a few things that can be accessed through the object.
# First thing is the status code. Every time I do a http request, a status code is returned.
# The status code tells how the request went. The default (okay) is 200, meaning that the request went fine.

print(response.status_code)

# There are a few ways to look at my response, because there are a ton of different

