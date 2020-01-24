from behave import *
import requests
import json

api_endpoints = {}
request_headers = {}

@given("I set POST request endpoint")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    api_endpoints["POST_URL"] = api_url + "/posts"
    print("URL is: {}".format(api_endpoints["POST_URL"]))


@when("make a POST request")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    response = requests.post(url=api_endpoints["POST_URL"],
                             json=context.request_body,
                             headers=request_headers
                             )
    context.response = response
    print("\nThe response text is:", response.text)


@then("I receive valid HTTP response code {response_code}")
def step_impl(context, response_code):
    """
    :type response_code: str
    :type context: behave.runner.Context
    """
    if context.response.__getattribute__("status_code"):
        print("\nThe response code is: {}".format(context.response.status_code))
        assert context.response.status_code is int(response_code)


@step("response body contains parameter id")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    to_json = json.loads(context.response.text)
    assert to_json["id"]


@step("I set request body")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.request_body = {"title": "Just A Title", "body": "This is a body", "user": "Joe"}
    print("\nThe request body is:\n", context.request_body)


@given("I set REST API base URL")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    global api_url
    api_url = "http://jsonplaceholder.typicode.com"


@given("I set GET request endpoint")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    api_endpoints["GET_URL"] = api_url + "/posts/42"
    print("URL is: {}".format(api_endpoints["GET_URL"]))


@step('set Header content type parameter as "{content_type}"')
def step_impl(context, content_type):
    """
    :type content_type: str
    :type context: behave.runner.Context
    """
    request_headers['Content-Type'] = content_type
    print("The headers are:\n", request_headers)


@when("I make a GET request")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    response = requests.get(
        url=api_endpoints["GET_URL"], headers=request_headers
    )
    context.response = response
    print("\nThe response text is:", response.text)


@step("the GET request response type is JSON")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    content_type = context.response.headers.get("Content-Type", None)
    assert 'json' in content_type, "Content type is not JSON"


@step("the response parameter userId equals to 5")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    response2json = json.loads(context.response.text)
    assert response2json['userId'] == 5, "userId is not equal to 5"


@step("the response parameter title contains {string}")
def step_impl(context, string):
    """
    :type string: str
    :type context: behave.runner.Context
    """
    response2json = json.loads(context.response.text)
    assert string in response2json['title'], "title does not contain {}".format(string)