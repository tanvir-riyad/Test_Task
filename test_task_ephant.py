import random


class Customer:
    
    def __init__(self, name, money, customer_type):        
        self.name = name
        self.money = money
        self.customer_type = customer_type
        
        
class Restaurant:
    
    def __init__(self, seats, balance):
        self.seats = seats
        self.balance = balance
        
    def pay_costs(self, costs):
        self.balance -= costs
                
        
def generate_random_customers(n):
    
    customers = []
    types_of_customer = ['single', 'pair', 'Family']
    for i in range(n):
        customer_type = random.choice(types_of_customer)
        if customer_type == 'single':
            name = [''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=random.randint(5, 12)))]
            
        elif customer_type == 'pair':
            name = [''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=random.randint(5, 12))), ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=random.randint(5, 12)))]
        
        else:
            family_member = random.randint(3, 6)
            name = [''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=random.randint(5, 12))) for i in range(0, family_member)]
        money = random.randint(50, 100)
        customers.append(Customer(name, money, customer_type))
    return customers


def simulate_interactions(customers, restaurant):

    total_single_customers = sum(customer.customer_type == 'single' for customer in customers)
    total_pair_customers = sum(customer.customer_type == 'pair' for customer in customers)
    per_hour_single_customers = round(total_single_customers * 0.01)
    per_hour_pair_customers =round(total_pair_customers * 0.02)
    per_hour_family_customers = round((len(customers) - (total_single_customers + total_pair_customers))* 0.005)
    per_hour_customer = per_hour_single_customers + per_hour_pair_customers + per_hour_family_customers
    monthly_balance = []
    for i in range(1, 3*30+1):
        num_of_seats = []
        daily_balance = 0
        temp_customers = customers[:]
        random.shuffle(temp_customers)
        for j in range(6):
            single_count = 0
            pair_count = 0
            family_count = 0
            restaurant.seats = 100            
            while True:
                customer = temp_customers.pop()
                if customer.customer_type == "single":        
                    single_count += 1
                    restaurant.seats -= 1
                    customer_expense = random.choice([0, customer.money])
                    restaurant.balance += customer_expense
                    customer.money -= customer_expense
                    daily_balance += customer_expense
                elif customer.customer_type == "pair": 
                    pair_count += 1                  
                    restaurant.seats -= 2
                    customer_expense = random.choice([0, customer.money])
                    restaurant.balance += customer_expense
                    customer.money -= customer_expense
                    daily_balance += customer_expense
                elif customer.customer_type == "Family":
                    family_count += 1                  
                    restaurant.seats -= len(customer.name)
                    customer_expense = random.choice([0, customer.money])
                    restaurant.balance += customer_expense
                    customer.money -= customer_expense
                    daily_balance += customer_expense                    
                if single_count + pair_count + family_count == per_hour_customer:
                    break
            num_of_seats.append(100 - restaurant.seats)
        temp_list = sorted(customers, key=lambda customer: customer.money, reverse = False)
        print('-----------------------------------------------')
        print('Daily statistics : The five customers with highest balance are :')
        print('-----------------------------------------------')
        for i in range(1, 6):
            print(temp_list[-i].name ,' : ', temp_list[-i].money)  
            
            
        print('Minimum number of busy seats daily:', min(num_of_seats))
        print('Daily account state of the restaurant:', daily_balance)
            
        if i % 30 == 0:
            for customer in customers:
                customer.money += random.randint(50, 100) 
            restaurant.balance -= random.randint(100, 500)
            monthly_balance.append(restaurant.balance)
            if i % 60 == 0:
                print('-----------------------------------------------')
                print('Second month account state of the restaurant:', monthly_balance[1] - monthly_balance[0])
                print('-----------------------------------------------')
            elif i % 90 == 0:
                print('-----------------------------------------------')
                print('Third month account state of the restaurant:', monthly_balance[2] - monthly_balance[1])
                print('-----------------------------------------------')
            else:
                print('-----------------------------------------------')
                print('First month account state of the restaurant:', monthly_balance[0])
                print('-----------------------------------------------')
                
    print('The total account state of the restaurant for three months: ', restaurant.balance)
    
    temp_list = sorted(customers, key=lambda customer: customer.money, reverse = False)
    print('-----------------------------------------------')
    print('Total statistics : The five customers with lowest balance are :')
    print('-----------------------------------------------')
    for i in range(5):
        print(temp_list[i].name ,' : ', temp_list[i].money)  

    return restaurant.balance

customers = generate_random_customers(2000)
restaurant = Restaurant(100, 0)
simulate_interactions(customers, restaurant)