# Printing Models 8.15
# Moved functions to this file

def print_models(unprinted_designs, completed_models):
    """Simulate printing each design. 
    Move each completed design to completed_models after printing
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()

        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
     """Display all completed models"""
     print("\nThe following models were printed: ")
     for completed_model in completed_models:
        print(completed_model)