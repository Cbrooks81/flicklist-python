import webapp2
import random
class Index(webapp2.RequestHandler):

    def getRandomMovie(self):

        # TODO: make a list with at least 5 movie titles
        movie_list = ["Major League", "Remember the Titans", "Ali", "Happy Gilmore", "Blue Chips"]
        # TODO: randomly choose one of the movies, and return it
        selected_movie = random.choice(movie_list)
        return selected_movie

    def get(self):
        # choose a movie by invoking our new function
        movie = self.getRandomMovie()

        # build the response string
        content = "<h1>Movie of the Day</h1>"
        content += "<p>" + movie + "</p>"

        # TODO: pick a different random movie, and display it under
        # the heading "<h1>Tommorrow's Movie</h1>"
        movie_2 = self.getRandomMovie()
        while movie == movie_2:
            movie_2 = self.getRandomMovie()
        content += "<h1>Tommorrow's Movie of the Day</h1>"
        content += "<p>" + movie_2 + "</p>"

        self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', Index)
], debug=True)
