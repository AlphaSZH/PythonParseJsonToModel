import time
class Order:
   def __init__(self, ID, Code, Name, Price, OrderCount, OrderAmount, Status, IsVip, CreateTime):
       self.ID = ID
       self.Code = Code
       self.Name = Name
       self.Price = Price
       self.OrderCount = OrderCount
       self.OrderAmount = OrderAmount
       self.Status = Status
       self.IsVip = IsVip
       self.CreateTime = CreateTime

   @property
   def ID(self):
       return self.ID

   @property
   def Code(self):
       return self.Code

   @property
   def Name(self):
       return self.Name

   @property
   def Price(self):
       return self.Price

   @property
   def OrderCount(self):
       return self.OrderCount

   @property
   def OrderAmount(self):
       return self.OrderAmount

   @property
   def Status(self):
       return self.Status

   @property
   def IsVip(self):
       return self.IsVip

   @property
   def CreateTime(self):
       return self.CreateTime

   @ID.setter
   def ID(self,ID):
       if not isinstance(ID, str) or ID == " " or ID.__len__() <36 or ID.__len__() >36:
           raise TypeError("ID is error!!")
       self.ID = ID

   @Code.setter
   def Code(self,Code):
       if not isinstance(Code, str) or Code == " " or Code.__len__() <1 or Code.__len__() >50:
           raise TypeError("Code is error!!")
       self.Code = Code

   @Name.setter
   def Name(self,Name):
       if not isinstance(Name, str) or Name == " " or Name.__len__() <1 or Name.__len__() >50:
           raise TypeError("Name is error!!")
       self.Name = Name

   @Price.setter
   def Price(self,Price):
       if not isinstance(Price, float) or Price.__str__().__len__() !=8:
           raise TypeError("Price is error!!")
       self.Price = Price

   @OrderCount.setter
   def OrderCount(self,OrderCount):
       if not isinstance(OrderCount, int):
           raise TypeError("OrderCount is error!!")
       self.OrderCount = OrderCount

   @OrderAmount.setter
   def OrderAmount(self,OrderAmount):
       if not isinstance(OrderAmount, float) or OrderAmount.__str__().__len__() !=8:
           raise TypeError("OrderAmount is error!!")
       self.OrderAmount = OrderAmount

   @Status.setter
   def Status(self,Status):
       if not isinstance(Status, int) or Status != 0 and Status != 1:
           raise TypeError("Status is error!!")
       self.Status = Status

   @IsVip.setter
   def IsVip(self,IsVip):
       if not isinstance(IsVip, bool):
           raise TypeError("IsVip is error!!")
       self.IsVip = IsVip

   @CreateTime.setter
   def CreateTime(self,CreateTime):
       if not isinstance(CreateTime, time):
           raise TypeError("CreateTime is error!!")
       self.CreateTime = CreateTime

