from pipeline import *
from MathMe import ask_question, generate_message, print_response, model




my_array = [True, True, False, False, True, False, False]

# Initialize index
index = 0

# Iterate through the array using a while loop
while index < len(my_array) and my_array[index]:
    index += 1

# Check if a False value was found
if index < len(my_array):
    print("Index of first False:", index)
else:
    print("No False value found in the array")
    
    
    #superPipeline()


