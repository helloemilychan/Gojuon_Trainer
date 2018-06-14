# A GUI written in tkinter of Gojuon Practicer 

# Import modules
import tkinter as tk
import time
import random
from tkinter import messagebox

# Dictionary of gojuon and yoon
gojuon = [
    ("a", "あ", "ア"),
    ("i", "い", "イ"),
    ("u", "う", "ウ"),
    ("e", "え", "エ"),
    ("o", "お", "オ"),
    ("ka", "か", "カ", "ga", "が", "ガ"),
    ("ki", "き", "キ", "gi", "ぎ", "ギ"),
    ("ku", "く", "ク", "gu", "ぐ", "グ"),
    ("ke", "け", "ケ", "ge", "げ", "ゲ"),
    ("ko", "こ", "コ", "go", "ご", "ゴ"),
    ("sa", "さ", "サ", "za", "ざ", "ザ"),
    ("shi", "し", "シ", "ji", "じ", "ジ"),
    ("su", "す", "ス", "zu", "ず", "ズ"),
    ("se", "せ", "セ", "ze", "ぜ", "ゼ"),
    ("so", "そ", "ソ", "zo", "ぞ", "ゾ"),
    ("ta", "た", "タ", "da", "だ", "ダ"),
    ("chi", "ち", "チ", "ji", "ぢ", "ヂ"),
    ("tsu", "つ", "ツ", "zu", "づ", "ヅ"),
    ("te", "て", "テ", "de", "で", "デ"),
    ("to", "と", "ト", "do", "ど", "ド"),
    ("na", "な", "ナ"),
    ("ni", "に", "ニ"),
    ("nu", "ぬ", "ヌ"),
    ("ne", "ね", "ネ"),
    ("no", "の", "ノ"),
    ("ha", "は", "ハ", "ba", "ば", "バ", "pa", "ぱ", "パ"),
    ("hi", "ひ", "ヒ", "bi", "び", "ビ", "pi", "ぴ", "ピ"),
    ("fu", "ふ", "フ", "bu", "ぶ", "ブ", "pu", "ぷ", "プ"),
    ("he", "へ", "ヘ", "be", "べ", "ベ", "pe", "ぺ", "ペ"),
    ("ho", "ほ", "ホ", "bo", "ぼ", "ボ", "po", "ぽ", "ポ"),
    ("ma", "ま", "マ"),
    ("mi", "み", "ミ"),
    ("mu", "む", "ム"),
    ("me", "め", "メ"),
    ("mo", "も", "モ"),
    ("ya", "や", "ヤ"),
    ("yu", "ゆ", "ユ"),
    ("yo", "よ", "ヨ"),
    ("ra", "ら", "ラ"),
    ("ri", "り", "リ"),
    ("ru", "る", "ル"),
    ("re", "れ", "レ"),
    ("ro", "ろ", "ロ"),
    ("wa", "わ", "ワ"),
    ("wo", "を", "ヲ"),
    ("n", "ん", "ン"),
]

yoon = [
    ("kya", "きゃ", "キャ"),
    ("kyu", "きゅ", "キュ"),
    ("kyo", "きょ", "キョ"),
    ("gya", "ぎゃ", "ギャ"),
    ("gyu", "ぎゅ", "ギュ"),
    ("gyo", "ぎょ", "ギョ"),
    ("sha", "しゃ", "シャ"),
    ("shu", "しゅ", "シュ"),
    ("sho", "しょ", "ショ"),
    ("jya", "じゃ", "ジャ"),
    ("jyu", "じゅ", "ジュ"),
    ("jyo", "じょ", "jyo"),
    ("cha", "ちゃ", "チャ"),
    ("chu", "ちゅ", "チュ"),
    ("cho", "ちょ", "チョ"),
    ("dya", "ぢゃ", "ヂャ"),
    ("dyu", "ぢゅ", "ヂュ"),
    ("dyo", "ぢょ", "ヂョ"),
    ("nya", "にゃ", "ニャ"),
    ("nyu", "にゅ", "ニュ"),
    ("nyo", "にょ", "ニョ"),
    ("hya", "ひゃ", "ヒャ"),
    ("hyu", "ひゅ", "ヒュ"),
    ("hyo", "ひょ", "ヒョ"),
    ("bya", "びゃ", "ビャ"),
    ("byu", "びゅ", "ビュ"),
    ("byo", "びょ", "ビョ"),
    ("pya", "ぴゃ", "ピャ"),
    ("pyu", "ぴゅ", "ピュ"),
    ("pyo", "ぴょ", "ピョ"),
    ("mya", "みゃ", "ミャ"),
    ("myu", "みゅ", "ミュ"),
    ("myo", "みょ", "ミョ"),
    ("rya", "りゃ", "リャ"),
    ("ryu", "りゅ", "リュ"),
    ("ryo", "りょ", "リョ"),
]

# Functions
def _about():
    messagebox.showinfo(
        title='About', message=title_text)

