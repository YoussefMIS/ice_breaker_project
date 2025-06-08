import os
from dotenv import load_dotenv
import requests
import pprint

load_dotenv()  # Load environment variables from a .env file

# print(pprint.pprint(requests.get("https://gist.githubusercontent.com/YoussefMIS/3d11481653736d942454962936a1af95/raw/d3331bd77fdce9d20c47717ed99f6653d1235d67/youssef-scraping.json").json()))


def scrap_linkedin_profile(linkedin_url: str, mock: bool = True):
    """
    Scrape a LinkedIn profile using the provided URL.
    """
    if mock:
        linkedin_url = "https://gist.githubusercontent.com/YoussefMIS/3d11481653736d942454962936a1af95/raw/d3331bd77fdce9d20c47717ed99f6653d1235d67/youssef-scraping.json"
        response = requests.get(linkedin_url, timeout=10)
    else:
        api_endpoint = "https://api.scrapin.io/enrichement/profile"
        querystring = {
            "apikey": os.environ["SCRAPIN_API_KEY"],
            "linkedInUrl": "https://www.linkedin.com/in/youssef-shehata-8095231bb",
        }

        response = requests.request("GET", api_endpoint, params=querystring)

    data = response.json().get("person")
    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None) and k not in ["certifications"]
    }

    return data


if __name__ == "__main__":
    linkedin_url = "https://www.linkedin.com/in/youssef-shehata-8095231bb"
    profile_data = scrap_linkedin_profile(linkedin_url, mock=False)
    pprint.pprint(profile_data)
    # print(profile_data)
