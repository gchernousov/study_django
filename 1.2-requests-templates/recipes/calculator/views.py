from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    'pepperoni': {
        'тесто, г': 0.5,
        'моцарелла, г': 0.05,
        'томатный соус, г': 0.03,
        'колбаски пепперони, г': 0.1
    }
    # можете добавить свои рецепты ;)
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }

def show_all_recipes(request):
    context = {
        'recipes': DATA,
    }
    return render(request, 'calculator/index.html', context)


def show_ingredients(request, recipe):
    servings = int(request.GET.get('servings', 1))
    dish = DATA[recipe]
    serving_dish = {}
    for ingredient, amount in dish.items():
        serving_dish[ingredient] = amount * servings
    context = {
        'recipe': serving_dish,
        'dish_name': recipe,
    }
    return render(request, 'calculator/recipe.html', context)