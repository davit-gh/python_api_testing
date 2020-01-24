# Created by staceyfinch at 2019-11-13
Feature: REST API Testing
  API testing using BDD approach

  Background:
    Given I set REST API base URL

  Scenario: GET request testing
    Given I set GET request endpoint
    And set Header content type parameter as "application/json"
    When I make a GET request
    Then I receive valid HTTP response code 200
    And the GET request response type is JSON
    And the response parameter userId equals to 5
    And the response parameter title contains sint

  Scenario: POST request testing
    Given I set POST request endpoint
    And set Header content type parameter as "application/json"
    And I set request body
    When make a POST request
    Then I receive valid HTTP response code 201
    And response body contains parameter id

