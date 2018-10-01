
import datetime

class Pool_Table():
    def __init__(self,Table_Number,Table_Status):
        self.Table_Number = Table_Number
        self.Table_Status = Table_Status

    def __repr__(self):
        return ("Table number is: %s Table Status: %s") % (self.Table_Number, self.Table_Status)

# Creating 12 table
    def Add_Table(self):
        PoolTables = []
        for number in range (0,12):
            Pool_Table.append(["Table Number"] * 12)
            print ("Pool_Table")

class Pool_Table_Manger():

    def __init__(self,Check_In,Check_Out,Total_Time_Played):
        self.Check_in = Check_in
        self.Check_Out = Check_out
        self.Total_Time_Played = Total_Time_Played
        Number_Of_Players = 0

# Define the status of the table
    def Pool_Table_Status(Self,Table_Status):
        if Number_Of_Players > 0:
            print ("Table number %s is Occupied now") % (self.Table_Number)
        else:
            print ("This Table is open")

class Customer():

    def __init__(self,User_Name):
        self.User_Name = User_Name

    def __repr_(self):
        print ("Welcome to Pool Table Game %s") % (self.User_Name)


    def Starting_Pool_Table(self):
        UserInput = input("Please Enter User Name: ")
        UserInput = Int(input("Please select Table number: "))
        for number in len(PoolTables):
            if User_Name == "" and Table_Status =="Not Occupied":
                print ("Welcome to Pool Table Game click proceed to start Game")
            elif Table_Status == "Occupied":
                print ("Table number %s is Occupied now please select different table") % (self.Table_Number)
            else:
                ("Please enter Vaild Name or number without decimal")
            Availability = Pool_Table_Status()
            return Availability


    def PlayingGame(self,Game_Check_in,Game_Check_Out,Total_Time_Played):
        Game_Check_in = datetime.datetime.now()
        Game_Check_Out= datetime.datetime.now()
        Total_Time_Played = Game_Check_Out - Game_Check_in
        print ("Total_Time_Played")
        int(Total_Time_Played.total_seconds() * 1000)

    def GameCost(self,Total_Time_Played_Time,Cost):
        Cost_Per_Hour == 3
        if ("Total_Time_Played >= 1"):
            return Total_Time_Played * Cost_Per_Hour
        else:
            return float("TotalTimePlayed") * Cost_Per_Hour

    def exit_game(self):
        print ("Good Bye")
