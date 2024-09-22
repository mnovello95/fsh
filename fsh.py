import sys

class Fish:
    def __init__(self, name, ratio):
        self.Name = name
        self.Ratio = ratio
        self.MaxPrice = 0.0

class MichaelBloom:
    def __init__(self, quality, ratio):
        self.Name = quality
        self.Ratio = ratio
        self.MaxPrice = 0.0

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def CalculateMaxPrice(list, market_price):
    for i in list:
        i.MaxPrice = (float(market_price) * 0.95) * i.Ratio
        i.MaxPrice += i.MaxPrice * 0.08

    list.sort(key=lambda x: x.MaxPrice, reverse=False)
    return list

# List Init
FishList = []

FishList.append(Fish("Specular Rainbowfish", 0.82))
FishList.append(Fish("Dilly-Dally Dace    ", 0.82))
FishList.append(Fish("Bloody Perch        ", 0.82))
FishList.append(Fish("Goldengill Trout    ", 0.82))
FishList.append(Fish("Bismuth Bitterling  ", 0.82))
FishList.append(Fish("Dornish Pike        ", 0.82))
FishList.append(Fish("Crystalline Sturgeon", 0.82))
FishList.append(Fish("Roaring Anglerseeker", 1.00))
FishList.append(Fish("Spiked Sea Raven    ", 1.78))
FishList.append(Fish("Quiet River Bass    ", 1.00))

MichaelBloomList = []

MichaelBloomList.append(MichaelBloom("  *  ", 0.95))
MichaelBloomList.append(MichaelBloom(" * * ", 1.25))
MichaelBloomList.append(MichaelBloom("* * *", 1.56))

# End List Init

FilletPrice = 0.0
ChoppedPrice = 0.0

if len(sys.argv) > 1:
    FilletPrice = sys.argv[1]
else:
    print("Error: rerun as fsh.py <Fish market price>")
    sys.exit()

if len(sys.argv) > 2:
    ChoppedPrice = sys.argv[2]

FishList = CalculateMaxPrice(FishList, FilletPrice)
MichaelBloomList = CalculateMaxPrice(MichaelBloomList, ChoppedPrice)

print()
print(f"{bcolors.WARNING}Fish Prices")
print("Raw                     Break Even At")
print(f"------------------------------------{bcolors.ENDC}")
for f in FishList:
    print(" %s | %2.2f" % (f.Name, f.MaxPrice))
print()
print(f"{bcolors.WARNING}Michaelbloom Prices")
print("Quality                 Break Even At")
print(f"------------------------------------{bcolors.ENDC}")
for q in MichaelBloomList:
    print(" %s                | %2.2f" % (q.Name, q.MaxPrice))