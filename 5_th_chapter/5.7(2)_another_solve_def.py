def favorite(fruit, favorites):
    if fruit in favorites:
        print(f'I really like {fruit}')
    else:
        print(f"I don't like {fruit}")


favorite_fruits = ['pineapples', 'bananas', 'apples']
favorite('apples', favorite_fruits)
favorite('cherry', favorite_fruits)
favorite('bananas', favorite_fruits)
favorite('watermelon', favorite_fruits)
favorite('pineapples', favorite_fruits)
