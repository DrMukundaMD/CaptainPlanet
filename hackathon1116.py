checkPercent = 0

#FIXME place holders for objects
class object:
    maxTemp = 0

class crop:
    maxTemp = 0



for n in range(45):
    #FIXME: crop = crop object and object = api data input
    if(crop.maxTemp < object.n.maxTemp && crop.maxTemp < object.n+1.maxTemp && crop.maxTemp < object.n+2.maxTemp):
        for i in range(7):
            sum += object.i.percipitation
        if(sum >= crop.rainPerWeek * 1.2):
            checkPercent += 10/42
        else:
            #FIXME: used for appending error messaging

    else:
        checkPercent += 20/42

    # FIXME: crop = crop object and object = api data input
    if(crop.minTemp > object.n.minTemp && crop.minTemp > object.n+1.minTemp && crop.minTemp > object.n+2.minTemp):
        #FIXME: used for appending  error messaging
    else:
        checkPercent += 20/42


for n in range(39):
    for j in range(7):
        # FIXME: crop = crop object and object = api data input
        if(object.predictedPrecipitation > 0.5):
            sum += object.projectedRainfall

    if(crop.rainFallPerWeek < sum):
        #FIXME: used for appending error messaging
    else:
        checkPercent += 60/39

if(checkPercent < 40):
    #Don't Grow
else if(checkPercent < 70):
    #Grow, but be careful
else:
    #Grow: display remaining error messages