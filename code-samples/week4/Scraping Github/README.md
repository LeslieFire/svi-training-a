#Scraping Github

What the script does is it first sends a request to the Github api on the list of users with a substantial number of followers. Using that list, we send a request to call the detailed profile of each user. Authentication is needed as Github only allows 60 request for non authenticated scrapers.

For further reference:
*	[Github API](https://developer.github.com/v3/)
*	[Python Requests](http://docs.python-requests.org/en/latest/)