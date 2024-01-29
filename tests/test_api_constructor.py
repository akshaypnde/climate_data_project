import pytest
from src.api_connectors import construct_api_url  # Import the function from your module

def test_construct_api_url_success():
    base_url = "https://cckpapi.worldbank.org/cckp/v1/"
    expected_url = "https://cckpapi.worldbank.org/cckp/v1/cmip6-x0.25_climatology_tas,tasmin,tasmax_anomaly_annual_1995-2014_median_historical_ensemble_all_mean_WCA00202"
    actual_url = construct_api_url(
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
    )
    assert actual_url == expected_url

def test_construct_api_url_missing_component():
    base_url = "https://cckpapi.worldbank.org/cckp/v1/"
    with pytest.raises(ValueError):
        construct_api_url(
            base_url, 
            collection_code="cmip6-x0.25", 
            # Omitting some mandatory components
            type_code="climatology", 
            variable_code="tas,tasmin,tasmax"
            # The rest of the components are not provided
        )

# Add more tests as necessary to cover different scenarios
