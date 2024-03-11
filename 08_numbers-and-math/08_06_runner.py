# If a runner runs 10 miles in 30 minutes and 30 seconds,
# What is their average speed in kilometers per hour?
# (Tip: 1 mile = 1.6 km)

TotalSeconds = ((60 * 30) + 30)       # Total Seconds = Seconds in 30 minutes plus an additional 30 seconds
HourCalc = TotalSeconds / 3600      # Total Seconds from previous divided by total seconds in one hour

Kilometers = 10 * 1.6				# Total Kilometers

AverageSpeed = float(Kilometers / HourCalc)

print(HourCalc)

print("The Average Speed of the runner is " + str(AverageSpeed))
