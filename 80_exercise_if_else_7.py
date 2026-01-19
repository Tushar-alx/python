#write a program to decide which is cheaper approach to go from ahmedabad to delhi. by car or by train. consider person has his own petrol car  and he prefer to travel by 1st class train 

CAR_FUEL_EFFICIENCY = 15.0      # km per litre
CAR_PETROL_PRICE_PER_LITRE = 95.0  # in rupees
TRAIN_TICKET_PRICE = 3500.0     # 1st class ticket price in rupees
DISTANCE_AHMEDABAD_DELHI = 920.0 # distance in km

# Calculate car travel cost
litres_needed = DISTANCE_AHMEDABAD_DELHI / CAR_FUEL_EFFICIENCY
car_cost = litres_needed * CAR_PETROL_PRICE_PER_LITRE

# Calculate train travel cost
train_cost = TRAIN_TICKET_PRICE

 
print(f"Car travel cost: {car_cost}")
print(f"Train travel cost: {train_cost}")

# Decision
if car_cost < train_cost:
    print(">> Car is cheaper!")
else:
    if train_cost < car_cost:
        print(">> Train is cheaper!")
    else:
        print(">> Both options cost the same!")

