from .models import CarMake, CarModel

def initiate():
    car_make_data = [
        {"name":"NISSAN", "description":"Great cars. Japanese technology"},
        {"name":"Mercedes", "description":"Great cars. German technology"},
        {"name":"Audi", "description":"Great cars. German technology"},
        {"name":"Kia", "description":"Great cars. Korean technology"},
        {"name":"Toyota", "description":"Great cars. Japanese technology"},
    ]

    car_make_instances = []
    for data in car_make_data:
            car_make_instances.append(CarMake.objects.create(name=data['name'], description=data['description']))


    # Create CarModel instances with the corresponding CarMake instances
    car_model_data = [
      {"name":"Pathfinder", "model_type":"SUV", "year": 2023, "car_make":car_make_instances[0]},
      {"name":"Qashqai", "model_type":"SUV", "year": 2023, "car_make":car_make_instances[0]},
      {"name":"XTRAIL", "model_type":"SUV", "year": 2023, "car_make":car_make_instances[0]},
      {"name":"A-Class", "model_type":"SUV", "year": 2023, "car_make":car_make_instances[1]},
      {"name":"C-Class", "model_type":"SUV", "year": 2023, "car_make":car_make_instances[1]},
      {"name":"E-Class", "model_type":"SUV", "year": 2023, "car_make":car_make_instances[1]},
      {"name":"A4", "model_type":"SUV", "year": 2023, "car_make":car_make_instances[2]},
      {"name":"A5", "model_type":"SUV", "year": 2023, "car_make":car_make_instances[2]},
      {"name":"A6", "model_type":"SUV", "year": 2023, "car_make":car_make_instances[2]},
      {"name":"Sorrento", "model_type":"SUV", "year": 2023, "car_make":car_make_instances[3]},
      {"name":"Carnival", "model_type":"SUV", "year": 2023, "car_make":car_make_instances[3]},
      {"name":"Cerato", "model_type":"Sedan", "year": 2023, "car_make":car_make_instances[3]},
      {"name":"Corolla", "model_type":"Sedan", "year": 2023, "car_make":car_make_instances[4]},
      {"name":"Camry", "model_type":"Sedan", "year": 2023, "car_make":car_make_instances[4]},
      {"name":"Kluger", "model_type":"SUV", "year": 2023, "car_make":car_make_instances[4]},
      # Add more CarModel instances as needed
    ]

    for data in car_model_data:
            CarModel.objects.create(name=data["name"], car_make=data["car_make"],
                                    model_type=data["model_type"], year=data["year"])
