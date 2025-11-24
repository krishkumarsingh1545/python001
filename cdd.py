import time

class Car:
    def __init__(self, speed=0):
        self.speed = speed            # speed in miles per second
        self.start_time = None
        self.stop_time = None

    def start(self, speed):
        """Starts the car and records the start time."""
        self.speed = speed
        self.start_time = time.time()
        print(f"🚗 Car started at {self.speed} miles/sec!")

    def stop(self):
        """Stops the car and records the stop time."""
        if self.start_time is None:
            print("⚠️ Car hasn't started yet!")
            return
        self.stop_time = time.time()
        print("🛑 Car stopped!")

    def mileage(self):
        """Calculates and displays mileage (distance = speed × time)."""
        if self.start_time is None or self.stop_time is None:
            print("⚠️ Start and stop the car first to calculate mileage!")
            return

        duration = self.stop_time - self.start_time   # time in seconds
        distance = self.speed * duration              # miles = miles/sec × sec
        print(f"⏱️ Time driven: {duration:.2f} seconds")
        print(f"📏 Mileage (distance): {distance:.2f} miles")

# Example usage
car1 = Car()
car1.start(200)          # Start the car with 200 miles/sec
time.sleep(3)            # Simulate driving for 3 seconds
car1.stop()              # Stop the car
car1.mileage()           # Display mileage
