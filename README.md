# Pomodoro-Timer-preview
A Pomodoro Technique timer that implements 25 minutes work/5 minutes short rest cycles, with a long 25 minutes rest every 4 cycles.（test）

# Pomodoro Timer
Pomodoro Timer is a productivity tool that implements the Pomodoro Technique of timed working periods separated by breaks. This readme covers both the command line interface (CLI) version and graphical user interface (GUI) version of the Pomodoro Timer.

## Command Line Interface (CLI) Version
The CLI version is a basic timer that runs in the terminal.

### Features
- 25-minute work timer, 5-minute short rest timer, 15-minute long rest timer every 4 cycles
- Loops continuously between work and rest periods 
- Customizable work and rest durations 
### Usage
1. Install the dependencies:
```
 pip install -r requirements.txt
```
2. Run the timer:
```
 python timer.py
```
3. The timer will start a 25-minute work period. An alert will sound when the work period ends.
4. When the alert sounds, start a 5-minute short rest period. The timer will then start another work period. 
5. A long 15-minute rest period will start after every 4 work-rest cycles. 
6. The cycles will continue looping. Ctrl+C to stop the timer. 

### Customization
You can customize the work, short rest, and long rest durations by changing the `WORK_MINUTES`, `SHORT_BREAK_MINUTES` and `LONG_BREAK_MINUTES` constants in the `clockcommand.py` file.

## Graphical User Interface (GUI) Version
The GUI version has an intuitive visual interface powered by Tkinter.

### Features
- 25-minute work timer, 5-minute short rest timer, 15-minute long rest timer buttons 
- Countdown timer shown for each active timer
- Timer automatically switches between work, short rest and long rest 
- Customizable work, short rest and long rest durations

### Usage
1. Install the requirements: 
```
 pip install -r requirements.txt
```  
2. Run the timer: 
```
 python pomodoro_gui.py
```

3. The GUI will show:
   - Work: Start 25-minute work timer 
   - Short Rest: Start 5-minute short rest timer 
   - Long Rest: Start 15-minute long rest timer (every 4 cycles)
4. Press the buttons to start the respective timers. The countdown will be displayed.
5. The next timer will start automatically once complete. 
6. Repeat the cycles as needed. Close the window to exit.

### Customization
You can customize the work, short rest, and long rest durations by changing the `WORK_MINUTES`, `SHORT_BREAK_MINUTES` and  `LONG_BREAK_MINUTES` variables at the top of the `clockGUI.py` file.

## License
This project is licensed under the MIT License. See LICENSE for details.
This covers the basic information for an open source Pomodoro Timer project on GitHub, including a description, features, usage instructions, customization and licensing details in the readme file. Let me know if you would like me to explain or expand on any part of this. I can also provide suggestions for managing issues, pull requests and other aspects of an open source project if needed. 
