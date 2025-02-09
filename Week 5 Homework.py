import requests
import psutil

def is_divisible_by_five():
    num = int(input("Enter a number: "))
    if num % 5 == 0:
        print(f"{num} is divisible by 5.")
    else:
        print(f"{num} is not divisible by 5.")

def state_capital_if_else():
    state = input("Enter a state name: ")
    if state == "Oregon":
        print("Salem")
    elif state == "Washington":
        print("Olympia")
    elif state == "Idaho":
        print("Boise")
    elif state == "California":
        print("Sacramento")
    elif state == "Nevada":
        print("Carson City")
    elif state == "Texas":
        print("Austin")
    else:
        print("I do not know that one.")

def state_capital_dictionary():
    states = {
        "Oregon": "Salem",
        "Washington": "Olympia",
        "Idaho": "Boise",
        "California": "Sacramento",
        "Nevada": "Carson City",
        "Texas": "Austin"
    }
    state = input("Enter a state name: ")
    print(states.get(state, "I do not know that one."))

def state_capital_match_case():
    state = input("Enter a state name: ")
    match state:
        case "Oregon":
            print("Salem")
        case "Washington":
            print("Olympia")
        case "Idaho":
            print("Boise")
        case "California":
            print("Sacramento")
        case "Nevada":
            print("Carson City")
        case "Texas":
            print("Austin")
        case _:
            print("I do not know that one.")

def pool_admission(age):
    """Returns the pool admission price based on age."""
    if age < 2:
        return 0
    elif age < 12:
        return 3
    elif age <= 60:
        return 6
    else:
        return 4

def count_160_in_html():
    url = "http://coccbobcat.com"
    try:
        response = requests.get(url)
        response.raise_for_status()
        count = response.text.count("160")
        print(f'The substring "160" appears {count} times in the HTML source of {url}.')
    except requests.RequestException as e:
        print(f"Error fetching the webpage: {e}")

def count_running_processes():
    process_count = len(psutil.pids())
    print(f"Number of running processes: {process_count}")

if __name__ == "__main__":
    is_divisible_by_five()
    state_capital_if_else()
    state_capital_dictionary()
    state_capital_match_case()
    age = int(input("Enter age for pool admission: "))
    print(f"Admission price: {pool_admission(age)}")
    count_160_in_html()
    count_running_processes()
