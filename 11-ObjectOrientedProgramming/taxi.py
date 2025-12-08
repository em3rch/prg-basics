class TaxiRide:
    def __init__(self, rate_per_km):
        self.rate_per_km = rate_per_km # value in € (e.g. €2)
        self.distance = 0
        self.fare = 0

    def calculate_fare(self, distance):
        self.distance = distance
        self.fare = self.distance * self.rate_per_km
    
    def print_receipt(self):
        print(f"RECEIPT")
        print(f"Distance: {self.distance}\n"
              f"Rate: {self.rate_per_km}\n"
              f"Fare: {self.fare}")
        
        return


def main():
    # your program
    taxi1 = TaxiRide(2)
    taxi1.calculate_fare(100)

    taxi2 = TaxiRide(4)
    taxi2.calculate_fare(400)

    # Receipts
    taxi1.print_receipt()
    print()
    taxi2.print_receipt()




if __name__ == "__main__":
    main()
