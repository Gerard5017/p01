class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.ages = age
    def grow(self, x):
        self.height += x
    def age(self, x):
        self.ages += 1
        self.grow(x)
    def get_info(self):
        print(f"{self.name}: {self.height}cm, {self.ages} days old")

if __name__ == "__main__":
    plant = Plant("Rose", 25, 30)
    start_height = plant.height
    for i in range(1, 8):
        print(f"=== Day {i} ===")
        plant.get_info()
        end_height = plant.height
        plant.age(1)
    print(f"Growth this week: *{end_height - start_height}cm")
