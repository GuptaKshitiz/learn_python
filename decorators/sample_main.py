from logger_decorator import log_function_call

def calculate_sum(a, b):
    print("Entering calculate_sum function...")
    result = a + b
    print(f"Result: {result}")
    print("Exiting calculate_sum function...")
    return result

@log_function_call
def calculate_sum_with_dec(a, b):
    result = a + b
    print(f"Result: {result}")
    return result

print("\n--- Running functions without logging decorator (using logging library) ---")
calculate_sum(5, 3)

print("\n--- Running functions with logging decorator (using logging library) ---")
calculate_sum_with_dec(5, 3)
