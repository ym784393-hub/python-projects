imp=input("Enter your tasks for today separated by a comma : ").split(", ")
done_tasks = []
ongoing_tasks = []

for day in imp:
   print(day)
   may=input(f"did you finish { day } alredy? \n").lower()
   if may == "yes":
    print("\n Nice job")
    done_tasks.append(day)



   else:
    print("\n try not to put it off")
    ongoing_tasks.append(day)
   print("---------")

choise=input("Do you want to see your today's progrees? (yes, no )").lower()
if choise == "no":
    input("please hit Enter to exit ")
else:
   print("""
           ********* Done tasks *******
           """)
   print(done_tasks)
   print("""
           ******* ongoing tasks ********
           """)
   print(ongoing_tasks)
