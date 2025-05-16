from time import sleep
from tkinter.tix import Select
from turtledemo.paint import switchupdown

from config.apps import apps

from ui_auto.base_page import BasePage
from utils import mongo
from utils.logger import logger

collection = "watcher"

class WebGLHost(BasePage):
    PACKAGE = "com.u3d.webglhost"
    watcher_start = False
    PERMISSIONWINDOWS = []
    INSTALL = []

    def load_watcher(self):
        mongo_client = mongo.get()
        permission_query = {"brand": self.brand, "tag": "PERMISSION"}
        install_query = {"brand": self.brand, "tag": "INSTALL"}
        permission_objs = mongo_client.find_all(collection, permission_query)
        install_objs = mongo_client.find_all(collection, install_query)
        for permission in permission_objs:
            record = {
                "name": permission["name"],
                "resource": permission["resource"],
                "click": permission["click"],
            }
            self.PERMISSIONWINDOWS.append(record)

        for install in install_objs:
            record = {
                "name": install["name"],
                "resource": install["resource"],
                "click": install["click"],
            }
            self.INSTALL.append(record)



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
        for watcher in self.INSTALL:
            self.client.watcher(watcher["name"]).when(watcher["resource"]).when(watcher["click"]).click()
        self.client.watcher.start(interval=1.0)
        logger.info("启动安装相关的watcher")

    def start_after_watcher(self):
        for watcher in self.PERMISSIONWINDOWS:
            self.client.watcher(watcher["name"]).when(watcher["resource"]).when(watcher["click"]).click()
        self.client.watcher.start(interval=1.0)

    def stop_watcher(self):
        self.client.watcher.reset()

    def close_app(self):
        self.client.app_stop(self.PACKAGE)
        logger.info(f"关闭应用: {apps[self.PACKAGE]}")