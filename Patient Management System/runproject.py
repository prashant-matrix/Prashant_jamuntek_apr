import project
action = "start"
while action != "stop":
    print("Menu Options are insert update delete search stop")
    action = input("Please enter your action or use stop to quit : ")
    hosp = project.Hospital(action)
    hosp.PatientMgmt()
