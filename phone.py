class Phone():
    """This is a phone class that can be used for inheritances purposes"""
    def __init__(self, phone_number, color):
        self.phone_number = phone_number
        self.color = color

    def __str__(self):
        return f"This {self.color} phone belongs to {self.phone_number}"

    def call(self, other_number):
        print(f"Calling number: {other_number}")

    def text(self, other_number, message):
        print(f"Sending text to: {other_number}")
        print(message)

    def open_app(self, app_name):
        print(f"Opening {app_name}")

class Android(Phone):
    def __init__(self, phone_number, color):
        super().__init__(phone_number, color)
        self.passcode = None
        self.battery = 50

    def __str__(self):
        return f"Android phone that belong to number {self.phone_number}"

    def set_passcode(self, passcode):
        self.passcode = passcode

    def unlock_phone(self, passcode):
        if passcode == self.passcode:
            print('Phone Unlocked')

    def view_battery_life(self):
        print(f"Battery Life: {self.battery}")

    def charge_phone(self, charging_amount):
        self.battery += charging_amount

        if self.battery > 100:
            self.battery = 100

    def view_phone_number(self):
        print(f"Phone number: {self.phone_number}")

frank_phone = Android('888-777-3333', 'Black')

frank_phone.view_battery_life()
frank_phone.charge_phone(200)
frank_phone.view_battery_life()
frank_phone.view_phone_number()

frank_phone.call("919-282-4343")
frank_phone.text("919-282-4343", "Yo!")
frank_phone.open_app("Zoom")

class IPhone(Phone):
    def __init__(self, phone_number, color):
        super().__init__(phone_number, color)
        self.face_id = None
        self.material = "Aluminum"
        self.model = "12 Max Pro"

    def set_face_id(self, my_face):
        self.face_id = my_face
        print(f"{my_face} is now your Face ID")

    def send_message(self, other_number, message):
        print("------------------------")
        print(f"Sending text to: {other_number}")
        print(f"{message}")
        print("------------------------")

    def back_tap(self):
        print("Screenshot taken!")

    def lock(self):
        print("Phone is now locked")

ruben_phone = IPhone("917-288-4332", "black")

ruben_phone.back_tap()
ruben_phone.set_face_id("myface")
ruben_phone.send_message("555-555-5555","HEY! Answer your phone!")