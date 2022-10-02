import streamlit as st
import tkinter
import pyautogui as gui
import pandas as pd
import ctypes
import time


st.title("ガラス目視検査システム")
st.header("サンプル情報")

with st.form(key="sample_form"):
    name = st.text_input("名前")
    submit_btn_1 = st.form_submit_button("有効")

    if submit_btn_1:
        st.text(f"ようこそ！{name}さん！検査を開始します。")

        All_position_x = []
        All_position_y = []
        All_size = []

        try:
            while True:
                if ctypes.windll.user32.GetAsyncKeyState(0x01) == 0x8000:

                    x, y = gui.position()
                    print(x)
                    print(y)

                    # ボタンのクリックイベント
                    def btn_click_1():
                        # テキスト取得
                        Positon_x = int(txt_1.get())
                        Positon_y = int(txt_2.get())
                        Size = float(txt_3.get())

                        All_position_x.append(Positon_x)
                        All_position_y.append(Positon_y)
                        All_size.append(Size)

                        print("OK")
                        time.sleep(0.3)
                        root.destroy()

                    def btn_click_2():
                        # # テキスト取得
                        Positon_x = int(txt_1.get())
                        Positon_y = int(txt_2.get())
                        Size = float(txt_3.get())
                        ID = txt_4.get()

                        All_position_x.append(Positon_x)
                        All_position_y.append(Positon_y)
                        All_size.append(Size)

                        # リストからデータフレーム作成
                        df = pd.DataFrame(
                            list(zip(All_position_x, All_position_y, All_size)),
                            columns=["X座標", "Y座標", "欠点サイズ"],
                        )
                        df.to_csv(
                            ID + "_" + name + ".csv", encoding="shift_jis", index=False
                        )
                        print(df)

                        st.dataframe(df)

                        All_position_x.clear()
                        All_position_y.clear()
                        All_size.clear()

                        time.sleep(0.3)
                        st.text(f"{name}さん！{ID}_{name}.csvで出力しました。")
                        root.destroy()

                    def btn_click_3():
                        # テキスト取得
                        All_position_x.clear()
                        All_position_y.clear()
                        All_size.clear()
                        root.destroy()

                    def btn_click_4():
                        # テキスト取得
                        All_position_x.clear()
                        All_position_y.clear()
                        All_size.clear()
                        # テキスト取得
                        st.empty()
                        root.destroy()

                    # Tkクラス生成
                    root = tkinter.Tk()
                    # 画面サイズ
                    root.geometry("500x400")
                    # 画面タイトル
                    root.title("欠点入力画面")
                    # ラベル
                    lbl_1 = root.Label(text="X座標")
                    lbl_1.place(x=30, y=70)
                    # テキストボックス
                    txt_1 = root.Entry(width=20)
                    txt_1.place(x=140, y=70)

                    # Entryウィジェットへ文字列のセット
                    txt_1.insert(root.END, x)

                    lbl_2 = root.Label(text="Y座標")
                    lbl_2.place(x=30, y=140)
                    txt_2 = root.Entry(width=20)
                    txt_2.place(x=140, y=140)
                    txt_2.insert(root.END, y)

                    lbl_3 = root.Label(text="欠点ｻｲｽﾞ")
                    lbl_3.place(x=30, y=210)
                    txt_3 = root.Entry(width=20)
                    txt_3.place(x=140, y=210)

                    lbl_4 = root.Label(text="ID")
                    lbl_4.place(x=30, y=0)
                    txt_4 = root.Entry(width=20)
                    txt_4.place(x=140, y=0)

                    # ボタン作
                    btn_1 = root.Button(root, text="入力", command=btn_click_1)
                    btn_1.place(x=50, y=300)

                    btn_2 = root.Button(root, text="終了", command=btn_click_2)
                    btn_2.place(x=250, y=300)

                    btn_3 = root.Button(root, text="やり直し", command=btn_click_3)
                    btn_3.place(x=100, y=300)

                    btn_4 = root.Button(root, text="表示削除", command=btn_click_4)
                    btn_4.place(x=350, y=300)

                    root.attributes("-topmost", True)
                    root.mainloop()

        except KeyboardInterrupt:
            print("終了")
