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
        app.close_app()
        app.start_app()
        app.click_me()
        app.click_my_task()
        app.click_share_post()
        app.click_post()
        app.click_share_button()
        app.click_forward_QQ()
        app.click_to_my_computer()
        app.click_send_button()
        app.click_return_app()

        assert True