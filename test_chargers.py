import requests
import pytest
from jsonschema import validate
import json


base_url = "https://api-v1-green.uat.chargelab.io/core/v1/chargers"

# no filters, testing endpoint availability
def test_get_chargers():
    response = requests.get(base_url)
    
    #verify 200 success response
    assert response.status_code == 200, "Failed to retrieve chargers"
    chargers = response.json()
    
    #verify basic response schema
    assert "totalCount" in chargers, "Response does not contain totalCount"
    assert chargers["totalCount"] > 1, "Expected more than 1 charger but got {}".format(chargers["totalCount"])
    assert "entities" in chargers, "Response does not contain entities"
    assert len(chargers["entities"]) > 1,  "Expected more than 1 charger but got {}".format(chargers["totalCount"])
   

#valid query params/ filtering
def test_get_chargers_with_valid_params():
    params = {
        "filter_eq[name]": "csf-free-plugev",
        "role": "DRIVER"
    }
    response = requests.get(base_url, params=params)
    assert response.status_code == 200, "Failed to retrieve chargers with valid params"
    
    chargers = response.json()
    assert "totalCount" in chargers, "Response does not contain totalCount"
    assert "entities" in chargers, "Response does not contain entities"
    assert chargers["totalCount"] == 1, "Expected 1 charger but got {}".format(chargers["totalCount"])

#error handling (400 response)
@pytest.mark.parametrize("invalid_filter", [
    "filter_eq",  # Missing field name
    "invalid_filter[name]",  # Invalid field name
    "filter_eq=",  # Missing filter value
    "filter_eq[]",  # Missing filter value
    "filter_eq[invalid_field]=value",  # Invalid field name
    "filter_eq[name]=invalid_value"  # Invalid filter value
])
def test_get_chargers_with_invalid_params(invalid_filter):
    params = {
        invalid_filter: "value"
    }
    response = requests.get(base_url, params=params)
    assert response.status_code == 400, "Expected 400 Bad Request for invalid filter: {}".format(invalid_filter)

#verify entities schema
def test_entities_schema_validation():
   with open("entities_schema.json") as entities_json_file:
    entity_schema = json.load(entities_json_file)
    
    response = requests.get(base_url)
    assert response.status_code == 200, "Failed to retrieve chargers"
    chargers = response.json()
    assert "entities" in chargers, "Response does not contain entities"
    
    # Validate the 'entities' field against the schema
    try:
        validate(instance=chargers["entities"], schema=entity_schema)
    except Exception as e:
        pytest.fail(f"Schema validation failed for 'entities' field: {e}")