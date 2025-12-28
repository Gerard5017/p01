class Plant:
    def __init__(self, name, height, age):
        self._name = name
        print(f"Plant created: {name}")
        self._height = 0
        self._age = 0
        self.set_height(height)
        self.set_age(age)

    def get_height(self):
        return self._height

    def get_age(self):
        return self._age

    def set_height(self, new_height):
        if new_height < 0:
            print(f"Invalid operation attempted: height {new_height}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self._height = new_height
            print(f"Height updated: {new_height}cm [OK]")

    def set_age(self, new_age):
        if new_age < 0:
            print(f"Invalid operation attempted: age {new_age} days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self._age = new_age
            print(f"Age updated: {new_age} days [OK]")

    def display_status(self):
        print(f"Current plant: {self._name} ({self._height}cm, {self._age} days)")

if __name__ == "__main__":
    print("=== Garden Security System ===")
    plant = Plant("Rose", -25, 30)
    plant.display_status()