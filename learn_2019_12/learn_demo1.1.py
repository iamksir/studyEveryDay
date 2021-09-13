import time
import tkinter
import tkinter.messagebox
from threading import Thread

def main():
    class DownLoadTaskHandler(Thread):

        def run(self):
            time.sleep(10)
            tkinter.messagebox.showinfo('提示', '下载完成！')
            #启用下载按钮
            button1.config(state=tkinter.NORMAL)

    def download():
        #禁用下载按钮
        button1.config(state=tkinter.DISABLED)
        DownLoadTaskHandler(daemon=True).start()

    def show_about():
        tkinter.messagebox.showinfo('关于', 'Joker')

    top = tkinter.Tk()
    top.title('单线程')
    top.geometry('200x150')
    top.wm_attributes('-topmost', 1)

    panel = tkinter.Frame(top)
    button1 = tkinter.Button(panel, text='下载', command=download)
    button1.pack(side='left')
    button2 = tkinter.Button(panel, text='关于', command=show_about)
    button2.pack(side='right')
    panel.pack(side='bottom')

    tkinter.mainloop()

if __name__ == "__main__":
    main()