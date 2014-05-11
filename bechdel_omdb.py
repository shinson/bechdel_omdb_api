# Goal 1:
#   Ask the user for the movie title they want to check
#   Display all of the details about the movie returned by the API
#
#   Things to keep in mind:
#       How will your program behave when multiple movies are returned?
#       How will your program behave when no movies are returned?
#       How will your program behave with works like "the" in the title?

from urllib2 import Request, urlopen, URLError
import json

#Asks user for title or IMDB Id to search
#If the user inputs "The" in the beginning, the code searches for it and takes it out of the title
title = raw_input("What movie do you want to search? ").lower()
if "the" in title[0:4]:
	title = title.replace("the ", "")
# Goal 2:
#   Check to see if the user input is a movie title or an ImdbID and use the proper endpoint
# Used exceptions so that when the program checked to see if the title was an integer it wouldn't cause an error with a non-id input
try:
	if int(title) >=0 and len(title) == 7:
		endpoint = "http://bechdeltest.com/api/v1/getMovieByImdbId?imdbid=" + title	
except ValueError:
	endpoint = "http://bechdeltest.com/api/v1/getMoviesByTitle?title=" + title
	
request = Request(endpoint)
response = urlopen(request)
movie = json.loads(response.read())

#First conditional is for non-IMDb ID entries that will list all the titles it comes up with in the API
# The list is also listed with a number so the user can easily choose which movie they want
# When the movie is an id then it just skips the listing of all the tiles and just spits out the information
# In this conditional I am also setting up the endpoint for the OMDB api 
# Finally I use the .items() method in a for loop to iterate all the information of the movie from the api
if "title" in endpoint:
	y=0
	x=1
	print "Which movie are you looking for?"
	for index, movies in enumerate(movie):
		print "{0}.{1}".format(index+1, movies['title'])
	choice = raw_input("Pick a number? ")
	endpoint_omdb= "http://omdbapi.com/?i=tt" + movie[int(choice)-1]['imdbid']
	print "Information from the Bechdel Test"
	for key, value in movie[int(choice)-1].items():
		print "\t{0}:{1}".format(key.capitalize(), value)
else:
	for key, value in movie.items():
		print "\t{0}:{1}".format(key.capitalize(), value)
	endpoint_omdb= "http://omdbapi.com/?i=tt" + movie['imdbid']

# Goal 3:
# Integrate this with the Open Movie Database API: http://www.omdbapi.com/
#   Display all of the details from both APIs when searching for a movie.
#   Note that you may need to prefix your ImdbIDs with 'tt' to get the search to work.

#Endpoint came from conditional above
request_omdb = Request(endpoint_omdb)

response_omdb = urlopen(request_omdb)
movie_omdb = json.loads(response_omdb.read())
print "Info from OMBD API:"
for key, value in movie_omdb.items():
	print "\t{0}:{1}".format(key, value)



