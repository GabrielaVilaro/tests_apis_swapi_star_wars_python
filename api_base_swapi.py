import json
import requests
from api_init import ApiInit


class ApiBaseSwapi:

    @staticmethod
    def get_people_swapi_starwars(people):
        """
        :param people: int
        :return: body json
        """
        response = requests.get(url=ApiInit.BASE_SWAPI + f"people/{people}/")

        json_response = json.loads(response.text)
        print(json.dumps(json_response, indent=3))

        return json_response

    @staticmethod
    def get_planets_swapi_starwars(planet):
        """
        :param planet: str number
        :return: body json
        """
        response = requests.get(url=ApiInit.BASE_SWAPI + f"planets/{planet}/")

        json_response = json.loads(response.text)
        print(json.dumps(json_response, indent=3))

        return json_response

    @staticmethod
    def get_films_swapi_starwars(film):
        """
        :param film: str number
        :return: body json
        """
        response = requests.get(url=ApiInit.BASE_SWAPI + f"films/{film}/")

        json_response = json.loads(response.text)
        print(json.dumps(json_response, indent=3))

        return json_response

    @staticmethod
    def get_species_swapi_starwars(specie):
        """
        :param specie: str number
        :return: body json
        """
        response = requests.get(url=ApiInit.BASE_SWAPI + f"species/{specie}/")

        json_response = json.loads(response.text)
        print(json.dumps(json_response, indent=3))

        return json_response

    @staticmethod
    def get_starships_swapi_starwars(starship):
        """
        :param starship: str number
        :return: body json
        """
        response = requests.get(url=ApiInit.BASE_SWAPI + f"starships/{starship}/")

        json_response = json.loads(response.text)
        print(json.dumps(json_response, indent=3))

        return json_response

    @staticmethod
    def get_vehicles_swapi_starwars(vehicle):
        """
        :param vehicle: str number
        :return: body json
        """
        response = requests.get(url=ApiInit.BASE_SWAPI + f"vehicles/{vehicle}/")

        json_response = json.loads(response.text)
        print(json.dumps(json_response, indent=3))

        return json_response
