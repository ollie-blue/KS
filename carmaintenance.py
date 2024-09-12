# data taken from https://caredge.com/ranks/maintenance/


car_maintenance_cost = {
    'Toyota': 5445,
    'FIAT': 6443,
    'Volkswagen': 6496,
    'Mitsubishi': 6593,
    'Honda': 6684,
    'Mazda': 6836,
    'Hyundai': 7167,
    'Kia': 7254,
    'MINI': 7262,
    'Subaru': 7374,
    'Nissan': 7544,
    'Buick': 8814,
    'Chevrolet': 9369,
    'Dodge': 9696,
    'Chrysler': 9884,
    'GMC': 9944,
    'Ford': 10640,
    'Jeep': 10930,
    'Ram': 23748,
}

car_maintenance_cost = {key.capitalize(): value for key, value in car_maintenance_cost.items()}
print(car_maintenance_cost)
    