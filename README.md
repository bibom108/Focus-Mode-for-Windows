# Focus Mode for Windows
I have some trouble in focusing on studying during day time and end up playing video games the whole day :(. So i decide to look online for an application to block a program (or video games) in a specific time but found nothing. I wonder if I'm capable of writing one with that requirement. And here is my journey.
## Kill the process in the given time
First, I need to kill a process with a given name. I look online and found the **os** library can done that.  
Next, I set start time and end time for a focus session and covert it to this formula: _time = hour * 60 + minute_, compared to the current time to decide whether kill the process.  
_Testing ... _  
_The program can kill the game when I try to lanch_  
But then I realised the code in super while loop comsume lots of CPU, I look online for a solution for thing and turn out you need to set sleep time for while loop in order not to crash the program as it comsume CPU.  
Now it works perfectly.  
## The GUI for program
I want to finish this project so i decide to add GUI for user to modify focus session time, add more program blocking list without rebuilding the program again. So i start to look online for GUI guide ...  
