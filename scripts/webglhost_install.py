import time
from time import sleep

from config.path import file_path
from pages.webglhost_page import WebGLHost


def webglhost_ui_auto():
    app = WebGLHost()
    app.load_watcher()
    app.uninstall_app("com.u3d.webglhost")
    app.one_plus_passwd()
    app.weak_device()
    app.start_install_watcher()
    app.install_app(package_path=file_path)
    sleep(6)
    app.stop_watcher()
    while True:
        app.start_app()
        for pes in app.PERMISSIONWINDOWS:
            app.check_permission(pes["resource"])
        time.sleep(20)
        app.close_app()
        time.sleep(2)
webglhost_ui_auto()