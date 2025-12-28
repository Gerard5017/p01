class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age
    
class Flower(Plant):
    def __init__(self, name, height, age, color, bloom_state):
        super().__init__(name, height, age)
        self.color = color
        self.bloom_state = bloom_state
    def bloom(self):
        if (self.bloom_state == "yes"):
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} is not in bloom")
    def display_status(self):
        print(f"{self.name} (Flower): {self.height}cm, {self.age} days, {self.color} color")
        self.bloom()

class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter, shade_surface):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        self.shade_surface = shade_surface
    def produce_shade(self):
        print(f"{self.name} provides {self.shade_surface} square meters of shade")
    def display_status(self):
        print(f"{self.name} (Tree): {self.height}cm, {self.age} days, {self.trunk_diameter}cm diameter")
        self.produce_shade()

class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season, nutritional_value):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value
    def display_status(self):
        print(f"{self.name} (Vegetable): {self.height}cm, {self.age} days, {self.harvest_season} harvest")
        print(f"{self.name} is rich in {self.nutritional_value}")

if __name__ == "__main__":
    print("=== Garden Plant Types ===\n")
    
    # Au moins 2 fleurs
    plant1 = Flower("Rose", 25, 30, "white", "yes")
    plant2 = Flower("Tulip", 20, 15, "yellow", "no")
    
    # Au moins 2 arbres
    plant3 = Tree("Maple", 1000, 67, 69, 666)
    plant4 = Tree("Oak", 800, 1825, 80, 500)
    
    # Au moins 2 légumes
    plant5 = Vegetable("Eggplant", 16, 16, "Autumn", "calcium")
    plant6 = Vegetable("Tomato", 50, 60, "Summer", "vitamins")
    
    print("--- Flowers ---")
    plant1.display_status()
    print()
    plant2.display_status()

    print("\n--- Trees ---")
    plant3.display_status()
    print()
    plant4.display_status()
    
    print("\n--- Vegetables ---")
    plant5.display_status()
    print()
    plant6.display_status()