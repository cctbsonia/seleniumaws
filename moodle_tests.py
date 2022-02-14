import unittest
import moodle_methods as methods
import moodle_locators as locators

class MoodleAppPositiveTestCases(unittest.TestCase):

    @staticmethod
    def test_create_new_user():
        methods.setUp()
        methods.log_in(locators.moodle_username, locators.moodle_password)
        methods.create_new_user()
        methods.check_user_created()
        methods.log_out()
        methods.log_in(locators.new_username, locators.new_password)
        methods.check_we_logged_in_with_new_cred()
        methods.log_out()
        methods.log_in(locators.moodle_username, locators.moodle_password)
        methods.delete_test_user()
        methods.log_out()
        methods.tearDown()

#
# setUp()
# # Log in
# log_in(locators.moodle_username, locators.moodle_password)
# # Create a new user
# create_new_user()
# # Check a new user has been added
# check_user_created()
# # Close web browser
#
#
# ### Log in with new user credentials Test Case ###
# # Open web browser
# #setUp()
# # Log in
# log_in(locators.new_username, locators.new_password)
# # Check we logged in with the new credentials
# check_we_logged_in_with_new_cred()
# log_out()
# log_in(locators.moodle_username, locators.moodle_password)
# delete_test_user()
# log_out()
# # Close the web browser
# tearDown()

