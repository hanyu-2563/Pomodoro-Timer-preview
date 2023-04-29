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
