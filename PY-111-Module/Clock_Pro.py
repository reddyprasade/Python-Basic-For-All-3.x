""" 
The class Clock is used to simulate a clock.
"""
class Clock(object):
    
    
    def __init__(self,hours,minutes,seconds):
        """
        The  Parmenter hours,minutes,seconds have to be 
        integers and must satisfy the following equations:
        0 <= h < 24
        0 <= m < 60
        0 <= s < 60
        """
        self.set_Clock(hours, minutes, seconds)
      
    
    
    def set_Clock(self,hours,minutes,seconds):
        """
        The  Parmenter hours,minutes,seconds have to be 
        integers and must satisfy the following equations:
        0 <= h < 24
        0 <= m < 60
        0 <= s < 60
        """
        if type(hours) == int and 0 <= hours and hours < 24:
            self.hours = hours
        else:
            raise TypeError("Hours should be integer between 0 to 24")
        if type(minutes) == int and 0 <= minutes and minutes < 60:
            self.minutes = minutes 
        else:
            raise TypeError("Minutes have to be integers between 0 and 59!")
        if type(seconds) == int and 0 <= seconds and seconds < 60:
            self.seconds = seconds
        else:
            raise TypeError("Seconds have to be integers between 0 and 59!")
    
    def __str__(self):
        return "{0:02d}:{1:02d}:{2:02d}".format(self.hours,
                                                self.minutes,
                                                self.seconds)
    def  tick(self):
        """
        This method lets the clock "tick", this means that the 
        internal time will be advanced by one second."""
        if self.seconds == 59:
            self.seconds = 0
            if self.minutes == 59:
                self.minutes = 0
                if self.hours == 23:
                    self.hours = 0
                else:
                    self.hours += 1
            else:
                self.minutes += 1
        else:
            self.seconds += 1
            
if __name__ == "__main__":
    x = Clock(23,59,59)
    print(x)
    
