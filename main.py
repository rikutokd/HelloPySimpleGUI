import PySimpleGUI as sg

# ウィンドウのレイアウト
layout = [ [sg.Text('Hello World!')] ]

# ウィンドウオブジェクトの作成
window = sg.Window('PySimpleGUI Sample', layout, size=(600, 300))

# イベントのループ
while True:
    # イベントの読み込み
    event, values = window.read()
    # ウィンドウの×ボタンが押されれば終了
    if event == sg.WIN_CLOSED:
        break

# ウィンドウ終了処理
window.close()