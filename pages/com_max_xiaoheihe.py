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