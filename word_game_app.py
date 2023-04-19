# 単語テストをTkinterで作成する。

# モジュールのインポート
import tkinter as tk
import csv
import random

Random = []
Question = []
right = 0
index = 0
user_answer = ""
Num = 0
count = 0


# csvファイルの読み込み
words = []
with open("words.csv", encoding="Shift-JIS") as f:
    for row in csv.reader(f):
        words.append(row)



def clear_result():
    lbl1.configure(text="")
    lbl2.configure(text="")
    lbl3.configure(text="")
    lbl4.configure(text="")


# スタート関数
def word_game_start(self):
    
    # ゲームの説明
    lbl1.configure(text = "単語テストを始めます。")
    lbl2.configure(text = "問題は全て小文字で入力してください。")
    lbl3.configure(text = "問題は全部で" + str(len(words)) + "問あります。" )
    lbl4.configure(text = "挑戦したい問題数を入力してスタートボタンを押してください")

    entry1.focus_set() # フォーカスをエントリーに移す
    btn1.bind('<ButtonPress>',word_game_number)
    


# 入力した問題数だけリストから抽出する関数
def word_game_number(self):
    global Random, right, index, user_answer, Num, count
    lbl1.configure(text="")
    lbl2.configure(text="")

    Num = int(entry1.get()) 
    # リストから行を指定した数だけ乱数で取得
    for i in range(Num):
        Random.append(random.choice(words))
    lbl3.configure(text = str(Num) + "問に挑戦します。")
    lbl4.configure(text="数秒後に自動的にスタートします。")
    entry1.delete(0, tk.END) # エントリー内の文字を削除
    root.after(2000, word_game_random)


def word_game_random():
    global Random, Question, right, index, user_answer, Num, count
    
    count += 1

    # 問題の中から１行取得
    Question = random.choice(Random)

    # 取得した行の問題を表示
    lbl1.configure(text= "今" + str(count) + "問目です。") 
    lbl2.configure(text=Question[0]) # 日本語を表示
    lbl3.configure(text=Question[1]) # 英語を表示
    lbl4.configure(text="")
    entry1.bind('<Return>', word_game_judge)


def word_game_judge(self):
    global Random, Question, right, index, user_answer, Num
    print(Question)
    entry1.focus_set()# フォーカスをエントリーに移す
    user_answer = entry1.get()
    print(user_answer)
    print(Question[2])
    entry1.delete(0, tk.END) # エントリー内の文字を削除
    if user_answer == Question[2]:
        lbl3.configure(text="正解")
        right += 1
    else:
        lbl3.configure(text="不正解")
        lbl4.configure(text="正解は" + Question[2] + "です。")
    if index == len(Random) - 1:
        lbl4.configure(text= str(Num) + "問中" + str(right) + "問正解です。")
    else:
        root.after(1500, word_game_random)
        Random.remove(Question)
    




# ウインドウの作成
root = tk.Tk()
root.geometry('500x500')
root.title('単語テスト')

# ラベルの設置
lbl1 = tk.Label(text="スタートボタンを押してください。")
lbl2 = tk.Label(text="")
lbl3 = tk.Label(text="")
lbl4 = tk.Label(text="")

# ボタンの設置
btn1 = tk.Button(text="スタート")
    
# テキストボックスの配置
entry1 = tk.Entry(width = 20)
entry1.place(relx = 0.5, rely = 0.5, anchor = tk.CENTER)

# ボタンを押すとword_game_random()が実行される
btn1.bind('<ButtonPress>',word_game_start)



# ラベルのパック
lbl1.pack()
lbl2.pack()
lbl3.pack()
lbl4.pack()

# ボタンのパック
btn1.pack()


root.mainloop()