def sample_range(id):
	random_item = gojuon[id]
	range_dakuon = random.randint(0,1)
	range_handakuon = random.randint(0,2)
	romaji = random_item[0]
	hiragana = random_item[1]
	katakana = random_item[2]
	if dakuon_option.get() == 1:
		if id in range(5,20) or id in range(25,30):
			romaji = random_item[0 + range_dakuon*3]
			hiragana = random_item[1 + range_dakuon*3]
			katakana = random_item[2 + range_dakuon*3]
	if handakuon_option.get() == 1:
		if id in range(25,30):
			romaji = random_item[0 + range_handakuon*3]
			hiragana = random_item[1 + range_handakuon*3]
			katakana = random_item[2 + range_handakuon*3]
	if yoon_option.get() == 1:
		if random.random() < 0.5:
			if id < 36:
				yoon_item = yoon[id]
				romaji = yoon_item[0]
				hiragana = yoon_item[1]
				katakana = yoon_item[2]
	return romaji, hiragana, katakana


def generate_id(low,high):
    num = random.randint(low,high)
    global num_old
    while num_old == num:
    	num = random.randint(low,high)
    num_old = num
    return num

def _click(event=None):
    global i
    if (i % 2) == 0:
        num = generate_id(option_range_from.get()-1, option_range_to.get()-1)
        global random_list
        random_list = sample_range(num)
        output_1.config(text=" ")
        output_2.config(text=" ")
        output_3.config(text=" ")
        a = random.randint(0,2)
        if a == 0:
            output_1.config(text=random_list[a], font=('Arial', 60), fg='#6b72ff')
        if a == 1:
            output_2.config(text=random_list[a], font=('Arial', 60), fg='#6b72ff')
        if a == 2:
            output_3.config(text=random_list[a], font=('Arial', 60), fg='#6b72ff')
        i = i + 1
        Button_main.config(text='Show Answer (Space)')
        if win._job is not None:
            win.after_cancel(win._job)
            win._job = None
        win._job = win.after(timerange.get()*1000, _click)
    else:
        output_1.config(text=random_list[0], font=('Arial', 60), fg='#6b72ff')
        output_2.config(text=random_list[1], font=('Arial', 60), fg='#6b72ff')
        output_3.config(text=random_list[2], font=('Arial', 60), fg='#6b72ff')
        i = i + 1
        if win._job is not None:
            win.after_cancel(win._job)
            win._job = None
        Button_main.config(text='Next (Space)')

# Main windows and menubar
win = tk.Tk()
win.geometry('640x480')
title_text = 'Gojuon Trainer by Yunkai Zhang'
win.title(title_text)
win.option_add('*Font', 'Arial')
MenuBar = tk.Menu(win)
win.config(menu=MenuBar)
helpMenu = tk.Menu(MenuBar)
MenuBar.add_cascade(label='Help', menu=helpMenu)
helpMenu.add_command(label='About', command=_about)

# Range Selection
tk.Label(text='Gojuon Range From:').grid(row=0, column=0, stick='SE')
option_range_from = tk.Scale(win, from_=1, to=46, length=300, orient='horizontal')
option_range_from.set(1)
option_range_from.grid(row=0,column=1,columnspan=2, stick='W')

tk.Label(text='Gojuon Range To:').grid(row=1, column=0, stick='SE')
option_range_to = tk.Scale(win, from_=2, to=46, length=300, orient='horizontal')
option_range_to.set(46)
option_range_to.grid(row=1,column=1,columnspan=2, stick='W')

# Checkbuttons
dakuon_option = tk.IntVar()
handakuon_option = tk.IntVar()
yoon_option = tk.IntVar()

check_dakuon = tk.Checkbutton(win, text='Include Dakuon', variable=dakuon_option)
check_dakuon.grid(row=2, column=0)
check_dakuon.deselect()

check_handakuon = tk.Checkbutton(win, text='Include Handakuon', variable=handakuon_option)
check_handakuon.grid(row=2, column=1)
check_handakuon.deselect()

check_yoon = tk.Checkbutton(win, text='Include Yoon', variable=yoon_option)
check_yoon.grid(row=2, column=2)
check_yoon.deselect()

tk.Label(text='                     \n').grid(row=3, column=1)

# Chracter Display
tk.Label(text='Romaji').grid(row=4, column=0)
tk.Label(text='Hiragana').grid(row=4, column=1)
tk.Label(text='Katakana').grid(row=4, column=2)
win.grid_columnconfigure(0, weight=3, uniform="x")
win.grid_columnconfigure(1, weight=3, uniform="x")
win.grid_columnconfigure(2, weight=3, uniform="x")
win.grid_rowconfigure(5, weight=5, uniform="y")
output_1 = tk.Message(win, text="")
output_1.grid(row=5, column=0)
output_2 = tk.Message(win, text="")
output_2.grid(row=5, column=1)
output_3 = tk.Message(win, text="")
output_3.grid(row=5, column=2)

# Time range and next button
tk.Label(text='Time range (seconds)').grid(row=6, column=0, stick='SE')
timerange = tk.Scale(win, from_=1, to=60, length=200, orient='horizontal')
timerange.set(30)
timerange.grid(row=6, column=1, columnspan=2)

num_old = tk.IntVar()
i = 0
Button_main = tk.Button(win, text='Show Answer (Space)', command=_click)
Button_main.grid(row=7, column=0, columnspan=3)
Button_main.bind_all("<space>", _click)

tk.Label(text=' ').grid(row=8, column=0)

win._job = win.after(0, _click)
win.mainloop()