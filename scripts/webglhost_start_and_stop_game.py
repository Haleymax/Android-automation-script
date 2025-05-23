import time
from datetime import datetime
from utils.logger import logger
from ui_auto.webglhost_page import WebGLHost

url = "https://minigamehost.cdn.unity.cn/wxgames/sqcs7"


end_time = datetime(2025, 5, 23, 18, 00, 0)

def retry_start_and_stop_game():
    app = WebGLHost()
    app.load_watcher()
    app.start_app()
    app.click_sdk_sample()
    app.input_url(url=url)
    count = 0
    while datetime.now() < end_time:
        app.select_wxminigame()
        app.click_start()
        time.sleep(5)
        app.click_play()
        time.sleep(10)
        app.click_destroy()
        count = count + 1
        logger.info(f"这是第 {count} 次循环启停")




retry_start_and_stop_game()