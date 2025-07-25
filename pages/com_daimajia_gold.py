from time import sleep

from config.apps import apps
from pages.base_page import BasePage
from utils.logger import logger

class DaimajiaGold(BasePage):
    PACKAGE = "com.daimajia.gold"
    SIGN_BUTTON_ID = "com.daimajia.gold:id/tv_sign"
    CLOSE_BUTTON_XPATH = '//*[@resource-id="android:id/content"]//android.widget.ImageView[1]'
    LOTTERY = '//*[@content-desc="去抽奖"]'
    CHECKIN_DAY = '//*[@content-desc="已连续签到 %d+ 天"]'
    DRAW_ONE = '//*[@content-desc="幸运抽奖"]'

    def start_app(self):
        self.client.app_start(self.PACKAGE)
        logger.info(f"启动应用: {apps[self.PACKAGE]}")
        sleep(2)

    def click_me(self, text="我"):
        try:
            if self.client(text=text).wait(timeout=10.0):
                self.client(text=text).click()
                logger.info(f"点击按钮: {text}")
        except Exception as e:
            logger.error(f"点击'{text}'失败: {e}")
        sleep(2)

    def click_check_in(self):
        try:
            if self.client(resourceId=self.SIGN_BUTTON_ID).wait(timeout=10.0):
                sign_btn = self.client(resourceId=self.SIGN_BUTTON_ID)
                sign_btn.click()
                logger.info("点击签到成功")
        except Exception as e:
            logger.error(f"签到失败: {e}")
        sleep(2)

    def close_lottery(self):
        try:
            if self.client.xpath(self.CLOSE_BUTTON_XPATH).wait(timeout=10.0):
                close_btn = self.client.xpath(self.CLOSE_BUTTON_XPATH)
                close_btn.click()
                logger.info("关闭抽奖弹窗")
            else:
                logger.warning("未找到关闭按钮")
        except Exception as e:
            logger.error(f"关闭弹窗失败: {e}")
        sleep(2)

    def click_check_in_days(self):
        try:
            if self.client.xpath(self.CHECKIN_DAY).wait(timeout=10.0):
                close_btn = self.client.xpath(self.CHECKIN_DAY)
                close_btn.click()
                logger.info("点击已签到")
            else:
                logger.warning("点击已签到")
        except Exception as e:
            logger.error(f"关闭弹窗失败: {e}")
        sleep(2)

    def go_lottery(self):
        try:
            if self.client.xpath(self.LOTTERY).wait(timeout=10.0):
                close_btn = self.client.xpath(self.LOTTERY)
                close_btn.click()
                logger.info("去抽奖")
            else:
                logger.warning("去抽奖")
        except Exception as e:
            logger.error(f"关闭弹窗失败: {e}")
        sleep(2)

    def draw_one(self):
        try:
            if self.client.xpath(self.DRAW_ONE).wait(timeout=10.0):
                close_btn = self.client.click(0.278, 0.901)
                close_btn.click()
                logger.info("抽奖一次")
            else:
                logger.warning("抽奖一次")
        except Exception as e:
            logger.error(f"关闭弹窗失败: {e}")
        sleep(2)

    def close_app(self):
        self.client.app_stop(self.PACKAGE)
        logger.info(f"关闭应用: {apps[self.PACKAGE]}")
