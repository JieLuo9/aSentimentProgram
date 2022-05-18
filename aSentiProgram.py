# from email import message
# import imp
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import Message
from tkinter import Text
from tkinter import END
from aip import AipNlp
# from matplotlib import cbook


""" 我的 APPID AK SK """
APP_ID = '26011028'
API_KEY = 'u50reZx5TGjGRSlfVntursUT'
SECRET_KEY = 'qtzcjdBrQDS9z7kbunKI1KzKF1ri4p7Q'

list = {"酒店": 1,
        "KTV": 2,
        "美食": 4,
        "旅游": 5,
        "健康": 6,
        "教育": 7,
        "商业": 8,
        "房产": 9,
        "汽车": 10,
        "生活": 11,
        "购物": 12,
        "数码": 13}
client = AipNlp(APP_ID, API_KEY, SECRET_KEY)     # 创建客户端

acbox = ""


def aMessageBox1(text):
    messagebox.showinfo(title="情感分析结果", message=text)


def aMessageBox2(text):
    messagebox.showinfo(title="关键词提取结果", message=text)


def theCbox(event):
    global acbox
    acbox = cbox.get()


def sentimentKey():
    global acbox
    txt = ""
    text = entry_k.get("1.0", END)
    options = {}
    print(list[acbox])
    options["type"] = list[acbox]
    result = client.commentTag(text, options)
    print(result)
    for item in result['items']:
        if item['sentiment'] == 0:

            tmp = "负面情绪的关键词：" + item['prop'] + item['adj'] + '\n'
            txt += tmp
            print(txt)
            print("负面情绪的关键词：" + item['prop'] + item['adj'])

        if item['sentiment'] == 1:

            tmp = "中立情绪的关键词：" + item['prop'] + item['adj'] + '\n'
            txt += tmp
            # print(txt)
            # print("中立情绪的关键词：" + item['prop'] + item['adj'])
        if item['sentiment'] == 2:

            tmp = "正面情绪的关键词：" + item['prop'] + item['adj'] + '\n'
            txt += tmp
            print(txt)
            print("正面情绪的关键词：" + item['prop'] + item['adj'])
    print(txt)
    aMessageBox2(txt)
    print(result)


def sentimentClassify():
    text = text1.get("1.0", END)            # 获取文本框的字符串
    # print(text)
    """ 调用情感倾向分析 """
    result = client.sentimentClassify(text)
    print(result)
    data2 = result['items']          # 获取key为“items”的value，其为一个列表，包含一个字典
    detc = data2[0]                 # 获取字典
    positive = detc['positive_prob']   # 获取字典中的情感倾向概率
    if positive > 0.50000:
        aMessageBox1("这段文本很可能是正面的情感倾向！")
    else:
        aMessageBox1("这段文本很可能是负面的情感倾向！")


root_w = tk.Tk()                                                       # 创建根窗口
root_w.title("情感分析程序 by JieLuo")                                  # 根窗口标题
# 根窗口宽高
w = 600
h = 300
# 根窗口居中，获取屏幕尺寸以计算布局参数，使根窗口居屏幕中央
screenw = root_w.winfo_screenwidth()
screenh = root_w.winfo_screenheight()
size_geo = '%dx%d+%d+%d' % (w, h, (screenw-w)/2, (screenh-h)/2)
root_w.geometry(size_geo)
root_w.iconbitmap('icon.ico')  # 根窗口图标

tk.Label(root_w, text="情感倾向分析：").grid(row=0)
tk.Label(root_w, text="文本：").grid(row=1)
text1 = Text(root_w, width=20, height=4, undo=True, autoseparators=False)
text1.grid(row=1, column=1)
button_c = tk.Button(root_w, text="分析", width=10, command=sentimentClassify)
button_c.grid(row=2, column=0, sticky="w", padx=10, pady=5)

tk.Label(root_w, text="关键词提取：").grid(row=3)
tk.Label(root_w, text="文本：").grid(row=5)
entry_k = Text(root_w, width=20, height=4, undo=True, autoseparators=False)
entry_k.grid(row=5, column=1)

tk.Label(root_w, text="文本环境：").grid(row=5, column=2, padx=10)
cbox = ttk.Combobox(root_w)
# 使用 grid() 来控制控件的位置
cbox.grid(row=5, column=3)
# 设置下拉菜单中的值
cbox['value'] = ("酒店", "KTV", "美食", "旅游", "健康",
                 "教育", "商业", "房产", "汽车", "生活", "购物", "数码")
cbox.bind("<<ComboboxSelected>>", theCbox)


button_k = tk.Button(root_w, text="提取", width=10, command=sentimentKey)
button_k.grid(row=6, column=0, sticky="w", padx=10, pady=5)

txt = ""
msg = Message(root_w, text=txt, width=60, font=('微软雅黑', 10, 'bold'))
msg.grid(row=7)
root_w.mainloop()
