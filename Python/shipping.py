pound = int(input("How many pounds is the package?"))

if pound <= 2:
  ground_per_pound = pound * 1.50
  ground_flat_charge = 20
  drone_per_pound = pound * 4.50
  drone_flat_charge = 0
elif pound > 2 and pound <= 6:
  ground_per_pound = pound * 3.00
  ground_flat_charge = 20
  drone_per_pound = pound * 9.00
  drone_flat_charge = 0
elif pound > 6 and pound <= 10:
  ground_per_pound = pound * 4.00
  ground_flat_charge = 20
  drone_per_pound = pound * 12.00
  drone_flat_charge = 0
elif pound > 10:
  ground_per_pound = pound * 4.75
  ground_flat_charge = 20
  drone_per_pound = pound * 14.25
  drone_flat_charge = 0

ground_premium_total = 125

ground_total = ground_per_pound + ground_flat_charge
ground_total = round(ground_total,2)

drone_total = drone_per_pound + drone_flat_charge
drone_total = round(drone_total,2)

if ground_total < drone_total and ground_total < ground_premium_total:
  print("Ground shipping is better: " + str(ground_total))
elif drone_total < ground_total and drone_total < ground_premium_total:
  print("Drone shipping is better: " + str(drone_total))
elif ground_premium_total < ground_total and ground_premium_total < drone_total:
  print("Premium ground shipping is better: " + str(ground_premium_total))
