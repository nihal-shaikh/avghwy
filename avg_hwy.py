import csv

def calculateAvgHwy(filepath):
    with open(filepath) as csvfile:
        mpg = list(csv.DictReader(csvfile))
    vehicleclass = set(d['class'] for d in mpg)

    HwyMpgByClass = []

    for t in vehicleclass:
        summpg = 0
        vclasscount = 0
        for d in mpg:
            if (d['class'] == t):
                summpg += float(d['hwy'])
                vclasscount += 1
        HwyMpgByClass.append((t, summpg/vclasscount))
    return HwyMpgByClass

    HwyMpgByClass.sort(key=lambda x: x[1])






filepath = "/home/nihal/Desktop/assigments/files/mpg.csv"
print(calculateAvgHwy(filepath))