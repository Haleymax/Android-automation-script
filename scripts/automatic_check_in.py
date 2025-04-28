from ui_auto.com_daimajia_gold import DaimajiaGold

def auto_check_in():
    app = DaimajiaGold()
    app.start_app()
    app.click_me()
    app.click_check_in()
    app.close_lottery()
    app.close_app()

auto_check_in()