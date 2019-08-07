import tkinter as tk

class SSW():
    def createSsw(self):
        smartScriptWindow = tk.Tk()
        smartScriptWindow.title("beat anyone")
        smartScriptWindow.geometry("500x309")
        return smartScriptWindow

    def createLabel(self,smartScriptWindow):
        l = tk.Label(smartScriptWindow,
                     text='OMG! this is TK!',  # 标签的文字
                     bg='green',  # 背景颜色
                     font=('Arial', 12),  # 字体和字体大小
                     width=15, height=2)  # 标签长宽
        return l

if __name__ == '__main__':
    ssw = SSW()
    smartScriptWindow = ssw.createSsw()
    firstLabel = ssw.createLabel(smartScriptWindow)
    firstLabel.pack()
    smartScriptWindow.mainloop()
