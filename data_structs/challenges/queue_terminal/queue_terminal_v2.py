def create_student(time: int) -> dict:
    student = dict()
    student['work_time'] = time
    student['next'] = None
    return student

def create_queue(terminal_time: int) -> dict:
    queue = dict()
    queue['begin'] = None
    queue['end'] = None
    queue['terminal_time'] = terminal_time
    queue['spended_time'] = 0
    queue['size'] = 0
    return queue

def insert_student(queue: dict, time: int) -> dict:
    new_student = create_student(time)
    if queue['begin'] is None and queue['end'] is None:
        queue['begin'] = new_student
        queue['end'] = new_student
    else:
        queue['end']['next'] = new_student
        queue['end'] = new_student
    queue['size'] += 1
    return queue

def remove_student(queue: dict) -> dict:
    if queue['begin'] is None:
        return None
    temp = queue['begin']
    queue['begin'] = temp['next']
    if queue['begin'] is None:
        queue['end'] = None
    queue['size'] -= 1
    return temp

def process_queue(terminal_time: int, student_times: list[int]) -> int:
    queue = create_queue(terminal_time)
    for time in student_times:
        queue = insert_student(queue, time)

    while queue['size'] > 0:
        current_student = remove_student(queue)
        if current_student['work_time'] > terminal_time:
            # Process part of the student's work
            queue['spended_time'] += terminal_time
            remaining_time = current_student['work_time'] - terminal_time
            queue = insert_student(queue, remaining_time)
        else:
            # Process the entire remaining work time of the student
            queue['spended_time'] += current_student['work_time']

    return queue['spended_time']

# Leitura da entrada
def main():
    terminal_time = int(input())
    student_times = list(map(int, input().split()))

    # Processamento e saída
    result = process_queue(terminal_time, student_times)
    print(result)

if __name__ == "__main__":
    main()
