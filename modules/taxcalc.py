TAX_BRACKETS = [(12570,0.2), (50270,0.4), (125140,0.45)]

def calculate_takehome_income(income: float) -> float:
    takehome = 0
    if (income <= 12_570):
        return income
    takehome += 12570
    remaining = income - 12_570
    if (income <= 50_270):
        return takehome + 0.2*remaining
    takehome += 0.2 * (50_270 - 12_570)
    remaining -= (50_270 - 12_570)
    if (income <= 125_140):
        return takehome + 0.4*remaining
    return takehome + 0.4*(125_140 - 50_270) + 0.45*(income - 125_140)

