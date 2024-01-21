from testCases.testcase_login import TestLogin
import pytest


@pytest.mark.regress
def test_execution():
    login_obj = TestLogin()

    login_obj.test_homepage_title()
    login_obj.test_login_001()

