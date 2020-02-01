from tkinter import ttk
import tkinter
import win32ui
import win32con
import tkinter.messagebox
import tkinter.filedialog
import pyperclip
import time
import random

t_ground_color_on = ('blue','black','deeppink','cyan','yellow','orangered','white','gray')
t_ground_color = {'蓝色':0,'黑色':1,'桃红':2,'青色':3,'黄色':4,'橘红色':5,'白色':6,'灰色':7}
t_ground_color_t = ('蓝色','黑色','桃红','青色','黄色','橘红色','白色','灰色')
tgc = 0

t_t_color_on = ('white','blue','black','deeppink','cyan','yellow','orangered','gray')
t_t_color = {'白色':0,'蓝色':1,'黑色':2,'桃红':3,'青色':4,'黄色':5,'橘红色':6,'灰色':7}
t_t_color_t = ('白色','蓝色','黑色','桃红','青色','黄色','橘红色','灰色')
ttc = 0

t_f_color_on = ('black','blue','deeppink','cyan','yellow','orangered','white','gray')
t_f_color = {'黑色':0,'蓝色':1,'桃红':2,'青色':3,'黄色':4,'橘红色':5,'白色':6,'灰色':7}
t_f_color_t = ('黑色','蓝色','桃红','青色','黄色','橘红色','白色','灰色')
tfc = 0

font = ('楷体',10)
dlg = win32ui.CreateFontDialog(None,win32con.CF_EFFECTS|win32con.CF_SCREENFONTS,None,None)

file_text = ''
file_name = ''
this_file = ''
mst = ''
file = None
save = 0

root=tkinter.Tk()
root.state('zoomed')
root.title('NanShan ETNR. Notepad')

f=tkinter.Frame(root)
s1 = tkinter.Scrollbar(f,orient=tkinter.VERTICAL)
s2 = tkinter.Scrollbar(f,orient=tkinter.HORIZONTAL)
b1 = tkinter.Text(f,width=1366,height=768,wrap=tkinter.NONE,yscrollcommand=s1.set,xscrollcommand=s2.set,undo=True,fg=t_f_color_on[tfc],selectbackground=t_ground_color_on[tgc],selectforeground=t_t_color_on[ttc],font=font)
s1.pack(side=tkinter.RIGHT,fill=tkinter.Y) 
s1.config(command=b1.yview)
s2.pack(side=tkinter.BOTTOM,fill=tkinter.X) 
s2.config(command=b1.xview)
b1.pack(fill=tkinter.BOTH)
f.pack()

def exit_win(*args):
     global b1
     if b1.get('0.0','end') != '\n':
          ass = tkinter.messagebox.askokcancel('NanShan ETNR. Notepad','您确定要关闭 NanShan ETNR. Notepad 吗？')
          if ass == True:
               exit()
          else:
               pass
     else:
          exit()

def copy(*args):
     global b1
     b1.event_generate("<<Copy>>")

def paste(*args):
     global b1
     b1.event_generate("<<Paste>>")

def cut(*args):
     global b1
     b1.event_generate("<<Cut>>")

def new_text(*args):
     global b1
     global save
     if b1.get('0.0','end') != '\n':
          if save == 0:
               ass = tkinter.messagebox.askokcancel('NanShan ETNR. Notepad','您的文件未保存，您确定要新建文本文档吗？')
          else:
               ass = True
          if ass == True:
               b1.delete('0.0','end')
               save = 0
          else:
               pass
     else:
          pass

