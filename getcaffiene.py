def get_caffeine_type(type):
    caffeine_map = {
        'Coffee': '95 mg',
        'RedBull': '125 mg',
        'Tea': '11 mg',
        'Soda': '21 mg'
    }
    caffeine = caffeine_map.get(type, 'Not Found')
    return caffeine

def main():
    drink_type = "Soda"
    caffeine_amount = get_caffeine_type(drink_type)
    print(f"Caffeine amount in {drink_type} is {caffeine_amount}")

if __name__ == "__main__":
    main()
