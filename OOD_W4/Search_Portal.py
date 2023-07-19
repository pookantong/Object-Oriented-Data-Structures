class Queue:
    def __init__(self) -> None:
        self.__queue = []
        
    def enqueue(self, item):
        self.__queue.append(item)

    def dequeue(self):
        return self.__queue.pop(0) if not self.isEmpty() else None

    def isEmpty(self):
        return len(self.__queue) == 0

    def size(self):
        return len(self.__queue)
    
    @property
    def queue(self):
        return self.__queue

class SearchPortal:
    def __init__(self) -> None:
        self.queue = Queue()
        self.directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    
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
                
    def search(self, room):
        self.queue.enqueue(self.find_start(room))
        if None in self.queue.queue:
            return 'Invalid map input.'
        # Main Loop
        while not self.queue.isEmpty():
            print(f'Queue: {self.queue.queue}')
            if self.find_the_next_way(room):
                return 'Found the exit portal.'
        return 'Cannot reach the exit portal.'      


def check_valid_room(width, height, room):
    for row in room:
        if len(row) != width:
            return False
    return len(room) == height

width, height, room = input('Enter width, height, and room: ').split()
search_portal = SearchPortal()
room = [list(string) for string in room.split(',')]
if check_valid_room(int(width), int(height), room):
    print(search_portal.search(room))
else:
    print('Invalid map input.')
