from requests import get
from bs4 import BeautifulSoup as parser
import json


main_source_of_zip = 'https://worldpostalcode.com/'
data_set = {}
region_names = []
zip_code_per_city = {}


def parse():
    regions_source = parser(get(main_source_of_zip + 'united-states/').text, 'html.parser')
    list_of_regions = regions_source.find("div", {"class": 'regions'})

    for parsed_region_name in list_of_regions.findAll('a'):
        data_set[parsed_region_name.text] = {"state": []}

    for region_name in data_set:
        city_source = parser(get(main_source_of_zip + 'united-states/' + region_name.lower() + '/').text, 'html.parser')
        print("Parsing the Cities For", region_name)
        list_of_cities = city_source.find("div", {"class": 'regions'})

        for city_name in list_of_cities.findAll('a'):
            data_set[region_name]['state'].append({city_name.get_text(): ""})

            zip_source = parser(get(main_source_of_zip + 'united-states/' + region_name.lower() + '/' + city_name.get_text()).text, 'html.parser')
            list_of_codes = zip_source.findAll("div", {'class': 'unit'})

            for main_list in list_of_codes:
                places = main_list.findAll('div', {'class': 'place'})
                zip_codes = main_list.findAll('div', {'class': "code"})
                for place in places:
                    for zip_code in zip_codes:
                        zc = [zc.text for zc in zip_code.findAll('span')]
                        place = place.text
                        data_set[region_name]['state'][0][city_name] = {place: zc}
                        pass

    with open("parsed_addresses.json", 'w+') as jfile:
        json.dump(data_set, jfile, ensure_ascii=False, indent=4)

    return "Parsing Done"
