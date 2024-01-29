from construct_api_url import construct_api_url
from src.config import base_url
import requests

def extract_data(api_url):
    """
    Extract data from a given API URL.

    :param api_url: URL of the API to extract data from.
    :return: Extracted data in JSON format.
    """
    
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # will raise an HTTPError if the HTTP request returned an unsuccessful status code
        return response.json()
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

# Example usage
api_url = construct_api_url(
        base_url, 
        collection_code="cmip6-x0.25", 
        type_code="climatology", 
        variable_code="tas,tasmin,tasmax", 
        product_code="anomaly", 
        aggregation_code="annual", 
        period_code="1995-2014", 
        percentile_code="median", 
        scenario_code="historical", 
        model_code="ensemble", 
        model_calculation_code="all", 
        statistic_code="mean", 
        geocode="WCA00202"
        # Add the remaining parameters as required
    )

data = extract_data(api_url)
print(data)
