class TV:
    def __init__(self, brand):
        self.brand = brand  # Initialize brand property with the provided brand
        self.channel = 1  # Initialize channel property to default value 1
        self.volume = 50  # Initialize volume property to default value 50
        self.on = False  # Initialize on property to default value False

    def increase_volume(self):
        if self.volume < 100:
            self.volume += 1  # Increase volume by 1 if it's less than 100

    def decrease_volume(self):
        if self.volume > 0:
            self.volume -= 1  # Decrease volume by 1 if it's greater than 0

    def set_channel(self, channel):
        if 1 <= channel <= 50:
            self.channel = channel  # Set channel only if it's within the range 1 to 50

    def reset_tv(self):
        self.channel = 1  # Reset channel to default value 1
        self.volume = 50  # Reset volume to default value 50

    def status(self):
        return f"{self.brand} at channel {self.channel}, volume {self.volume}"  # Return TV status string


class LedTV(TV):
    def __init__(self, brand, screen_thickness, energy_usage, lifespan, refresh_rate):
        super().__init__(brand)  # Call the superclass (TV) constructor
        self.screen_thickness = screen_thickness
        self.energy_usage = energy_usage
        self.lifespan = lifespan
        self.refresh_rate = refresh_rate  

    def display_details(self):
        return f"Screen thickness: {self.screen_thickness}, Energy usage: {self.energy_usage}, Lifespan: {self.lifespan}, Refresh rate: {self.refresh_rate}"  # Return detailed TV features


class PlasmaTV(TV):
    def __init__(self, brand, screen_thickness, energy_usage, lifespan, refresh_rate, viewing_angle, backlight):
        super().__init__(brand)  # Call the superclass (TV) constructor
        self.screen_thickness = screen_thickness
        self.energy_usage = energy_usage
        self.lifespan = lifespan
        self.refresh_rate = refresh_rate
        self.viewing_angle = viewing_angle
        self.backlight = backlight

    def display_details(self):
        return f"Screen thickness: {self.screen_thickness}, Energy usage: {self.energy_usage}, Lifespan: {self.lifespan}, Refresh rate: {self.refresh_rate}, Viewing angle: {self.viewing_angle}, Backlight: {self.backlight}"  # Return detailed TV features


# Example usage
led_tv = LedTV("Sony", "0.5 inches", "Low", "10 years", "120Hz")
print(led_tv.status())
led_tv.increase_volume()
led_tv.set_channel(8)
print(led_tv.status())
print(led_tv.display_details())

plasma_tv = PlasmaTV("Samsung", "1 inch", "Medium", "8 years", "60Hz", "180 degrees", "Yes")
print(plasma_tv.status())
plasma_tv.decrease_volume()
plasma_tv.set_channel(60)  # This should not change the channel
print(plasma_tv.status())
print(plasma_tv.display_details())
