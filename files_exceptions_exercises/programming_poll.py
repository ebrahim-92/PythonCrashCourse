# Programming poll 10.5

program_poll_file = "files_exceptions_exercises/programming_poll.txt"

with open(program_poll_file, "w") as poll:
    while poll:
        people = input("What is your name? ")
        reason = input("Why do you like programming? ")
        poll.write(f"\n{reason}")
        break
    
  


    
