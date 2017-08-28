@type-root @type-tests
Feature: Manage Tests


  @browser-different
  Scenario: Run tests on different platforms
    Given I use the current directory as working directory
    When I run "behave -D platform="platform" -D browserName="browserName" -D version="version" features/"
      |platform         |browserName|version|
      |Windows 8        |firefox    |50     |
      |Mac OS X 10.9    |chrome     |31     |
    Then it should pass
