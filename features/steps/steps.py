from behave import *

# This should be added to environments.py
# from steps.actionwords import Actionwords
#
# def before_scenario(context, scenario):
#     context.actionwords = Actionwords.new(nil)

use_step_matcher('re')


@given(r'I logged in as administrator')
def impl(context):
    context.actionwords.i_logged_in_as_administrator()


@when(r'I choose one user')
def impl(context):
    context.actionwords.i_choose_one_user()


@when(r'I update its permission that this user can only read list')
def impl(context):
    context.actionwords.i_update_its_permission_that_this_user_can_only_read_list()


@when(r'I logged out')
def impl(context):
    context.actionwords.i_logged_out()


@when(r'logged in with updated user account')
def impl(context):
    context.actionwords.logged_in_with_updated_user_account()


@then(r'this user can only view list')
def impl(context):
    context.actionwords.this_user_can_only_view_list()


@then(r'this user can not create item')
def impl(context):
    context.actionwords.this_user_can_not_create_item()


@then(r'this user can not update item')
def impl(context):
    context.actionwords.this_user_can_not_update_item()


@then(r'this user can not delete item')
def impl(context):
    context.actionwords.this_user_can_not_delete_item()


@then(r'this user can not update list')
def impl(context):
    context.actionwords.this_user_can_not_update_list()


@then(r'this user can not delete list')
def impl(context):
    context.actionwords.this_user_can_not_delete_list()


@given(r'I am a logged-in user')
def impl(context):
    context.actionwords.i_am_a_loggedin_user()


@when(r'I add an item "(.*)"')
def impl(context, p1 = ""):
    context.actionwords.i_add_an_item_p1(p1)


@when(r'I create a list with first item "(.*)"')
def impl(context, p1 = ""):
    context.actionwords.i_create_a_list_with_first_item_p1(p1)


@then(r'I will see a link to "(.*)"')
def impl(context, p1 = ""):
    context.actionwords.i_will_see_a_link_to_p1(p1)


@when(r'I click the link to "(.*)"')
def impl(context, p1 = ""):
    context.actionwords.i_click_the_link_to_p1(p1)


@then(r'I will be on the "(.*)" list page')
def impl(context, p1 = ""):
    context.actionwords.i_will_be_on_the_p1_list_page(p1)


@then(r'this user can not create list')
def impl(context):
    context.actionwords.this_user_can_not_create_list()
