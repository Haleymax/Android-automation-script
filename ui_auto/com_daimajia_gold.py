from config.apps import apps
from ui_auto.base_page import BasePage
from utils.logger import logger

class DaimajiaGold(BasePage):
    PACKAGE = "com.daimajia.gold"
    SIGN_BUTTON_ID = "com.daimajia.gold:id/tv_sign"
    CLOSE_BUTTON_XPATH = '//*[@resource-id="android:id/content"]//android.widget.ImageView[1]'

    def start_app(self):
        self.client.app_start(self.PACKAGE)
        logger.info(f"启动应用: {apps[self.PACKAGE]}")

    def click_me(self, text="我"):
        try:
            if self.client(text=text).wait(timeout=10.0):
                self.client(text=text).click()
                logger.info(f"点击按钮: {text}")
        except Exception as e:
            logger.error(f"点击'{text}'失败: {e}")

    def click_check_in(self):
        try:
            if self.client(resourceId=self.SIGN_BUTTON_ID).wait(timeout=10.0):
                sign_btn = self.client(resourceId=self.SIGN_BUTTON_ID)
                sign_btn.click()
                logger.info("点击签到成功")
        except Exception as e:
            logger.error(f"签到失败: {e}")

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

    def close_app(self):
        self.client.app_stop(self.PACKAGE)
        logger.info(f"关闭应用: {apps[self.PACKAGE]}")
