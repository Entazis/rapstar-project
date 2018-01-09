
import codecs
from shutil import copyfile
import io
import time

start_time = time.time()

file_output = io.open('output.txt', 'r', encoding="utf-8")
content = file_output.read()
file_output.close()

content = content.lower()
#content = content.replace('á', 'a')
#content = content.replace('é', 'e')
#content = content.replace('í', 'i')
#content = content.replace('ú', 'u')
#content = content.replace('ü', 'u')
#content = content.replace('ű', 'u')
#content = content.replace('ó', 'o')
#content = content.replace('ö', 'o')
#content = content.replace('ő', 'o')
content = content.replace('\n\n\n', '\n\n')
#content = content.replace(':', '')
content = content.replace('/', '')
content = content.replace('(', '')
content = content.replace(')', '')
content = content.replace('[', '')
content = content.replace(']', '')
#content = content.replace('-', '')
#content = content.replace(',', '')
content = content.replace(';', '')
content = content.replace('\'', '')
#content = content.replace('"', '')
content = content.replace('.', '')
content = content.replace('+', '')
content = content.replace('\\', '')
content = content.replace('|', '')
content = content.replace('&', '')

file_output_clean = open('output_clean.txt', 'w', encoding="utf-8")
file_output_clean.write(content)
file_output_clean.close()

copyfile("output_clean.txt", "data/rapstar/input.txt")

elapsed_time = time.time() - start_time
print("preparing time was: ", elapsed_time)