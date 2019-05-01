def ground_ship_cost(weight):
  if weight <= 2:
    cost = ((weight * 1.50) + 20)
    return cost
  if weight > 2 and weight <= 6:
    cost = ((weight * 3.00) + 20)
    return cost
  if weight > 6 and weight <=10:
    cost = ((weight * 4.00) + 20)
    return cost
  else:
    cost = ((weight * 4.75) + 20)
    return cost
  
premium_shipping_cost = 125.00

def drone_ship_cost(weight):
  if weight <= 2:
    cost = weight * 4.50
    return cost
  if weight > 2 and weight <= 6:
    cost = weight * 9.00
    return cost
  if weight > 6 and weight <=10:
    cost = weight * 12.00
    return cost
  else:
    cost = weight * 14.75
    return cost

def cheapest_cost(weight):
  cost_1 = ground_ship_cost(weight)
  cost_3 = drone_ship_cost(weight)
  if cost_1 < 125 and cost_1 < cost_3:
    return "The cheapest option is our ground shipping at $" + str(cost_1)
  if cost_1 > 125 and cost_3 > 125:
    return "The cheapest option is our premium shipping, at a flat rate of $125.00"
  if cost_3 < cost_1 and cost_3 < 125:
    return "The cheapest option is our drone shipping rate, at $" + str(cost_3)
  else:
    return "I'm sorry, there's an issue. Please check your weight and try again."
