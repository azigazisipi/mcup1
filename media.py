import webbrowser


class Movie():
    """
    Movie class determines the input and output parameters
    """
    
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        """
        :param moviee_title: string
        :param movie_storyline: string
        :param poster image: string
        :param trailer_youtube: string
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        
    def show_trailer(self):
        """
        opens the movie's trailer from youtube
        """
        webbrowser.open(self.trailer_youtube_url)
