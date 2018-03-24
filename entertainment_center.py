import fresh_tomatoes
import media


# Iron Man movie: movie title, story line, poster image and trailer
iron_man = media.Movie("Iron Man", "When wealthy industrialist Tony Stark is "
                       "forced to build an armored suit after "
                       "a life-threatening incident, he ultimately decides "
                       "to use the technology to fight against evil.",
                       "https://upload.wikimedia.org/wikipedia/en"
                       "/7/70/Ironmanposter.JPG",
                       "https://www.youtube.com/watch?v=byQpcN78UjQ")

# The Incredible Hulk movie: movie title, story line, poster image and trailer
the_i_hulk = media.Movie("The Incredible Hulk", "Thanks to a gamma ray "
                         "experiment gone wrong, Dr. Bruce Banner must deal"
                         " with the side effects as well as being hunted by "
                         "the military. Manwhile, a soldier uses the same "
                         "technology to become a deadly abomination.",
                         "https://upload.wikimedia.org/wikipedia/"
                         "en/8/88/The_Incredible_Hulk_poster.jpg",
                         "https://www.youtube.com/watch?v=CcqpE-mR7sY")

# Iron Man 2 movie: movie title, story line, poster image and trailer
iron_man_2 = media.Movie("Iron Man 2", "With the world now aware of his dual"
                         " life as an armored superhero, billionaire inventor"
                         " Tony Stark faces pressure from the government, the"
                         " press, and the public to share his technology "
                         "with the military, along with dealing with an "
                         "insane Russian genius who is intent on killing him.",
                         "https://upload.wikimedia.org/"
                         "wikipedia/en/e/ed/Iron_Man_2_poster.jpg",
                         "https://www.youtube.com/watch?v=DIfgxIv5xmk")

# Thor movie: movie title, story line, poster image and trailer
thor = media.Movie("Thor", "The powerful but arrogant Asgardian Thor is cast"
                   " out from his home to live among humans on Earth, where"
                   " he must learn humility, and ends up finding love.",
                   "https://upload.wikimedia.org/wikipedia/en/f/fc"
                   "/Thor_poster.jpg",
                   "https://www.youtube.com/watch?v=JOddp-nlNvQ")

# Captain America: The First Avenger movie: movie title,
# story line, poster image and trailer
cap_am_tfa = media.Movie("Captain America: The First Avenger", "After being "
                         "deemed unfit for military service, Steve Rogers"
                         " volunteers for a top secret research project that"
                         " turns him into Captain America, a superhero "
                         "dedicated to defending American ideals.",
                         "https://upload.wikimedia.org/wikipedia/en/3/37"
                         "/Captain_America_The_First_Avenger_poster.jpg",
                         "https://www.youtube.com/watch?v=JerVrbLldXw")

# The Avengers movie: movie title, story line, poster image and trailer
the_avengers = media.Movie("The Avengers", "When global security is threatened"
                           " by Loki and his cohorts, Nick Fury of "
                           "S.H.I.E.L.D. assembles a team of superheroes to "
                           "save the world from disaster.",
                           "https://upload.wikimedia.org/wikipedia/en/f/f9"
                           "/TheAvengers2012Poster.jpg",
                           "https://www.youtube.com/watch?v=eOrNdBpGMv8")

# Set the movies that will be passed to the media file
movies = [iron_man, the_i_hulk, iron_man_2, thor, cap_am_tfa, the_avengers]

# Open the HTML file in a webbrowser via the fresh_tomatoes.py file
fresh_tomatoes.open_movies_page(movies)
