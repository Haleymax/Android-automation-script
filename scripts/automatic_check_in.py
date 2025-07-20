from pages.com_daimajia_gold import DaimajiaGold

def auto_check_in():
    app = DaimajiaGold()
    app.start_app()
    app.click_me()
    app.click_check_in()
    app.click_check_in_days()
    app.close_lottery()
    app.go_lottery()
    app.close_app()

auto_check_in()