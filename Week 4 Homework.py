# CIS 161 Python - Week 4 Homework Solutions

# Historical ice cream price data from BLS (2014-2024)
HISTORICAL_PRICES = {
    2014: {'Jan': 5.022, 'Feb': 4.979, 'Mar': 4.842, 'Apr': 5.011, 'May': 4.911, 'Jun': 4.691, 'Jul': 4.719,
           'Aug': 4.751, 'Sep': 4.987, 'Oct': 4.884, 'Nov': 4.863, 'Dec': 5.041},
    2015: {'Jan': 5.089, 'Feb': 4.955, 'Mar': 4.889, 'Apr': 4.791, 'May': 4.696, 'Jun': 4.620, 'Jul': 4.466,
           'Aug': 4.597, 'Sep': 4.791, 'Oct': 4.626, 'Nov': 4.684, 'Dec': 4.725},
    2016: {'Jan': 4.913, 'Feb': 4.851, 'Mar': 4.850, 'Apr': 4.915, 'May': 4.801, 'Jun': 4.710, 'Jul': 4.691,
           'Aug': 4.710, 'Sep': 4.695, 'Oct': 4.712, 'Nov': 4.615, 'Dec': 4.682},
    2017: {'Jan': 4.834, 'Feb': 4.870, 'Mar': 4.751, 'Apr': 4.659, 'May': 4.631, 'Jun': 4.629, 'Jul': 4.606,
           'Aug': 4.688, 'Sep': 4.648, 'Oct': 4.683, 'Nov': 4.567, 'Dec': 4.758},
    2018: {'Jan': 4.786, 'Feb': 4.670, 'Mar': 4.825, 'Apr': 4.709, 'May': 4.588, 'Jun': 4.656, 'Jul': 4.750,
           'Aug': 4.662, 'Sep': 4.754, 'Oct': 4.864, 'Nov': 4.786, 'Dec': 4.812},
    2019: {'Jan': 4.912, 'Feb': 4.981, 'Mar': 4.791, 'Apr': 4.821, 'May': 4.850, 'Jun': 4.633, 'Jul': 4.674,
           'Aug': 4.682, 'Sep': 4.802, 'Oct': 4.940, 'Nov': 4.935, 'Dec': 4.740},
    2020: {'Jan': 4.824, 'Feb': 4.884, 'Mar': 4.918, 'Apr': 4.941, 'May': 4.934, 'Jun': 5.088, 'Jul': 4.898,
           'Aug': 4.950, 'Sep': 4.944, 'Oct': 4.925, 'Nov': 4.846, 'Dec': 4.927},
    2021: {'Jan': 5.014, 'Feb': 4.937, 'Mar': 4.949, 'Apr': 4.978, 'May': 4.685, 'Jun': 4.886, 'Jul': 4.943,
           'Aug': 4.918, 'Sep': 4.900, 'Oct': 4.952, 'Nov': 4.770, 'Dec': 4.766},
    2022: {'Jan': 4.993, 'Feb': 5.048, 'Mar': 5.059, 'Apr': 5.129, 'May': 5.352, 'Jun': 5.536, 'Jul': 5.621,
           'Aug': 5.638, 'Sep': 5.701, 'Oct': 5.745, 'Nov': 5.724, 'Dec': 5.561},
    2023: {'Jan': 5.809, 'Feb': 5.722, 'Mar': 5.920, 'Apr': 5.950, 'May': 5.807, 'Jun': 5.812, 'Jul': 5.845,
           'Aug': 5.904, 'Sep': 5.959, 'Oct': 6.041, 'Nov': 6.014, 'Dec': 6.015},
    2024: {'Jan': 5.903, 'Feb': 5.885, 'Mar': 5.733, 'Apr': 6.196, 'May': 6.000, 'Jun': 6.137, 'Jul': 6.030,
           'Aug': 6.357, 'Sep': 6.338, 'Oct': 6.295, 'Nov': 6.447, 'Dec': 6.270}
}


def average(num1, num2, num3):
    """
    Calculate the average of three numbers.

    Args:
        num1 (float): First number
        num2 (float): Second number
        num3 (float): Third number

    Returns:
        float: The average of the three numbers
    """
    return (num1 + num2 + num3) / 3


def calculate_dog_years(dog_age):
    """
    Convert a dog's age to human years using the formula:
    human years = 24 + (dog's age - 2) x 4

    Args:
        dog_age (int): The age of the dog in years

    Returns:
        float: The equivalent human years
    """
    if dog_age <= 2:
        return dog_age * 12  # Simplified calculation for young dogs
    else:
        return 24 + (dog_age - 2) * 4


