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
    HwyMpgByClass.sort(key=lambda x: x[1])
    return HwyMpgByClass








filepath = "/home/nihal/Desktop/avghwy/files/mpg.csv"
print(calculateAvgHwy(filepath))