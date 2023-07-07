
def total(gallos,slary,knut):
    return (gallos*10 + slary) * 17 + knut 

coins = {"gallos":20,"slary":50,"knut":10}

print(total(**coins))