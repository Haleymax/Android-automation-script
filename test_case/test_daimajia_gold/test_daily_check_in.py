import allure
import pytest

from pages.com_daimajia_gold import DaimajiaGold
from utils.logger import logger


class TestDailyCheckIn:

    @allure.story("稀土掘金-每日自动签到脚本")
    @pytest.mark.name("daily_check_in")
    def test_daily_check_in(self):
        """
        稀土掘金每日自动进行签到的脚本
        """
        allure.step("进行ui自动化操作")
        logger.info("进行自动化操作")
        app = DaimajiaGold()
        app.weak_up()
        app.unlock()
        app.start_app()
        app.click_me()
        file = app.get_screenshot("me")
        allure.attach.file(
            source=file,
            name="screenshot",
            attachment_type=allure.attachment_type.PNG,
        )
        app.close_app()

        assert True