def calculate_car_value(purchase_price, years, car_type):
    """
    Calculate the future value of a car based on its type and years owned.

    Args:
        purchase_price (float): Initial purchase price of the car
        years (int): Number of years to calculate depreciation/appreciation
        car_type (str): Type of car ('German', 'Japanese', or 'Italian')

    Returns:
        float: The calculated value of the car after specified years
    """
    rates = {
        'German': -0.05,  # loses 5% per year
        'Japanese': -0.07,  # loses 7% per year
        'Italian': 0.05  # gains 5% per year
    }

    if car_type not in rates:
        raise ValueError("Invalid car type. Must be 'German', 'Japanese', or 'Italian'")

    rate = rates[car_type]
    final_value = purchase_price * (1 + rate) ** years
    return final_value


def calculate_ice_cream_price(scoops):
    """
    Calculate the price of an ice cream cone based on number of scoops.
    Price = number of scoops x $1.15 + $2.25

    Args:
        scoops (int): Number of ice cream scoops

    Returns:
        float: Total price of the ice cream cone
    """
    return scoops * 1.15 + 2.25


def get_historical_ice_cream_price(month, year):
    """
    Get the historical price of ice cream for a specific month and year.
    Data source: BLS Average Price Data for Ice cream, prepackaged, bulk, regular (1/2 gal)

    Args:
        month (str): Month name (Jan, Feb, etc.)
        year (int): Year (2014-2024)

    Returns:
        float: Historical price of ice cream for the specified month and year

    Raises:
        ValueError: If the month/year combination is not in the database
    """
    if year not in HISTORICAL_PRICES:
        raise ValueError(f"No data available for year {year}")

    if month not in HISTORICAL_PRICES[year]:
        raise ValueError(f"Invalid month. Please use three-letter format (Jan, Feb, etc.)")

    return HISTORICAL_PRICES[year][month]


def calculate_historical_cone_price(month, year, scoops):
    """
    Calculate the price of an ice cream cone for a specific historical period,
    adjusting the base price according to the historical bulk ice cream prices.

    Args:
        month (str): Month name (Jan, Feb, etc.)
        year (int): Year (2014-2024)
        scoops (int): Number of ice cream scoops

    Returns:
        float: Adjusted historical price of the ice cream cone
    """
    # Get the base price for April 2018 (as mentioned in the assignment)
    base_reference_price = HISTORICAL_PRICES[2018]['Apr']

    # Get the actual historical price for the requested month/year
    historical_price = get_historical_ice_cream_price(month, year)

    # Calculate the price adjustment factor
    price_factor = historical_price / base_reference_price

    # Calculate the adjusted cone price
    base_cone_price = calculate_ice_cream_price(scoops)
    adjusted_price = base_cone_price * price_factor

    return adjusted_price


def main():
    # Test average function
    print(f"Average of 7, 5, 9 is: {average(7, 5, 9)}")
    print(f"Average of 6, 6, 7 is: {average(6, 6, 7)}")

    # Test dog age calculator with user input
    print("\nDog's Age calculator:")
    dog_name = input("What is your dog's name? ")
    dog_age = int(input(f"How old is {dog_name}? "))
    human_years = calculate_dog_years(dog_age)
    print(f"Your {dog_name} is {human_years} human years old")

    # Test car value calculator
    car_value = calculate_car_value(30000, 5, 'German')
    print(f"\nThe value of German car will be ${car_value:.2f} after 5 years.")

    # Test ice cream cone calculator
    print("\nIce cream cone price calculator:")
    scoops = int(input("How many scoops would you like? "))
    price = calculate_ice_cream_price(scoops)
    print(f"A {scoops}-scoop cone will cost ${price:.2f}")

    # Extra Credit: Historical ice cream price calculator
    print("\nHistorical ice cream cone price calculator:")
    month = input("Enter month (Jan, Feb, etc.): ")
    year = int(input("Enter year (2014-2024): "))
    scoops = int(input("How many scoops? "))

    try:
        historical_price = calculate_historical_cone_price(month, year, scoops)
        print(f"A {scoops}-scoop cone would have cost ${historical_price:.2f} in {month} {year}")

        # Show comparison to current price
        current_price = calculate_ice_cream_price(scoops)
        print(f"Compare to today's price: ${current_price:.2f}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()