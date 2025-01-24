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
    queue['size'] += 1
  else:
    queue['end']['next'] = new_student
    queue['end'] = new_student
    queue['size'] += 1

  return queue

def remove_student(queue: dict) -> dict:
  if queue['begin'] is None and queue['end'] is None:
    return None
  elif queue['begin'] == queue['end']:
    temp = queue['begin']
    queue['begin'] = None
    queue['end'] = None
    temp['next'] = None
    queue['size'] -= 1
    return temp
  else:
    temp = queue['begin']
    queue['begin'] = temp['next']
    queue['size'] -= 1 
    return temp


terminal_time = int(input())
queue = create_queue(terminal_time)
student_times = input().split(' ')

for time in student_times:
    queue = insert_student(queue, int(time))

while(queue['size'] >= 1):
  print('Tamanho atual da fila', queue['size'])
  print(queue)
  print('-------------------')
  atual_student = remove_student(queue)
  if(queue['size'] > 1):
    if atual_student['work_time'] > terminal_time:
      print('Aluno ainda precisa de cpu')
      print('Tempo atual do trabalho: ',  atual_student['work_time'])
      queue = insert_student(queue, (atual_student['work_time'] - terminal_time))
      queue['spended_time'] += queue['terminal_time']
      print('Novo tempo do trabalho: ', queue['end']['work_time'])
      print('Tempo gasto até agora:', queue['spended_time'])
    else:
      print('Aluno finalizou ou vai finalizar o trabalho')
      print('Tempo atual do trabalho: ',  atual_student['work_time'])
      print('Tempo gasto até agora:', queue['spended_time'])
      queue['spended_time'] += queue['terminal_time']
      print('Tempo gasto até agora:', queue['spended_time'])
  
  elif queue['size'] == 1:
    if atual_student['work_time'] > terminal_time:
      print('Aluno ainda precisa de cpu')
      print('Tempo atual do trabalho: ',  atual_student['work_time'])
      queue = insert_student(queue, (atual_student['work_time'] - terminal_time))
      queue['spended_time'] += queue['terminal_time']
      print('Novo tempo do trabalho: ', queue['end']['work_time'])
      print('Tempo gasto até agora:', queue['spended_time'])
    else:
      atual_student = remove_student(queue)
      queue['spended_time'] += atual_student['work_time']
      
print(queue['spended_time'])




