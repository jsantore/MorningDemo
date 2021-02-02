import requests


def get_data(url: str):
    all_data = []
    

    return all_data


def main():
    url = "https://api.data.gov/ed/collegescorecard/v1/schools.json?school.degrees_awarded.predominant=2,3&fields=id,school.state,school.name"
    all_data = get_data(url)

if __name__ == '__main__':
    main()