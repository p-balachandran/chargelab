# chargelab

To write automated tests for the provided endpoint, we'll focus on testing the following areas:

Endpoint Availability: Ensure that the endpoint is accessible and returns a valid response.
Query Parameter Validation: Validate that the endpoint handles query parameters correctly, including both valid and invalid parameters.
Response Structure: Verify that the response structure matches the expected format, including key fields and values.
Filtering Functionality: Test the filtering functionality to ensure that chargers are filtered correctly based on the provided parameters.
Error Handling: Validate the behavior of the endpoint when encountering errors, such as invalid parameters or missing data.

These tests can be executed using the pytest framework to automatically discover and run the test functions.

Limitations:
Test relies on specific test data to be available -- this may change depending on which environment this test is performed on

To run (assuming you have python and pip installed)
- Install libraries using `pip install -r requirements.txt`
- `pytest` will run the test and return pass/ fail for each test case


Notes:
If using VS code, you can follow this to install python and virtual env.
https://code.visualstudio.com/docs/python/python-tutorial
