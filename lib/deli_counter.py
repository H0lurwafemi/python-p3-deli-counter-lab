katz_deli = []

def take_a_number(queue, name):
    queue.append(name)
    position = len(queue)
    print(f"Welcome, {name}. You are number {position} in line.")

def line(queue):
    if not queue:
        print("The line is currently empty.")
    else:
        line_str = "The line is currently: " + ", ".join([f"{i + 1}. {name}" for i, name in enumerate(queue)])
        print(line_str)

def now_serving(queue):
    if not queue:
        print("There is nobody waiting to be served!")
    else:
        serving_customer = queue.pop(0)
        print(f"Currently serving {serving_customer}.")

# Example usage
take_a_number(katz_deli, "Ada")
take_a_number(katz_deli, "Grace")
take_a_number(katz_deli, "Kent")
line(katz_deli)
now_serving(katz_deli)
line(katz_deli)
take_a_number(katz_deli, "Matz")
line(katz_deli)
now_serving(katz_deli)
line(katz_deli)
