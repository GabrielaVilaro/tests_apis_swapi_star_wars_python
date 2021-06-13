"""DOCUMENTACIÓN API: https://swapi.dev/"""

from api_base_swapi import ApiBaseSwapi


class TestGetSwapi:

    @classmethod
    def setup_class(cls):
        print("Pre-Condiciones")

    def tests_get_validate_luck_skywalker(self):
        """Este tes realiza un GET sobre el endpoint de personajes y valida el nombre"""

        response_person = ApiBaseSwapi.get_people_swapi_starwars(people="1")

        luck = response_person["name"]

        assert luck == "Luke Skywalker"

    def test_get_validate_yavin(self):
        """Este tes realiza un GET sobre el endpoint de planetas y valida el nombre"""

        response_planet = ApiBaseSwapi.get_planets_swapi_starwars(planet="1")

        yavin = response_planet["name"]

        assert yavin == "Yavin IV"

    def test_get_validate_a_new_hope_into_film(self):
        """Este tes realiza un GET sobre el endpoint de peliculas y valida el nombre"""

        response_film = ApiBaseSwapi.get_films_swapi_starwars(film="1")

        film_a_new_hope = response_film["title"]

        assert film_a_new_hope == "A New Hope"


