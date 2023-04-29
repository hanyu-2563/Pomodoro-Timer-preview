import time
import tkinter as tk

work_mins = 25 
short_break_mins = 5
long_break_mins = 15
cycles = 0

# 窗口设置
window = tk.Tk() 
window.title('番茄钟')

# 计时器
def work_timer(): 
    work_sec = work_mins * 60
    for sec in range(work_sec, 0, -1): 
        mins, secs = divmod(sec, 60) 
        time_format = '{:02d}:{:02d}'.format(mins, secs)  
        work_timer_label['text'] = time_format  # 更新时间显示
        window.update()      # 更新GUI
        time.sleep(1)
    start_short_break()      # 短休息

def short_break_timer():
    short_break_sec = short_break_mins * 60 
    for sec in range(short_break_sec, 0, -1):
        mins, secs = divmod(sec, 60)    
        time_format = '{:02d}:{:02d}'.format(mins, secs)
        short_break_timer_label['text'] = time_format
        window.update()
        time.sleep(1)
    start_work()         # 回到工作  

def long_break_timer():
    long_break_sec = long_break_mins * 60
    for sec in range(long_break_sec, 0, -1): 
        mins, secs = divmod(sec, 60)
        time_format = '{:02d}:{:02d}'.format(mins, secs)
        long_break_timer_label['text'] = time_format
        window.update()
        time.sleep(1)
    start_work()        # 回到工作   

# 按钮事件  
def start_work(): 
    global cycles
    cycles += 1
    work_timer_label['text'] = '25:00' 
    short_break_timer_label['text'] = ''
    long_break_timer_label['text'] = ''
    if cycles % 8 == 0:     # 每8次循环有一次长休息
        long_break_timer()
    else:
        work_timer()   # 启动工作计时器

def start_short_break(): 
    short_break_timer_label['text'] = '05:00' 
    work_timer_label['text'] = '' 
    long_break_timer_label['text'] = ''
    short_break_timer()  

def start_long_break():
    long_break_timer_label['text'] = '15:00'
    work_timer_label['text'] = ''
    short_break_timer_label['text'] = '' 
    long_break_timer()   

# GUI布局
work_timer_label = tk.Label(window, text='25:00', font=('Helvetica', 20)) 
work_timer_label.grid(row=0, column=1)

short_break_timer_label = tk.Label(window,  font=('Helvetica', 20))
short_break_timer_label.grid(row=1, column=1)   

long_break_timer_label = tk.Label(window,  font=('Helvetica', 20))  
long_break_timer_label.grid(row=2, column=1)

start_work_button = tk.Button(window, text='工作', command=start_work)
start_work_button.grid(row=0, column=0)  

start_short_break_button = tk.Button(window, text='短休息', command=start_short_break) 
start_short_break_button.grid(row=1, column=0)

start_long_break_button = tk.Button(window, text='长休息', command=start_long_break)  
start_long_break_button.grid(row=2, column=0)

window.mainloop()   