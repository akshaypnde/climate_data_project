from src.config import base_url 

def construct_api_url(base_url, **kwargs):
    """
    Construct an API URL based on the given keyword arguments, following a specific sequence.

    :param base_url: The base URL of the API.
    :param kwargs: Keyword arguments representing the different components of the URL.
    :return: Constructed API URL as a string.
    :raises ValueError: If any mandatory component is missing.
    """
    # Define the expected sequence of components
    expected_keys = [
        'collection_code', 'type_code', 'variable_code', 'product_code', 
        'aggregation_code', 'period_code', 'percentile_code', 'scenario_code', 
        'model_code', 'model_calculation_code', 'statistic_code', 'geocode'
    ]

    # Check for missing mandatory components
    missing_keys = [key for key in expected_keys if key not in kwargs or kwargs[key] is None]
    if missing_keys:
        raise ValueError(f"Missing mandatory components: {', '.join(missing_keys)}")

    # Construct the URL
    components = [kwargs[key] for key in expected_keys]
    return f"{base_url}/{'_'.join(components)}"

# Example usage
try:

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
    print(api_url)
except ValueError as e:
    print(f"Error constructing the API URL: {e}")
