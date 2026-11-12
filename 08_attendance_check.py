att_input=input("Enter the names of attendees separated by commas:   ")
attendees=att_input.split(", ")
for person in attendees:
  print("\n" + person + "\n")
  response=input("is this person attending? yes \ No ....").lower()
  if response =="yes":
    print("Attendance confirmed")
  else:
    print("Attendance not confirmed")
  print("----------")
