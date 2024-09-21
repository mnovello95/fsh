import sys

class Fish:
    def __init__(self, name, ratio):
        self.Name = name
        self.Ratio = ratio
        self.MaxPrice = 0.0

FishList = []

FishList.append(Fish("Specular Rainbowfish", 0.82))
FishList.append(Fish("Dilly-Dally Dace....", 0.82))
FishList.append(Fish("Bloody Perch........", 0.82))
FishList.append(Fish("Goldengill Trout....", 0.82))
FishList.append(Fish("Bismuth Bitterling..", 0.82))
FishList.append(Fish("Dornish Pike........", 0.82))
FishList.append(Fish("Crystalline Sturgeon", 0.82))
FishList.append(Fish("Roaring Anglerseeker", 1.00))
FishList.append(Fish("Spiked Sea Raven....", 1.78))
FishList.append(Fish("Quiet River Bass....", 1.00))

MarketPrice = 0.0
if len(sys.argv) > 1:
    MarketPrice = sys.argv[1]
else:
    print("Error: Rerun script with market price as argument.")
    sys.exit()

# print(str(MarketPrice))
for f in FishList:
    f.MaxPrice = (float(MarketPrice) * 0.95) * f.Ratio
    f.MaxPrice += f.MaxPrice * 0.08

FishList.sort(key=lambda x: x.MaxPrice, reverse=True)
print("Raw                    Break Even At")
print("------------------------------------")
for f in FishList:
    print(" %s...%2.2f" % (f.Name, f.MaxPrice))