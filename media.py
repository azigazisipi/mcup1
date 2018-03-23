import webbrowser


class Movie():
    """
    Movie class defines the parameters for entertaintment_center.py
    """
    
    def __init__(self, movie_title, movie_storyline, poster_image_url,
                 trailer_youtube_url):
        """
        :param moviee_title: string
        :param movie_storyline: string
        :param poster_image_url: string
        :param trailer_youtube_url: string
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
        
    def show_trailer(self):
        """
        opens the movie's trailer from youtube
        """
        webbrowser.open(self.trailer_youtube_url)
