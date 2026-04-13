# Function to track nutrition data for a day, including calories, protein, carbs, and fat
class food_item:
    def __init__(self, name, cal, pro, carb, fat):
        self.name = name
        self.cal = cal
        self.pro = pro
        self.carb = carb
        self.fat = fat

# Function to calculate daily totals of calories, protein, carbs, and fat from a list of food items
def daily_total(food_list):
    total_cal = 0
    total_pro = 0
    total_carb = 0
    total_fat = 0

    for food in food_list:
        total_cal += food.cal
        total_pro += food.pro
        total_carb += food.carb
        total_fat += food.fat

    print("Total cal:", total_cal, "kcal")
    print("Total pro:", total_pro, "g")
    print("Total carb:", total_carb, "g")
    print("Total fat:", total_fat, "g")

    if total_cal > 2500:
        print("Warning: Calories exceed 2500!")

    if total_fat > 90:
        print("Warning: Fat exceeds 90g!")


apple = food_item("Apple", 60, 0.3, 15, 0.5)
Hamburger = food_item("Hamburger", 500, 25, 40, 30)
pizza = food_item("Pizza", 700, 30, 60, 35)

daily_food = [apple, Hamburger, pizza]
daily_total(daily_food)
