print('******** Parking Lot ********')

class Stack:
    def __init__(self):
        self.items = []
        
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        res = self.items[-1]
        self.items = self.items[:-1]
        return res
    
    def isEmpty(self):
        if len(self.items) == 0:
            return True
        return False
    
    def size(self):
        return len(self.items)
    
    def __repr__(self) -> str:
        return f'{self.items}'

def parkingLot(max, cars_input, state, target_car):
    max = int(max)
    if cars_input == '0':
        cars = Stack()
    else:
        cars_input = [int(car) for car in cars_input.split(',')]
        cars = Stack()
        for car in cars_input:
            cars.push(car)
    target_car = int(target_car)
    if state == 'arrive':
        if target_car in cars.items:
            print(f'car {target_car} already in soi')
            print(cars)
        elif len(cars.items) == max:
            print(f'car {target_car} cannot arrive : Soi Full')
            print(cars)
        else:
            print(f'car {target_car} arrive! : Add Car {target_car}')
            cars.push(target_car)
            print(cars)
    elif state == 'depart':
        if target_car not in cars.items and len(cars.items) == 0:
            print(f'car {target_car} cannot depart : Soi Empty')
            print(cars)
        elif target_car not in cars.items:
            print(f'car {target_car} cannot depart : Dont Have Car {target_car}')
            print(cars)
        else:
            print(f'car {target_car} depart ! : Car {target_car} was remove')
            temp_cars = Stack()
            for i in range(len(cars)-1, -1, -1):
                if cars.items[i] != target_car:
                    temp_cars.push(cars.pop())
                else:
                    cars.pop()
                    break
            for i in range(len(temp_cars)-1, -1, -1):
                cars.push(temp_cars.items[i])
            print(cars) 
            
    
    

input = input('Enter max of car,car in soi,operation : ').split()
parkingLot(*input)
