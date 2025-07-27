import allure
import pytest

from pages.com_max_xiaoheihe import Xiaoheihe


class TestDailyCheckIn:

    @allure.story("小黑盒 - 每日签到自动化脚本")
    @pytest.mark.name("xiaoheihe-daily-check-in")
    def test_daily_check_in(self):

        app = Xiaoheihe()
        app.weak_up()
        app.unlock()
        app.start_app()

        assert True