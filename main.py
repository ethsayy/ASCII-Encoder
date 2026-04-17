import time
from pathlib import Path
start = time.time()

current_working_directory = Path.cwd()
input_path = current_working_directory / 'input'
output_path = current_working_directory / 'output'
key_file = current_working_directory / 'key.txt'

text_files = list(input_path.glob('*.txt'))

override_key = False
while True:
    answer = input('Do you want to override the key in {}? Y/N\n>> '.format(key_file))
    if answer.lower() == 'y':
        answer = input('Enter numeral key:\n>> ')
        if not answer.removeprefix('-').isdecimal():
            print('Must be a number.')
            exit()
        else:
            key = int(answer)
            break
    if answer.lower() == 'n':
        with open(key_file, encoding='utf-8') as f:
            try:
                key = int(f.read())
                break
            except Exception:
                print(f'{str(key_file)} must be a number')

for file in text_files:
    with open(file, encoding='utf-8') as f:
        contents = f.readlines()
        name = file.name.removesuffix('.txt') + '_encoded_key' + str(key) + '.txt'
        for i, x in enumerate(contents):
            new_x = ''
            y_count = len(x)-1
            for index, y in enumerate(x):
                if index < y_count:
                    new_x += str(ord(y) + key) + ' '
                else:
                    new_x += str(ord(y) + key)
            contents[i] = new_x
        
        with open(output_path / name, 'w', encoding='utf-8') as f_one:
            f_one.write('\n'.join(contents))

elapsed = (time.time() - start) * 1000
print(f'Finished in {elapsed:.3f} ms')
input()
exit()