from getDb import GetDataBaseData

all_Actors = GetDataBaseData.getAllActors()
all_films = GetDataBaseData.getAllFilms()

for actor in all_Actors:
    print(actor)

for film in all_films:
    print(film)
