
class Valut:
    def __init__(self, galleons = 0, sickles = 0, knuts=0):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts

    def __str__(self):
        return f"{self.galleons} galleons, {self.sickles} sickles, {self.knuts} knuts"


potter = Valut(100,50,25)
print(potter)

weasley = Valut(25,50,100)
print(weasley)

galleons = potter.galleons + weasley.galleons
sickles = potter.sickles + weasley.sickles
knuts = potter.knuts + weasley.knuts

total = Valut(galleons,sickles,knuts)

print(total)


