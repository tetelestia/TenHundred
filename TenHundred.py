import re
import csv

with open("input_text.txt", "r") as inputFile:
    input_text=inputFile.read()
inputFile.close()

with open("Ten_Hundred_Dict.txt") as dictFile:
    ten_dict = dictFile.readlines()
dictFile.close()
ten_dict = [s.strip() for s in ten_dict]

translation_dict=[[],[]]
with open('Ten_Hundred_Translation.csv', 'rb') as csvFile:
    reader = csv.reader(csvFile, delimiter='\t')
    reader.next()
    for row in reader:
        translation_dict[0].append(row[0])
        translation_dict[1].append(row[1])
csvFile.close()

input_text = re.findall(r"[\w']+|[.,!?;:]", input_text)

output_text = []
invalid_words = []
for word in input_text:
    if word.lower() in ten_dict:
        output_text.append(word)
    else:
        try:
            index_pos = translation_dict[0].index(word.lower())
            output_text.append(translation_dict[1][index_pos])
        except:
            output_text.append("FAIL")
            if word.lower() not in invalid_words:
                invalid_words.append(word.lower())


output_text = ' '.join(output_text)
output_text = re.sub(r'\s([?.!":](?:\s|$))', r'\1', output_text)

fo = open("output_text.txt", "wb")
fo.write("Invalid words: ")
fo.write(" ".join(invalid_words))
fo.write("\n\n")
fo.write(output_text)
fo.close()
