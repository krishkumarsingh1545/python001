#Make a Car class with methods to start, stop, and display mileage
import time
class Car:
    def __init__(self):
        self.startTime = 0
        self.stopTime = 0
        self.speed = 0
        i = 0
        while True:
            i = int(input('''1. Start the car
2. Give Mileage
3. Exit the car
Input: '''))
            match i:
                case 1:
                    self.start()
                case 2:
                    self.mileage()
                case _:
                    print("Thanks for driving")
                    time.sleep(2)
                    exit

    def start(self):
        self.speed = int(input('''1. 100 Miles/s
2. 200 Miles/s
3. 300 Miles/s
4. 400 Miles/s
Speed: '''))
        
        match self.speed:
            case 1:
                speed = 100
            case 2:
                speed = 200
            case 3:
                speed = 300
            case 4:
                speed = 400
            case _:
                print("Invalid speed")
                exit
            
        
        self.startTime = time.time()
        print("Press any key and enter to stop the car: ")
        if input():
            self.stop()
    
    def stop(self):
        self.stopTime = time.time()
    
    def mileage(self):
        mil = (self.speed*(self.stopTime - self.startTime))
        print(f"Mileage: {mil:.2f} miles")
        

c1 = Car()
