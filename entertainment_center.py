import media
import movie_website
toy_story = media.Movie("Toy Story","A story of a boy and his toys that come to life","https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg","https://www.youtube.com/watch?v=JcpWXaA2qeg")
#print(toy_story.storyline)


avatar = media.Movie("Avatar"," A marine on an alien planet","https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg","https://www.youtube.com/watch?v=5PSNL1qE6VY")
#print(avatar.storyline)

#avatar.poster()

coc = media.Movie("Clash of Clans","Best mobile Strategy game Ever","http://i.imgur.com/H1WCTRc.jpg","https://www.youtube.com/watch?v=IpV441HhQ2g")
#coc.show_trailer()
#coc.poster()

avengers = media.Movie("Avengers","A group of superheros of the Marvel Universe fighting to protect the world","https://vignette3.wikia.nocookie.net/marvelmovies/images/f/f9/The_Avengers_Poster.jpg/revision/latest?cb=20110210135515","https://www.youtube.com/watch?v=eOrNdBpGMv8")

justice_league = media.Movie("Justice League","A group of superheros of the DC Comics fighting against crime and safeguarding the world","https://upload.wikimedia.org/wikipedia/en/3/31/Justice_League_film_poster.jpg","https://www.youtube.com/watch?v=3cxixDgHUYw")

cars3 = media.Movie("Cars 3","Story of a racing car having life","https://vignette2.wikia.nocookie.net/pixar/images/1/18/Cars_3_poster_2.jpg/revision/latest?cb=20170428231519","https://www.youtube.com/watch?v=2LeOH9AGJQM")



movies=[toy_story,avatar,coc,avengers,justice_league,cars3]
movie_website.open_movies_page(movies)
