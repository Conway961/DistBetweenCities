#Distance Between Two Cities - Calculates the distance between two cities and allows the user to specify a unit of distance.
# This program may require finding coordinates for the cities like latitude and longitude.
from geopy import Nominatim
from geopy.distance import distance

def get_details(city1: str, city2: str):
    loc = Nominatim(user_agent="Geopy Library")
    getloc1 = loc.geocode(city1)
    getloc2 = loc.geocode(city2)
    coord1 = getloc1.latitude, getloc1.longitude
    coord2 = getloc2.latitude, getloc2.longitude

    return coord1, coord2

def calc_dis(city1, city2, unit):
    if unit in ['Miles', 'Mi', 'M', 'm']:
        x =  distance(city1, city2).miles
        return f'{x:.2f} miles'
    elif unit in ['Km', 'K', 'Kilometres', 'k']:
        x = distance(city1, city2).km
        return f'{x:.2f} km'

def main():
    while True:
        try:
            user_input = int(input('1 to continue, 2 to exit: '))
            if user_input == 2:
                print('Exiting program...')
                break
            elif user_input == 1:
                city1 = input('Input City One: ')
                city2 = input('Input City Two: ')
                m = input('Unit of measurement (Miles / Km): ')
                x, y = get_details(city1, city2)
                dist = calc_dis(x, y, m)
                if dist is not None:
                    print(f'The distance from {city1} to {city2} is {dist}')
                print('Locations or measurement invalid..')
            else:
                print('Invalid input, try again..')
        except ValueError:
            print('Invalid input, try again..')


if __name__ == '__main__':
    main()