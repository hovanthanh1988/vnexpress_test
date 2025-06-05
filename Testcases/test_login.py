import pytest


class TestLogin():
    @pytest.mark.usefixtures("setup")
    def test_go_to_vnexpress(self):
        self.driver.get("https://vnexpress.net/")
        assert True, "This is a placeholder test to ensure pytest runs correctly."
