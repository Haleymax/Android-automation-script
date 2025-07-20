import os.path
import subprocess
from datetime import datetime
from time import sleep

import uiautomator2 as u2

from config.apps import apps
from config.path import screenshot_path
from utils.logger import logger


class BasePage:
    def __init__(self):
        self.client = u2.connect()
        self._get_brand()

    def install_app(self, package_path):
        try:
            self.client.app_install(package_path)
            logger.info(f"installed {package_path}")
        except Exception as e:
            logger.error(f"Failed to install {package_path}: {e}")

    def uninstall_app(self, package):
        try:
            app_info = self.client.app_info(package)
            if app_info is not None:
                logger.info("webglhost 存在，准备卸载...")
                result = self.client.app_uninstall(package)
                if result:
                    logger.info(f"{apps[package]} 卸载成功")
                else:
                    logger.info(f"{apps[package]} 卸载失败")
            else:
                logger.info(f"{apps[package]} 不存在，无需卸载")
        except Exception as e:
            logger.error(f"Failed to uninstall {package}: {e}")

    def weak_up(self):
        logger.info("唤醒设备")
        self.client.screen_on()
        sleep(1)

    def unlock(self):
        logger.info("解锁手机")
        self.client.swipe(0.4398, 0.7471, 0.5204, 0.2367)
        sleep(1)

    def get_screenshot(self, picture_name)->str:
        logger.info(f"截取当前屏幕: {picture_name}")
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_name = f"{timestamp}{picture_name}.png"
        os.makedirs(screenshot_path, exist_ok=True)
        file_path = os.path.join(screenshot_path, file_name)
        self.client.screenshot(file_path)
        logger.info(f"{file_path} 图片保存成功")
        return file_path



    def _get_brand(self):
        result = subprocess.run(
            ["adb", "shell", "getprop", "ro.product.brand"],
            capture_output=True,
            text=True
        )
        self.brand = result.stdout.strip()

    def __del__(self):
        self.client.exists()