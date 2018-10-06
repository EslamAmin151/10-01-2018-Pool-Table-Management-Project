class PoolTable:

    def __init__(self,Table_Number):
        self.Table_Number = Table_Number
        self.Table_Status = "open"


    def __repr__(self):
        return ("Table number is: %s Table Status: %s") % (self.Table_Number, self.Table_Status)

# Creating 12 table
    def table_creation():
         Pool_Tables = []
         for number in range(1,13):
         Pool_Tables.append(PoolTable(number))
         table1 = Pool_Tables[0]
         return Pool_Tables


class PoolTableManger():

def __init__(self,User_Name,Check_In,Check_Out,Total_Time_Played, Cost):
      self.User_Name = User_Name
      self.Check_in = Check_in
      self.Check_Out = Check_out
      self.Total_Time_Played = Total_Time_Played
      self.Cost = Cost
      self.Status = Status


 def __repr_(self):
      print ("Welcome to Pool Table Game %s") % (self.User_Name)


  def starting_pool_table(self):
      UserInput = input("Please Enter User Name: ")
      UserInput = Int(input("Please select Table number: "))
      for number in len(Pool_Tables):
          if User_Name == "" and Table_Status =="Open":
              print ("Welcome to Pool Table Game click proceed to start Game")
          elif Table_Status == "Occupied":
              print ("Table number %s is Occupied now please select different table") % (self.Table_Number)
          else:
              ("Please enter Vaild Name or number without decimal")

    def playing_game(self,Game_Check_in,Game_Check_Out,Total_Time_Played):
       Game_Check_In = datetime.datetime.now()
       Game_Check_Out= datetime.datetime.now()
       Total_Time_Played = Game_Check_Out - Game_Check_in
       print ("Total_Time_Played")
       int(Total_Time_Played.total_seconds() * 1000)

 # Define the status of the table
     def change_status(Self,Table_Status):
         if ("Game_Check_in == True"):
              print ("This Table is Occupied")
         elif (Game_Check_Out == True )
              print ("Table_Number: %s  is Open now") % (self.Table_Number)


      def game_cost(self,Total_Time_Played_Time,Cost):
        Cost_Per_Hour == 3
        if ("Total_Time_Played >= 1"):
            return Total_Time_Played * Cost_Per_Hour
        else:
            return float("TotalTimePlayed") * Cost_Per_Hour

        def ending_game():
         if ("Game_Check_Out == True")
          Print ("Thanks for playing with us")

        def exit_game(self):
         print ("Good Bye")
