
def fun(mainstream,must_watch):
    set1 = set(mainstream)
    set2 = set(must_watch)

    common_movies= list(set1.intersection(set2))

    uncommon_movies = list(set1.symmetric_difference(set2))

    return common_movies,uncommon_movies
    
        




mainstream = ["One Punch Man","Attack On Titan","One Piece","Sword Art Online","Bleach","Dragon Ball Z","One Piece"]
must_watch = ["Full Metal Alchemist","Code Geass","Death Note","Stein's Gate","The Devil is a Part Timer!","One Piece","Attack On Titan"]


common_movies, uncommon_movies = fun(mainstream,must_watch)

print("Common movies: ", common_movies)
print("Uncommon movies: ", uncommon_movies)
