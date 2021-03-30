# Aaron Oviedo 1990958

class FoodItem:

    def __init__(self, name="None", fat=0.0, carbs=0.0, protein=0.0):
        self.name = name
        self.fat = fat
        self.carbs = carbs
        self.protein = protein


# implement get_calories() method with single parameter
    def get_calories(self, num_servings):
        # Calorie formula
        calories = ((self.fat * 9) + (self.carbs * 4) + (self.protein * 4)) * num_servings
        return calories  # return calories value


# implement print_info()
    def print_info(self):
        print('Nutritional information per serving of {}:'.format(self.name))
        print('   Fat: {:.2f} g'.format(self.fat))
        print('   Carbohydrates: {:.2f} g'.format(self.carbs))
        print('   Protein: {:.2f} g'.format(self.protein))

if __name__ == "__main__":

    userfood1 = FoodItem()

    item_name = input()
    amount_fat = float(input())
    amount_carbs = float(input())
    amount_protein = float(input())

    userfood2 = FoodItem(item_name, amount_fat, amount_carbs, amount_protein)

    num_servings = float(input())  # read num of servings

    userfood1.print_info()  # calling print_info() method
    print('Number of calories for {:.2f} serving(s): {:.2f}'.format(num_servings, userfood1.get_calories(num_servings)))  # calling get_calories() method
    print()
    userfood2.print_info()  # calling print_info() method
    print('Number of calories for {:.2f} serving(s): {:.2f}'.format(num_servings, userfood2.get_calories(num_servings)))  # calling get_calories() method
