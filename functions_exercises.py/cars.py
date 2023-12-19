# Cars 8.14

def car(manufacturer, model_name, **car_info):
    """Build dictionary about car"""
    car_info ['car_manufacturer'] = manufacturer
    car_info['car_model_name'] = model_name
    return car_info

car_information = car('toyota', 'camry', car_color = 'grey', cylinders = '6')
print(car_information)