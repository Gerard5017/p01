class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

if __name__ == "__main__":
    plant1 = Plant("Rose", 30, 12)
    plant2 = Plant("Sunflower", 150, 60)
    plant3 = Plant("Orchid", 20, 10)
    plant4 = Plant("Cactus", 15, 50)
    print("=== Garden Plant Registry ===")
    print(f"{plant1.name}: {plant1.height}cm, {plant1.age} days old")
    print(f"{plant2.name}: {plant2.height}cm, {plant2.age} days old")
    print(f"{plant3.name}: {plant3.height}cm, {plant3.age} days old")
    print(f"{plant4.name}: {plant4.height}cm, {plant4.age} days old")