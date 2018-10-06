# Creating 12 table

Pool_Tables = []
for number in range(1,13):
  Pool_Tables.append(["Table_Number"] * 12)
  Table_Number1 = Pool_Tables[0]


class PoolTable():
    def __init__(self,Table_Number):
        self.Table_Number = Table_Number
        self.Table_Status = False
        self.Check_in = None
        self.Check_Out = None
        self.Total_Time_Played = Total_Time_Played
        self.Cost = Cost
        self.User_Name = User_Name

    def __repr__(self):
         return ("Welcome to Pool Table Game %s") % (self.User_Name)



    def starting_pool_table(self,User_Name):
        self.Table_Status = False
        self.User_Name = Name
        UserInput = input("Please Enter User Name: ")
        if Name == "":
            print ("Welcome to Pool Table Game click proceed to start Game")
        else:
            print ("Please Enter Vaild Name")

    def playing_game(self, Table_Num):
        self.Table_Status = True
        self.Table_Number = Table_Num
        self.Check_In = datetime.datetime.now()
        self.Check_Out= datetime.datetime.now()
        Total_Time_Played = self.Check_Out - self.Check_In
        Total_Time_Played = int(Total_Time_Played.total_seconds() * 1000)
    while True:
        Table = Pool_Tables[Table_Num - 1]

    def ending_game(self, Check_out_Time):
        userInput  = input("Press click C to check out")
        self.Check_Out = Check_out_Time
        self.Table_Status = "Open"
    Print ("This Table is Open now")

    def game_cost(self,Time):
        Cost_Per_Hour == 3
        self.cost = Game_Cost
        self.Total_Time_Played = Time
        if Time >= 1:
            Game_Cost = Time * Cost_Per_Hour
            return Game_Cost
        else:
            return float(Time) * Cost_Per_Hour



        def exit_game(self):
             userinput  = input ("Press q to exit")
        print ("Thanks for playing with us Good Bye")

Pool_Tables.starting_pool_table()
Pool_Tables.ending_game()
Pool_Tables.game_cost()
Pool_Tables.exit_game()