def open_text(*args):
     global b1
     global s1
     global s2
     global f
     global file
     global save
     global file_text
     global file_name
     global this_file
     file_name = tkinter.filedialog.askopenfilename(title='NanShan ETNR. Notepad',filetypes=[('Text file','*.txt'),('NanShan ETNR. Notepad file','*.nsnp'),('All files','*')])
     this_file = file_name
     root.title('NanShan ETNR. Notepad --'+file_name)
     file = open(file_name,'r',encoding='UTF-8')
     file_text = file.read()
     if b1.get('0.0','end') != '\n':
          if save == 0:
               ass = tkinter.messagebox.askokcancel('NanShan ETNR. Notepad','您的文件未保存，您确定要打开这个文本文档吗？')
          if ass == True:
               s1.pack_forget()
               s2.pack_forget()
               b1.pack_forget()
               f.pack_forget()
               f=tkinter.Frame(root)
               s1 = tkinter.Scrollbar(f,orient=tkinter.VERTICAL)
               s2 = tkinter.Scrollbar(f,orient=tkinter.HORIZONTAL)
               b1 = tkinter.Text(f,width=1366,height=768,wrap=tkinter.NONE,yscrollcommand=s1.set,xscrollcommand=s2.set,undo=True,fg=t_f_color_on[tfc],selectbackground=t_ground_color_on[tgc],selectforeground=t_t_color_on[ttc],font=font)
               s1.pack(side=tkinter.RIGHT,fill=tkinter.Y) 
               s1.config(command=b1.yview)
               s2.pack(side=tkinter.BOTTOM,fill=tkinter.X) 
               s2.config(command=b1.xview)
               b1.pack(fill=tkinter.BOTH)
               f.pack()
               b1.insert(tkinter.INSERT,file_text)
          else:
               pass
     else:
          s1.pack_forget()
          s2.pack_forget()
          b1.pack_forget()
          f.pack_forget()
          f=tkinter.Frame(root)
          s1 = tkinter.Scrollbar(f,orient=tkinter.VERTICAL)
          s2 = tkinter.Scrollbar(f,orient=tkinter.HORIZONTAL)
          b1 = tkinter.Text(f,width=1366,height=768,wrap=tkinter.NONE,yscrollcommand=s1.set,xscrollcommand=s2.set,undo=True,fg=t_f_color_on[tfc],selectbackground=t_ground_color_on[tgc],selectforeground=t_t_color_on[ttc],font=font)
          s1.pack(side=tkinter.RIGHT,fill=tkinter.Y) 
          s1.config(command=b1.yview)
          s2.pack(side=tkinter.BOTTOM,fill=tkinter.X) 
          s2.config(command=b1.xview)
          b1.pack(fill=tkinter.BOTH)
          f.pack()
          b1.insert(tkinter.INSERT,file_text)
     file.close()

def saveas_text(*args):
     global save
     global b1
     global file
     global file_text
     global file_name
     global this_file
     save = 1
     if file_name == '':
          file_name = tkinter.filedialog.asksaveasfilename(title='NanShan ETNR. Notepad',filetypes=[('Text file','*.txt')])
          this_file = file_name
          file = open(file_name+'.txt','w',encoding='UTF-8')
          file_text = file.write(b1.get('0.0','end'))
          file.close()
     else:
          this_file = file_name
          file = open(file_name+'.txt','w',encoding='UTF-8')
          file_text = file.write(b1.get('0.0','end'))
          file.close()

def font(*args):
     global dlg
     global font
     global s1
     global s2
     global b1
     global f
     global file_text
     file_text = b1.get('0.0','end')
     font1 = ['楷体',10]
     dlg.DoModal()
     s1.pack_forget()
     s2.pack_forget()
     b1.pack_forget()
     f.pack_forget()
     del s1
     del s2
     del b1
     del f
     a = dlg.GetCharFormat()
     font1[0] = a[7]
     font1[1] = (a[2]) / 20
     font = (font1[0],int(font1[1]))
     f=tkinter.Frame(root)
     s1 = tkinter.Scrollbar(f,orient=tkinter.VERTICAL)
     s2 = tkinter.Scrollbar(f,orient=tkinter.HORIZONTAL)
     b1 = tkinter.Text(f,width=1366,height=768,wrap=tkinter.NONE,yscrollcommand=s1.set,xscrollcommand=s2.set,undo=True,fg=t_f_color_on[tfc],selectbackground=t_ground_color_on[tgc],selectforeground=t_t_color_on[ttc],font=font)
     s1.pack(side=tkinter.RIGHT,fill=tkinter.Y) 
     s1.config(command=b1.yview)
     s2.pack(side=tkinter.BOTTOM,fill=tkinter.X) 
     s2.config(command=b1.xview)
     b1.pack(fill=tkinter.BOTH)
     f.pack()
     b1.insert(tkinter.INSERT,file_text)

