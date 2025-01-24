class LinkedList:
    def __init__(self):
        self.head = None

    def insert_end(self, value):
        new_node = {'value': value, 'next': None}
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current['next']:
                current = current['next']
            current['next'] = new_node

    def remove_value(self, value):
        while self.head and self.head['value'] == value:
            self.head = self.head['next']

        current = self.head
        while current and current['next']:
            if current['next']['value'] == value:
                current['next'] = current['next']['next']
            else:
                current = current['next']

    def has_triplet(self):
        current = self.head
        count = 1
        while current and current['next']:
            if current['value'] == current['next']['value']:
                count += 1
                if count >= 3:
                    return True
            else:
                count = 1
            current = current['next']
        return False

    def to_list(self):
        result = []
        current = self.head
        while current:
            result.append(current['value'])
            current = current['next']
        return result


def process_input():
    n = int(input())
    # results = []

    for _ in range(n):
        data = input().split()
        lst = LinkedList()
        split_index = data.index('0')
        elements = list(map(int, data[:split_index]))
        value_to_remove = int(data[split_index + 1])

        for element in elements:
            lst.insert_end(element)

        lst.remove_value(value_to_remove)

        if lst.has_triplet():
            print("tripla")
        else:
            print("nada")

process_input()
