import time
from time import sleep

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



    def _identify_pop_ups(self, permission_id):
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

    # def check_pop_ups(self):


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

    def click_sdk_sample(self, resourceId="com.u3d.webglhost:id/sdkSampleBt"):
        sdk_sample_btn = self.client(resourceId=resourceId)
        sdk_sample_btn.click()
        logger.info("点击sdk sample 按钮")
        time.sleep(1.5)

    def input_url(self, url, resourceId="com.u3d.webglhost:id/server_address_et"):
        address_et = self.client(resourceId=resourceId)
        address_et.set_text(url)
        print("input url")
        time.sleep(1.5)
        self.client.click(0.909, 0.675)
        print("back")

    def select_wxminigame(self, resourceId='com.u3d.webglhost:id/btnweWeixinminigame'):
        wxmini_game_opt = self.client(resourceId=resourceId)
        wxmini_game_opt.click()
        logger.info("点击weixinminigame")
        time.sleep(1.5)

    def click_start(self, resourceId='com.u3d.webglhost:id/start_btn'):
        start_btn = self.client(resourceId=resourceId)
        start_btn.click()
        logger.info("点击start 按钮")
        time.sleep(1.5)

    def click_play(self, resourceId='com.u3d.webglhost:id/play_btn'):
        play_btn = self.client(resourceId=resourceId)
        play_btn.click()
        logger.info("点击play 按钮")
        time.sleep(1.5)


    def click_destroy(self, resourceId='com.u3d.webglhost:id/destroy_handle'):
        destroy_btn = self.client(resourceId=resourceId)
        destroy_btn.click()
        logger.info("点击play 按钮")
        time.sleep(1.5)

