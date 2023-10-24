import requests
from behave import given, when, then
from assertpy import assert_that

api_key = '63a6384429mshc5cb62cf7e66101p1b3d9ajsn5085948dfe5c'
if api_key is None:
    raise ValueError("No API key found in environment variables")

base_url = "https://weatherapi-com.p.rapidapi.com/current.json"

headers = {
    "X-RapidAPI-Key": api_key,
    "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
}


@when('I request current weather information for "{location}"')
def step_impl(context, location):
    querystring = {"q": location}
    response = requests.get(base_url, headers=headers, params=querystring)
    context.response = response
    # print("Response body:")
    # print(context.response.text)


@then('the response status code should be 200')
def step_impl(context):
    assert_that(context.response.status_code).is_equal_to(200)


@then('the response should contain "location" key')
def step_impl(context):
    response_json = context.response.json()
    assert_that(response_json).contains('location')


@then('the "location" key should contain "name" equal to "{location}"')
def step_impl(context, location):
    response_json = context.response.json()
    location_name = response_json['location']['name']
    assert_that(location_name).is_equal_to(location)


@when('I request current weather information for a invalid location "{location}"')
def step_impl(context, location):
    querystring = {"q": location}
    context.response = requests.get(
        base_url, headers=headers, params=querystring)


@then('the response status code should be 400 or 404')
def step_impl(context):
    assert_that(context.response.status_code).is_in([400, 404])


@then('the response should contain "error" key')
def step_impl(context):
    response_json = context.response.json()
    assert_that(response_json).contains('error')


@when(u'I request current weather information for a invalid "InvalidLocation"')
def step_impl(context):
    raise NotImplementedError(
        u'STEP: When I request current weather information for a invalid "InvalidLocation"')


@when(u'I request current weather information for "London" without API key')
def step_impl(context):
    headers_no_api_key = {
        "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
    }
    querystring = {"q": "London"}
    context.response = requests.get(
        base_url, headers=headers_no_api_key, params=querystring)


@then(u'the response status code should be 401 or 403')
def step_impl(context):
    assert context.response.status_code in [
        401, 403], "Expected a 401 or 403 status code, but got {}".format(context.response.status_code)
