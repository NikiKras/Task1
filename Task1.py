import gdown
url = 'https://drive.google.com/drive/u/1/folders/1mczhXrDys25ylY3btR_d8_SN9RkpGwFN'
gdown.download_folder(url, quiet=False, remaining_ok=True)

import re
from glob import glob

all_files = glob('data/problem_*.md')

task_reg = re.compile('# Задача(.*)# Решение', re.MULTILINE | re.DOTALL)
sol_reg = re.compile('# Решение(.*)# Подсказки', re.MULTILINE | re.DOTALL)

for filename in all_files:
  with open(filename, 'r') as f:
    data = f.read()

  task = task_reg.findall(data)[0].strip()
  solution = sol_reg.findall(data)[0].strip()

  prob_id = int(filename.split('_')[1][:-3])

  with open('log.txt', 'a') as f:
    f.write(f'Задача с ID {prob_id} обработана успешно!\n')

  print('\n'.join(task.split('\n')[:5]))
