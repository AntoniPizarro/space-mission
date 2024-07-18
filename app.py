import eel

eel.init("web")

@eel.expose
def view_menu_stage_planning():
    html = ""

    return html

eel.start("index.html", mode="chrome-app", port=8080, cmdline_args=["--start-fullscreen", "--browser-startup-dialog"])