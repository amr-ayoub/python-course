import movie_class

toy_story = movie_class.Movie("Toy Story","https://www.youtube.com/watch?v=KYz2wyBy3kc")
#toy_story.run_trailer()

avatar = movie_class.Movie("Avatar","https://www.youtube.com/watch?v=5PSNL1qE6VY")
#avatar.run_trailer()


#print(movie_class.Movie.__name__)

avatar.obj_var = 5
toy_story.obj_var = 6

print(avatar.obj_var)
print(toy_story.obj_var)

