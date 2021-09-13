import time
import tkinter
import tkinter.messagebox

def download():
    #模拟下载任务花费10s
    time.sleep(5)
    # 弹出框要展示的信息，showinfo接收三个参数，title，message，option
    tkinter.messagebox.showinfo('提示', '下载完成！')

def show_about():
    tkinter.messagebox.showinfo('关于', 'Joker')

def main():
    # 生成主窗口
    top = tkinter.Tk()
    # 标题名
    top.title('单线程')
    # 定义窗体的大小
    top.geometry('200x150')
    top.wm_attributes('-topmost', True)

    panel = tkinter.Frame(top)
    button1 = tkinter.Button(panel, text='下载', command=download)
    button1.pack(side='left')
    button2 = tkinter.Button(panel, text='关于', command=show_about)
    button2.pack(side='right')
    panel.pack(side='bottom')
    # 进入消息循环
    tkinter.mainloop()

if __name__ == "__main__":
    main()