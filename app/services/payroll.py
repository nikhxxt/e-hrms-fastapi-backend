def calculate_salary(base: float, tax_rate: float, deductions: float) -> float:
    taxed = base * (1 - tax_rate)
    return taxed - deductions