def tur(*args):
     global b1
     global mst
     global s1
     global s2
     global f
     mst = ''
     turr = tkinter.Tk()
     turr.title('格式纠正')
     turr.geometry('220x100+600+200')
     turr.resizable(0,0)
     #turr.overrideredirect(True)            #去除菜单栏
     #turr.configure(background='black')     #调节背景颜色
     
     def twotab(*args):
          mst = b1.get('0.0','end')
          mst = '  ' + mst
          mst = mst.replace('\n','\n  ')
          window = tkinter.Tk()
          window.title('格式纠正')
          window.geometry('630x150')
          tkinter.Label(window, text='进度:', ).place(x=50, y=60)
          canvas = tkinter.Canvas(window, width=465, height=22, bg="white")
          canvas.place(x=110, y=60)
          fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
          x = 50
          n = 465 / x
          for i in range(x):
               n = n + 465 / x
               canvas.coords(fill_line, (0, 0, n, 60))
               window.update()
               time.sleep(0.02)
          fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="white")
          x = 5
          n = 465 / x
          for t in range(x):
               n = n + 465 / x
               canvas.coords(fill_line, (0, 0, n, 60))
               window.update()
               time.sleep(0)
          window.destroy()
          turr.destroy()
          b1.delete('1.0','end')
          b1.insert(tkinter.INSERT,mst)
          return
     def oneokay(*args):
          '''
          q = []
          jtt = ''
          '''
          mst = b1.get('0.0','end')
          '''
          for i in mst:        #遍历出首行
               q.append(i)
               if i == '\n':
                    break
          for i in mst:        #将原字符串的首行去掉
               mst = mst.replace(i,'')
               if i == '\n':
                    break
          for i in q:          #存储首行的列表变字符串
               jtt = jtt + i
          jtt = jtt.center(200) #居中处理
          mst = jtt + mst      #拼接居中后的首行与内容
          '''
          mst = '                                                                         ' + mst
          window = tkinter.Tk()
          window.title('格式纠正')
          window.geometry('630x150')
          tkinter.Label(window, text='进度:', ).place(x=50, y=60)
          canvas = tkinter.Canvas(window, width=465, height=22, bg="white")
          canvas.place(x=110, y=60)
          fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
          x = 50
          n = 465 / x
          for i in range(x):
               n = n + 465 / x
               canvas.coords(fill_line, (0, 0, n, 60))
               window.update()
               time.sleep(0.02)
          fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="white")
          x = 5
          n = 465 / x
          for t in range(x):
               n = n + 465 / x
               canvas.coords(fill_line, (0, 0, n, 60))
               window.update()
               time.sleep(0)
          window.destroy()
          turr.destroy()
          b1.delete('1.0','end')
          b1.insert(tkinter.INSERT,mst)
          return
     def goto(*args):
          mst = b1.get('0.0','end')
          mst = '*** NanShan ETNR. Notepad ***\n' + '                                                                                    ' + ('  ' + mst.replace('\n','\n  ')) + '\n*** NanShan ETNR. Notepad ***'
          window = tkinter.Tk()
          window.title('格式纠正')
          window.geometry('630x150')
          tkinter.Label(window, text='进度:', ).place(x=50, y=60)
          canvas = tkinter.Canvas(window, width=465, height=22, bg="white")
          canvas.place(x=110, y=60)
          fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
          x = 50
          n = 465 / x
          for i in range(x):
               n = n + 465 / x
               canvas.coords(fill_line, (0, 0, n, 60))
               window.update()
               time.sleep(0.02)
          fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="white")
          x = 5
          n = 465 / x
          for t in range(x):
               n = n + 465 / x
               canvas.coords(fill_line, (0, 0, n, 60))
               window.update()
               time.sleep(0)
          window.destroy()
          turr.destroy()
          b1.delete('1.0','end')
          b1.insert(tkinter.INSERT,mst)
          return
   
     button1 = tkinter.Button(turr,text='行首空两格',command=twotab)
     button1.pack()
     button2 = tkinter.Button(turr,text='首行居中',command=oneokay)
     button2.pack()
     button3 = tkinter.Button(turr,text='自动格式纠正（不推荐使用）',command=goto)
     button3.pack()
     turr.mainloop()

def init(file_text,ggg,ttt,fff):
     f=tkinter.Frame(root)
     s1 = tkinter.Scrollbar(f,orient=tkinter.VERTICAL)
     s2 = tkinter.Scrollbar(f,orient=tkinter.HORIZONTAL)
     b1 = tkinter.Text(f,width=1366,height=768,wrap=tkinter.NONE,yscrollcommand=s1.set,xscrollcommand=s2.set,undo=True,fg=fff,selectbackground=ggg,selectforeground=ttt,font=font)
     s1.pack(side=tkinter.RIGHT,fill=tkinter.Y) 
     s1.config(command=b1.yview)
     s2.pack(side=tkinter.BOTTOM,fill=tkinter.X) 
     s2.config(command=b1.xview)
     b1.pack(fill=tkinter.BOTH)
     f.pack()
     b1.insert(tkinter.INSERT,file_text)

