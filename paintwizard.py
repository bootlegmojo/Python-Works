#room is 300meters squared
room = int(input("In meters squared how big is the area you want to paint?:"))

class Paint ():
    def __init__ (self, name, litre, price, squaremeters):
        self.name = name
        self.litre = litre
        self.price = price
        self.squaremeters = squaremeters
    
    def printinfo (self):
        print("\nThe ", self.name, "paint contains ",\
         self.litre, "litres for the price of ", self.price,\
          " \nThis paint covers ", self.squaremeters, \
          " square meters per can.")
    
    def waste(self):
        print("\nThe amount of paint wasted with ",self.name , "for your chosen area is ",\
         (format(room % (self.litre * self.squaremeters)/ self.squaremeters,".2f")), "litres.")
    #The below function gives a visualy rounded answer wich is not ideal for money.
    def ppl(self):
      print("price per litre for ", self.name, "is £", (format((self.price / self.litre), ".2f")))
    

cheapomax = Paint ("CheapoMax", 20, 19.99, 10)
averagejoes = Paint ("AverageJoes", 15, 17.99, 11)
duluxourouspaints = Paint("DuluxourusPaints", 10, 25, 20)

cheapomax.printinfo()
averagejoes.printinfo()
duluxourouspaints.printinfo()

cheapomax.waste()
averagejoes.waste()
duluxourouspaints.waste()

cheapomax.ppl()
averagejoes.ppl()
duluxourouspaints.ppl()

