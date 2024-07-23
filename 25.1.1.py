"""
 функция создаёт 100/10 файлов с задеркой 1 секунда, автер замер тайм алл апиратион
"""

import time

def do_file(filename):

    with  open(filename, 'w'):
      pass
    time.sleep(1)

start_time = time.time() 
for i in range(10): # 100 слишком много
  do_file(f"file_{i}.txt" ) 
end_time =  time.time() 

total_time = end_time - start_time
print(f"процесс длился: {total_time} секунд ")
