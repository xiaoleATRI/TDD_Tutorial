Feature: Manage Users Group
    **As** an Administrator
    **I want to** to be able to delete users and update permissions of users
    **So I can** manage users group


  Scenario Outline: Update permissions of users
    # **As** an Administrator
    # **I want to** to be able to delete users and update permissions of users
    # **So that** I can manage users group
    #  
    Given I logged in as administrator
    When I choose one user
    And I update its permission that this user can only read list
    When I logged out
    And logged in with updated user account
    Then this user can only view list
    And this user can not create item
    And this user can not update item
    And this user can not delete item
    And this user can not create list
    And this user can not update list
    And this user can not delete list

    Examples:
      | username | password | hiptest-uid |
      | admin | admin |  |

  Scenario: Delete users
    Given I logged in as administrator
