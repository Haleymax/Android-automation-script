import time
from datetime import datetime
from utils.logger import logger
from ui_auto.webglhost_page import WebGLHost

url = ["https://minigamehost.cdn.unity.cn/wxgames/sqcs7", "https://minigamehost.cdn.unity.cn/wxgames/zdlz2", "https://minigamehost.cdn.unity.cn/wxgames/jsjs9"]


end_time = datetime(2025, 5, 23, 18, 00, 0)

def retry_start_and_stop_game():
    app = WebGLHost()
    app.load_watcher()
    app.start_app()
    app.click_sdk_sample()

    count = 0
    index = 1
    while datetime.now() < end_time:
        app.input_url(url=url[index])
        app.select_wxminigame()
        app.click_start()
        time.sleep(5)
        app.click_play()
        time.sleep(3)
        if count % 5 == 0 :
            file_name = f"{count}.jpg"
            app.screen_to_file(file_name)
        time.sleep(5)
        app.click_destroy()
        count = count + 1
        logger.info(f"这是第 {count} 次循环启停")
        index = (index + 1) % 3



retry_start_and_stop_game()