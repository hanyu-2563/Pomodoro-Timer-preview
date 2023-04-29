import time

class Timer:
    def __init__(self, work_minutes=25, break_minutes=5, long_break_minutes=25):
        self.work_minutes = work_minutes  
        self.break_minutes = break_minutes  
        self.long_break_minutes = long_break_minutes
        self.is_work = True           
        self.work_start = None          
        self.cycles = 0                 

    def start_work_timer(self):         
        self.work_start = time.time()
        self.is_work = True          

    def stop_work_timer(self):          
        work_end = time.time()          
        work_time = work_end - self.work_start 
        self.is_work = False           
        if work_time < self.work_minutes * 60:        
            time.sleep(self.work_minutes * 60 - work_time) 

    def start_break(self):             
        self.cycles += 1               
        if self.cycles % 4 == 0:        
            self.start_long_break()    
        else:                           
            time.sleep(self.break_minutes * 60)   

        self.is_work = True           
        self.start_work_timer()      

    def start_long_break(self):        
        time.sleep(self.long_break_minutes * 60)

    def start(self):                   
        self.start_work_timer()     

    def stop(self):                   
        self.stop_work_timer()      
        self.start_break()          

timer = Timer()                        
timer.start() 
while True:
    try:                                
        timer.stop()                  
    except KeyboardInterrupt:        
        print('Timer stopped')       
        break