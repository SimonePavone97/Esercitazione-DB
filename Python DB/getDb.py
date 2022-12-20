from DataBase1 import DataBaseconnector


class GetDataBaseData:

    @classmethod
    def getAllActors(cls):
        all_actors = "SELECT * FROM Actor"
        results = DataBaseconnector.executeQuery(all_actors)
        DataBaseconnector.close()
        return results

    @classmethod
    def getAllFilms(cls):
        all_films = "SELECT * FROM Film"
        results = DataBaseconnector.executeQuery(all_films)
        DataBaseconnector.close()
        return results
