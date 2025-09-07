from time import sleep

from config.apps import apps
from pages.base_page import BasePage
from utils.logger import logger


class Xiaoheihe(BasePage):
    package = "com.max.xiaoheihe"

    def start_app(self):
        self.client.app_start(self.package)
        logger.info(f"启动应用: {apps[self.package]}")
        sleep(2)

    def close_app(self):
        self.client.app_stop(self.package)
        logger.info("close app")
        sleep(2)

    def click_me(self):
        self.client(text="我").click()
        logger.info("click me button clicked")
        sleep(2)

    def click_my_task(self):
        self.client(text="我的任务").click()
        logger.info("click my task clicked")
        sleep(2)

    def click_share_post(self):
        self.client.xpath("(//android.widget.FrameLayout)[11]").click()
        logger.info("click share any post to social platforms")
        sleep(2)

    def click_post(self):
        self.client.click(0.4648, 0.1917)
        logger.info("click post clicked")
        sleep(2)

    def click_share_button(self):
        self.client(resourceId="com.max.xiaoheihe:id/button_right").click()
        logger.info("click share button clicked")
        sleep(2)
        
    def click_forward_QQ(self):
        self.client(text="QQ").click()
        logger.info("click forward QQ clicked")
        sleep(2)

    def click_to_my_computer(self):
        self.client(text="我的电脑").click()
        logger.info("click my computer button clicked")
        sleep(2)

    def click_send_button(self):
        self.client(text="发送").click()
        logger.info("click send button clicked")
        sleep(2)

    def click_return_app(self):
        self.client(text="返回小黑盒").click()
        logger.info("click return app button clicked")
        sleep(2)

