class Hospital:
    '''
    Patient Management System
    '''
    def __init__(self,action):
        self.action = action
    
    def PatientMgmt(self):
        if self.action == "insert":
            pid = input("Enter PID : ")
            #Check for duplicate value for PID
            pdf = open("patient.data","r")
            pd = pdf.readlines()
            x = 0

            if len(pd) > 0:

                for sdata in pd:
                    s1 = sdata.find(pid)
                    # print(s1)
                    if s1 >= 0:
                        x = 1
                        #continue
                # print(x)
                if x == 1:
                    print("The Patient ID: ",pid," TAlready exists")
                else:
                    pdf.close()
                    pname = input("Enter Patient Name : ")
                    padd = input("Enter Patient Address : ")
                    pdf = open("patient.data","a") 
                    #pdf.write("\n")         
                    pdf.write(pid + ":" + pname + ":" + padd)
                    pdf.write("\n")
                    pdf.close()
                    
            else:
                pdf.close()
                pname = input("Enter Patient Name : ")
                padd = input("Enter Patient Address : ")
                pdf = open("patient.data","a")   
                #pdf.write("\n")       
                pdf.write(pid + ":" + pname + ":" + padd)
                pdf.write("\n")
                pdf.close()
                #break
        
        
        elif self.action == "delete":
            pid = input("Enter PID : ")
            pdf = open("patient.data","r+")
            pd = pdf.readlines()
            pdf.seek(0)
            for patdata in pd:
                s1 = patdata.find(pid)
                if s1 == 0:
                    print("Patient to Delete: ",patdata)
            
            pd = pdf.readlines()
            pdf.seek(0)
            pdf.truncate()
            
            for data in pd:
                s1 = data.find(pid)
                if s1 != 0:
                    pdf.write(data)
            pdf.close()

        elif self.action == "search":
            pid = input("Enter PID : ")
            pdf = open("patient.data","r")
            pd = pdf.readlines()
            x = 0
            for data in pd:
                s1 = data.find(pid)
                if s1 >= 0:
                    print("Patient is : ",data)
                    pdf.close()
                    x = 1
                    break
            if x == 0:
                print("No Such Patient")
          
        
        elif self.action == "update":
            pid = input("Enter PID : ")
            pdf = open("patient.data","r")
            pd = pdf.readlines()
            x = 0
            for data in pd:
                s1 = data.find(pid)
                if s1 >= 0:
                    print("Patient is : ",data)
                    ndata = input("Enter new data set :")                    
                    pdf.close()
                    
                    pdf = open("patient.data","r+")
                    pd = pdf.readlines()
                    pdf.seek(0)
                    pdf.truncate()

                    for data in pd:
                        s1 = data.find(pid)
                        if s1 != 0:
                            pdf.write(data)        
                            
                    pdf.write(ndata)        
                    pdf.close()
                    
                    
                    x = 1
                    break
            if x == 0:
                print("No Such Patient")
