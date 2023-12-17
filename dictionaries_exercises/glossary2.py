# Glossary part two 6.4, not adding extra entries to glossary

glossary = {
    'string': 'a value consisting of alphabet entries denoted in parentheses',
    'list': 'a item that contains entries wrapped in square brackets',
    'if statement': 'a conditional statement that occurs if the defined value is met',
    'else statement': 'a conditional that occurs if the orginal conditional and other conditionals are not met',
    'loop': 'continuously re-running all code in the block',
}

# Adding for loop to print all glossary keys and their values

for word, definition in glossary.items():
    print(f"\n{word.title()}: {definition}") 

