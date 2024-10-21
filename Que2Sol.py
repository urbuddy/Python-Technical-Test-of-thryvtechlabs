def calculate_total_income_tax(income):
    """
    Calculate the total income tax based on the defined tax slabs.
    :param income: The total taxable income
    :return: The total tax amount and the breakdown of the tax by slab
    """
    tax = 0
    slab_details = []

    # First slab: Up to ₹2,50,000 -> Nil
    if income <= 250000:
        slab_details.append(("0 - 2.5 lac", income, "Nil", "Nil"))
    else:
        slab_details.append(("0 - 2.5 lac", 250000, "Nil", "Nil"))

    # Second slab: ₹2,50,000 – ₹5,00,000 -> 5%
    if income > 250000:
        taxable_amount = min(income - 250000, 250000)  # Max ₹2,50,000 in this slab
        tax += taxable_amount * 0.05
        slab_details.append(("2.5 - 5 lac", taxable_amount, "5%", taxable_amount * 0.05))

    # Third slab: ₹5,00,000 – ₹10,00,000 -> 20%
    if income > 500000:
        taxable_amount = min(income - 500000, 500000)  # Max ₹5,00,000 in this slab
        tax += taxable_amount * 0.20
        slab_details.append(("5 - 10 lac", taxable_amount, "20%", taxable_amount * 0.20))

    # Fourth slab: Above ₹10,00,000 -> 30%
    if income > 1000000:
        taxable_amount = income - 1000000  # Amount above ₹10,00,000
        tax += taxable_amount * 0.30
        slab_details.append(("Above 10 lac", taxable_amount, "30%", taxable_amount * 0.30))

    return tax, slab_details

def display_tax_breakdown(income, slab_details, total_tax):
    """
    Display the breakdown of the tax calculation.
    :param income: The total taxable income
    :param slab_details: The breakdown of the tax for each slab
    :param total_tax: The total tax amount
    """
    print(f"\nTaxable Income: ₹{income}")
    print(f"{'Slab':<20}{'Amount to Tax':<20}{'Rate (%)':<10}{'Tax Amount (₹)':<15}")
    print("-" * 65)

    for slab in slab_details:
        slab_name, amount, rate, tax = slab
        print(f"{slab_name:<20}{amount:<20}{rate:<10}{tax:<15}")

    print(f"\nTotal Income Tax = ₹{total_tax:.2f}")

def get_user_income():
    """
    Prompt the user for their taxable income with error handling for invalid inputs.
    :return: The user's taxable income as a float
    """
    while True:
        try:
            income = float(input("Enter your taxable income (₹): ").strip())
            if income < 0:
                raise ValueError("Income cannot be negative.")
            return income
        except ValueError as ve:
            print(f"Invalid input: {ve}. Please enter a valid non-negative number.")

def start_income_tax_calculator():
    """
    The main function that drives the income tax calculator application.
    """
    print("Welcome to the Income Tax Calculator!")
    income = get_user_income()
    total_tax, slab_details = calculate_total_income_tax(income)
    display_tax_breakdown(income, slab_details, total_tax)

if __name__ == "__main__":
    start_income_tax_calculator()
