class Queue:
    def __init__(self) -> None:
        self.__items = []
        
    def enqueue(self, item):
        self.__items.append(item)

    def dequeue(self):
        return self.__items.pop(0) if not self.isEmpty() else None

    def isEmpty(self):
        return len(self.__items) == 0

    def size(self):
        return len(self.__items)
    
    @property
    def queue(self):
        return self.__items

class SearchPortal:
    def __init__(self) -> None:
        self.queue = Queue()
        self.directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        
    def valid_room(self, width, height, room):
        for row in room:
            if len(row) != width:
                return False
        if None in self.queue.queue:
            return False
        return len(room) == height
    
    # Find Position F    
    def find_start(self, room):
        for row in room:
            if 'F' in row:
                position = (row.index('F'), room.index(row))
                return position
            
    def find_the_next_way(self, room):
        x, y = self.queue.dequeue()
        for dx, dy in self.directions:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_y < len(room) and 0 <= new_x < len(room[0]) and room[new_y][new_x] == 'O':
                return True
            elif 0 <= new_y < len(room) and 0 <= new_x < len(room[0]) and room[new_y][new_x] == '_':
                self.queue.enqueue((new_x, new_y))
                room[new_y][new_x] = 'X'
                
    def search(self, width, height, room):
        self.queue.enqueue(self.find_start(room))
        if not self.valid_room(width, height, room):
            print('Invalid map input.')
            return
        # Main Loop
        while not self.queue.isEmpty():
            print(f'Queue: {self.queue.queue}')
            if self.find_the_next_way(room):
                print('Found the exit portal.')
                return
        return print('Cannot reach the exit portal.')      


width, height, room = input('Enter width, height, and room: ').split()
search_portal = SearchPortal()
room = [list(string) for string in room.split(',')]
search_portal.search(int(width), int(height), room)