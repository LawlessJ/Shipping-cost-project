#Shipping Cost Project#

##A Control flow project##

This project creates a series of functions that dictate various shipping costs from a hypothetical company. There exists a "premium" shipping cost, that is a flat $125.00 cost, a ground shipping cost that charges by rate at adds a flat $20.00 to the cost, and a drone shipping cost that adds 3 times the rate by weight of ground shipping, but has no flat rate. The rates are as follows:

Ground Shipping:
Weight of Package	                   Price per Pound	Flat Charge
2 lb or less	                                   $1.50	$20.00
Over 2 lb but less than or equal to 6 lb	   $3.00	$20.00
Over 6 lb but less than or equal to 10 lb	   $4.00	$20.00
Over 10 lb	                                   $4.75	$20.00

Drone Shipping:
Weight of Package	                   Price per Pound	Flat Charge
2 lb or less	                                   $4.50	$0.00
Over 2 lb but less than or equal to 6 lb	   $9.00	$0.00
Over 6 lb but less than or equal to 10 lb	   $12.00	$0.00
Over 10 lb	                                   $14.25	$0.00

Function ground_ship_cost(weight) takes an item's weight and returns what it will cost for ground shipping.

Function drone_ship_cost(weight) takes an item's weight and returns what it will cost for drone shipping.

Finally, function cheapest_cost(weight) takes an item's weight, and returns to the user a statement clarifying which option will be the least expensive, and tells the user what that least expensive cost will be.

##To test these functions:##
The ground shipping cost of an item weighing 8.4 lbs should be $53.60
The drone shipping cost of an item weighing 1.5 lbs should be $6.75

The cheapest cost of shipping a 4.8 lb item will be ground shipping at $34.40, and should return such with this program.
The cheapest cost of shipping a 41.5 lb item will be the premium shipping option at a flat $125.00, and should report that to the user.