def color(event=''):
     global s1
     global s2
     global b1
     global f
     global root
     global init
     global t_ground_color_t
     global t_t_color_t
     global t_f_color_t
     global t_ground_color_t_on
     global t_t_color_t_on
     global t_f_color_t_on
     global tgc
     global ttc
     global tfc
     file_text = b1.get('0.0','end')
     def ok(event=''):
          t_ground_color_on = ('blue','black','deeppink','cyan','yellow','orangered','white','gray')
          t_t_color_on = ('white','blue','black','deeppink','cyan','yellow','orangered','gray')
          t_f_color_on = ('black','blue','deeppink','cyan','yellow','orangered','white','gray')
          tgc = t_ground_color[comboxlist1.get()]
          ttc = t_t_color[comboxlist2.get()]
          tfc = t_f_color[comboxlist3.get()]
          print(str(tgc)+' '+str(ttc)+' '+str(tfc))
          print(str(comboxlist1.get())+' '+str(comboxlist2.get())+' '+str(comboxlist3.get()))
          print(str(type(comboxlist1.get())))
          print(str(type(t_f_color_on[tfc])))
          print(str(' f '+t_f_color_on[tfc])+' t '+str(t_t_color_on[ttc])+' g '+str(t_ground_color_on[tgc]))
          init(file_text,t_ground_color_on[tgc],t_t_color_on[ttc],t_f_color_on[tfc])
     def cancel(event=''):
          wind.destroy()
     wind=tkinter.Tk()
     wind.title('字体颜色')
     label1 = tkinter.Label(wind,text='选中后的背景颜色')
     label1.pack()
     comvalue1 = tkinter.StringVar()
     comboxlist1 = ttk.Combobox(wind,textvariable=comvalue1)
     comboxlist1["values"] = t_ground_color_t
     comboxlist1.current(0)
     comboxlist1.pack()
     comboxlist1.bind("<<ComboboxSelected>>",ok)
     label2 = tkinter.Label(wind,text='选中后的文字颜色')
     label2.pack()
     comvalue2 = tkinter.StringVar()
     comboxlist2 = ttk.Combobox(wind,textvariable=comvalue2)
     comboxlist2["values"] = t_t_color_t
     comboxlist2.current(0)
     comboxlist2.pack()
     comboxlist2.bind("<<ComboboxSelected>>",ok)
     label3 = tkinter.Label(wind,text='字体颜色')
     label3.pack()
     comvalue3 = tkinter.StringVar()
     comboxlist3 = ttk.Combobox(wind,textvariable=comvalue3)
     comboxlist3["values"] = t_f_color_t
     comboxlist3.current(0)
     comboxlist3.pack()
     comboxlist3.bind("<<ComboboxSelected>>",ok)
     button2 = tkinter.Button(wind,text='确定',command=cancel)
     button2.pack()
     button3 = tkinter.Button(wind,text='取消',command=cancel)
     button3.pack()

menu = tkinter.Menu(root)
submenu = tkinter.Menu(menu, tearoff=0)
submenu.add_command(label="新建(Ctrl+N)",command=new_text)
submenu.add_command(label="打开(Ctrl+O)",command=open_text)
submenu.add_command(label="另存为(Ctrl+S)",command=saveas_text)
submenu.add_command(label="关闭(Ctrl+E)",command=exit_win)
menu.add_cascade(label="文件", menu=submenu)
submenu = tkinter.Menu(menu, tearoff=0)
submenu.add_command(label="复制(Ctrl+C)",command=copy)
submenu.add_command(label="粘贴(Ctrl+P)",command=paste)
submenu.add_command(label="剪切(Ctrl+X)",command=cut)
menu.add_cascade(label="编辑", menu=submenu)
submenu = tkinter.Menu(menu, tearoff=0)
submenu.add_command(label="字体（该版本不支持在字体选择中使用颜色调节与样式调节）(Ctrl+F)",command=font)
submenu.add_command(label="格式纠正(Ctrl+G)",command=tur)
#submenu.add_command(label="字体颜色",command=color)
menu.add_cascade(label="格式", menu=submenu)
root.config(menu=menu)

b1.bind_all('<Control-KeyPress-e>',exit_win,'')
b1.bind_all('<Control-KeyPress-x>',cut,'')
b1.bind_all('<Control-KeyPress-p>',paste,'')
b1.bind_all('<Control-KeyPress-c>',copy,'')
b1.bind_all('<Control-KeyPress-n>',new_text,'')
b1.bind_all('<Control-KeyPress-o>',open_text,'')
b1.bind_all('<Control-KeyPress-s>',saveas_text,'')
b1.bind_all('<Control-KeyPress-f>',font,'')
b1.bind_all('<Control-KeyPress-g>',tur,'')
root.protocol("WM_DELETE_WINDOW",exit_win)



root.mainloop()
