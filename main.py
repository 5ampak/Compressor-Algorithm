# 1. readfile
# 2. count the number of word
# 3. count the number of letter
# 4. add index
# 5. compressed, and add index

# main.py
from pathlib import Path

from file_reader            import ReadFile 
from helper.infoWriter      import PrintInfo
from compressed.compressed  import Compressed
from Decompressed.decompressed  import Decompressed

file_path_decompressed = 'Decompressed/unCompressed.txt'
file_path_compressed = 'compressed_data.txt'

def main():

    if not Path(file_path_decompressed).exists():
        PrintInfo.printError('File does not exist.')
    else:
        PrintInfo.printInfo('File exist')

    contents = ReadFile.read_file(file_path_decompressed)

    if len(contents) == 0:
        PrintInfo.printError('File is empty')
    else:
        PrintInfo.printInfo('File is not empty')

    Compressed.findPattern(contents)

    decompressedContent = Decompressed.decompressed(file_path_compressed)

    print("decompressedContent :", str(decompressedContent)[:1000]) 
    print("contents :", str(contents)[:1000]) 

    if decompressedContent == contents:
        PrintInfo.printInfo('Compressed and decompressed work without losing data.')
    else:
        PrintInfo.display_error('Compressed and decompressed did not work and some data has been lose.')

main()
