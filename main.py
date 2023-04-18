class Bike:
    def __init__(self):
        self.speed = 0
        self.is_on = False

    def turn_on(self):
        self.is_on = True
        print("The bike is now on.")

    def turn_off(self):
        self.is_on = False
        print("The bike is now off.")

    def accelerate(self, speed):
        if self.is_on:
            self.speed += speed
            print(f"The bike is now going {self.speed} mph.")
        else:
            print("You need to turn on the bike first.")

    def brake(self, speed):
        if self.is_on:
            if self.speed - speed < 0:
                self.speed = 0
                print("The bike has stopped.")
            else:
                self.speed -= speed
                print(f"The bike is now going {self.speed} mph.")
        else:
            print("You need to turn on the bike first.")

# Example usage
bike = Bike()
bike.turn_on()
bike.accelerate(10)
bike.brake(5)
bike.accelerate(20)
bike.brake(30)
bike.turn_off()
