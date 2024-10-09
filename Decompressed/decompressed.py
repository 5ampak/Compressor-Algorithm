from helper.infoWriter import PrintInfo
from pathlib import Path

class Decompressed:
    @staticmethod   
    def decompressed(file_path):
        compressedFile = Decompressed.readFile(file_path)
        indexCompressed, dataCompressed = Decompressed.readContent(compressedFile)
        
        index = Decompressed.decompressedIndex(indexCompressed)
        
        # Decompress numbers
        decompressedNumber = Decompressed.decompress_numbers(dataCompressed)
        
        # Print details
        print("Index (limited to 50 chars):", str(index)[:50]) 
        print("Decompressed Number (limited to 50 chars):", str(decompressedNumber)[:50])
            
        # Find correspondence with index
        decompressedContent = Decompressed.decompressedContent(index, decompressedNumber)
        print("Decompressed Content (limited to 50 chars):", str(decompressedContent)[:50])
        return decompressedContent
        
    @staticmethod
    def decompressedContent(index, decompressedNumber):
        decompressed = []
        
        for number in decompressedNumber:
            # Ensure number is converted to string for key lookup in index
            word = index.get(str(number), str(number)) 
            decompressed.append(word)
        
        decompressedContent = ' '.join(decompressed)
        return decompressedContent

    @staticmethod
    def decompress_numbers(compressed_string):
        result = []
        segments = compressed_string.split() 

        for segment in segments:
            if '-' in segment: 
                start, end = map(int, segment.split('-'))
                result.extend(range(start, end + 1))
            else:
                result.append(int(segment)) 

        return result

    @staticmethod
    def readFile(file_path):
        contents = Path(file_path).read_text()
        return contents

    @staticmethod
    def readContent(content):
        parts = content.split("\n")
        indexCompressed = parts[0]
        dataCompressed = parts[1]
        return indexCompressed, dataCompressed
        
    @staticmethod
    def decompressedIndex(indexCompressed):
        index = {}
        listWord = indexCompressed.split('-')
        
        for count, word in enumerate(listWord, start=1):
            index[str(count)] = word.strip()  # strip whitespace around words

        return index
