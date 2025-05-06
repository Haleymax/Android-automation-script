import subprocess

import uiautomator2 as u2

from config.apps import apps
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


    def _get_brand(self):
        result = subprocess.run(
            ["adb", "shell", "getprop", "ro.product.brand"],
            capture_output=True,
            text=True
        )
        self.brand = result.stdout.strip()

    def __del__(self):
        self.client.exists()