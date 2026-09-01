variable_outside_function_scope = 7

def print_variable():
    print(f'Inside function: {variable_outside_function_scope}')
 

print_variable()
print(f'Outside function: {variable_outside_function_scope}')