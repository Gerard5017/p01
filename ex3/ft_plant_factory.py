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
    plants = [
    {"name": "Rose", "height": 25, "age": 30},
    {"name": "Tulip", "height": 20, "age": 15},
    {"name": "Cactus", "height": 10, "age": 50},
    {"name": "Sunflower", "height": 150, "age": 40},
    {"name": "Orchid", "height": 30, "age": 25},
    {"name": "Lavender", "height": 35, "age": 60},
    {"name": "Daisy", "height": 15, "age": 20},
    {"name": "Lily", "height": 40, "age": 35},
    {"name": "Jasmine", "height": 45, "age": 70},
    {"name": "Violet", "height": 12, "age": 18},
    {"name": "Peony", "height": 50, "age": 90},
    {"name": "Carnation", "height": 30, "age": 45},
    {"name": "Poppy", "height": 25, "age": 22},
    {"name": "Daffodil", "height": 28, "age": 30},
    {"name": "Iris", "height": 35, "age": 40},
    {"name": "Azalea", "height": 60, "age": 120},
    {"name": "Begonia", "height": 20, "age": 35},
    {"name": "Camellia", "height": 70, "age": 150},
    {"name": "Chrysanthemum", "height": 40, "age": 50},
    {"name": "Dahlia", "height": 55, "age": 60},
    {"name": "Fern", "height": 45, "age": 100},
    {"name": "Gardenia", "height": 50, "age": 80},
    {"name": "Hibiscus", "height": 65, "age": 90},
    {"name": "Hyacinth", "height": 22, "age": 25},
    {"name": "Hydrangea", "height": 75, "age": 110},
    {"name": "Magnolia", "height": 120, "age": 200},
    {"name": "Marigold", "height": 18, "age": 30},
    {"name": "Pansy", "height": 10, "age": 15},
    {"name": "Petunia", "height": 25, "age": 40},
    {"name": "Snapdragon", "height": 32, "age": 35},
    {"name": "Zinnia", "height": 28, "age": 38},
    {"name": "Aloe", "height": 35, "age": 180},
    {"name": "Bamboo", "height": 200, "age": 365},
    {"name": "Basil", "height": 30, "age": 45},
    {"name": "Mint", "height": 25, "age": 50},
    {"name": "Rosemary", "height": 40, "age": 90},
    {"name": "Thyme", "height": 15, "age": 60},
    {"name": "Sage", "height": 35, "age": 75},
    {"name": "Parsley", "height": 20, "age": 40},
    {"name": "Cilantro", "height": 18, "age": 30},
    {"name": "Dill", "height": 40, "age": 35},
    {"name": "Oregano", "height": 25, "age": 55}
    ]

    print("=== Plant Factory Output ===")
    i = 0
    for data in plants:
        plant = Plant(data["name"], data["height"], data["age"]) 
        plant.get_info()
        i += 1
    print()
    print(f"Total plants created: {i}")

