from helper.infoWriter import PrintInfo

class Compressed:
    @staticmethod
    def findPattern(data):
        PrintInfo.display_info('Starting compression')
        print(f"Uncompressed data length (words): {len(data.split())}")

        # Replace actual newline characters with spaces
        data = data.replace('\n', ' ')
        

        wordPattern = Compressed.findPatternWord(data)
        PrintInfo.display_info('Creating index for words')

        index = Compressed.createIndex(wordPattern)
        print("Index (limited to 50 chars):", str(index)[:50]) 

        # Compress index
        PrintInfo.display_info('Compressing Index')
        compressedIndex = Compressed.compressIndex(index)

        PrintInfo.display_info('Compressing file')
        compressedData = Compressed.compressedData(data, index)
        print(f"Compressed data length (words): {len(compressedData.split())}")

        compressNumber = Compressed.compress_numbers(compressedData)
        print(f"Compressed number length (words): {len(compressNumber.split())}")

        PrintInfo.display_info('File has been compressed.')
        Compressed.writeFile(compressedIndex, compressNumber)

    @staticmethod
    def writeFile(index, compressNumber):
        filename = "compressed_data.txt"
        
        with open(filename, 'w') as file:
            file.write(index)
            file.write("\n")  
            file.write(compressNumber)
        
        PrintInfo.display_info('File has been written')

    @staticmethod   
    def compressedData(data, index):
        compressed = []
        word = ""
        
        # Create a reverse index for faster lookup
        word_index = {v: k for k, v in index.items()}

        for char in data:
            if char != ' ':
                word += char
            else:
                if word:
                    compressed.append(word_index.get(word, word)) 
                    word = ""
                compressed.append(char)  # Preserve spaces

        if word:
            compressed.append(word_index.get(word, word))
        
        # Join the compressed list into a single string
        return ''.join(compressed)

    @staticmethod
    def compress_numbers(num_string):
        # Split the string and filter out non-numeric entries
        numbers = [int(num) for num in num_string.split() if num.isdigit()]

        result = []
        start = numbers[0]
        end = start

        for i in range(1, len(numbers)):
            if numbers[i] == end + 1: 
                end = numbers[i]
            else:
                if start == end:
                    result.append(str(start))
                else:
                    result.append(f"{start}-{end}")
                start = numbers[i]
                end = start

        if start == end:
            result.append(str(start))
        else:
            result.append(f"{start}-{end}")

        return ' '.join(result)

    @staticmethod
    def findPatternWord(data):
        word_count = {}
        word = ""

        for char in data:
            if char.isalnum():
                word += char
            elif char == ',' or '.' or '\b':
                word += char
                word_count[word] = word_count.get(word, 0) + 1
                word = "" 
            else:
                if word:
                    word_count[word] = word_count.get(word, 0) + 1
                    word = ""  

        if word:
            word_count[word] = word_count.get(word, 0) + 1
        result = dict(sorted(word_count.items(), key=lambda item: item[1], reverse=True))
        print(result)
        return result

        
    @staticmethod
    def createIndex(wordPattern):
        index = {}
        number_of_patterns = len(wordPattern)

        for count, (word, _) in enumerate(wordPattern.items(), start=1):
            index[str(count)] = word.strip()

        return index

    @staticmethod
    def compressIndex(index):
        # Convert the index to a list of words sorted by their keys and join them with hyphens
        words = [index[key] for key in sorted(index, key=int)]
        result_text = '-'.join(words)
        return result_text
