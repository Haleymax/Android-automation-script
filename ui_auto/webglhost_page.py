from time import sleep

from config.apps import apps
from config.watchers.webglhost import PERMISSIONWINDOWS, INSTALL

from ui_auto.base_page import BasePage
from utils.logger import logger


class WebGLHost(BasePage):
    PACKAGE = "com.u3d.webglhost"
    watcher_start = False

    def set_pop_window(self):
        perssions = PERMISSIONWINDOWS[self.brand]
        for key in perssions:
            self.check_permission(perssions[key][0])

    def check_permission(self, permission_id):
        if self.client(resourceId=permission_id).exists():
            logger.info("弹窗存在")
            self.start_after_watcher()
            self.watcher_start = True
            if self.watcher_start:
                logger.info("点击弹窗")
        else:
            logger.info("弹窗不存在")
            if self.watcher_start:
                self.stop_watcher()
                self.watcher_start = False

    def start_app(self):
        self.client.app_start(self.PACKAGE)
        logger.info(f"启动应用: {apps[self.PACKAGE]}")
        sleep(2)

    def one_plus_passwd(self):
        logger.info("启动一个密码watcher")
        self.client.watcher("1").when(xpath='//*[@content-desc="1"]').click()
        self.client.watcher.start(interval=1.0)

    def weak_device(self):
        self.client.screen_on()
        self.client.swipe(0.434, 0.882, 0.489, 0.157)
        logger.info(f"唤醒设备")

    def start_install_watcher(self):
        install_watchers = INSTALL[self.brand]
        for key in install_watchers:
            self.client.watcher(key).when(
                xpath=install_watchers[key]
            ).click()

        self.client.watcher.start(interval=1.0)
        logger.info("所有 Watcher 已启动")

    def start_after_watcher(self):
        permission_watchers = PERMISSIONWINDOWS[self.brand]
        for key in permission_watchers:
            self.client.watcher(key).when(
                xpath=permission_watchers[key][1]
            ).click()
        self.client.watcher.start(interval=1.0)

    def stop_watcher(self):
        self.client.watcher.reset()

    def close_app(self):
        self.client.app_stop(self.PACKAGE)
        logger.info(f"关闭应用: {apps[self.PACKAGE]}")