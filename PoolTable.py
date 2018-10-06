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

    def description(self):
        print ("Welcome to the fun house %s") % (self.User_Name)
        Print ("To start game please Enter s" or q to exit")



    def starting_pool_table(self):
        UserInput = input("Please Enter User Name: ")
        UserInput = input("Please Enter Table_Number: ")
        self.Table_Status = availability
        if availability == False and User_Name ="":
            print "This Table is open now "
            print ("Welcome to Pool Table Game click c to continue")
        else:
            " This Table is Occupied  now please selet different table "



    def playing_game(self, Table_Num):
        self.Table_Status = True
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

Pool_Tables.description()
