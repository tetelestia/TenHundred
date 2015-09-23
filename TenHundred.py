import re	#For regular expressions, working with the punctuation
import csv	#For importing the csv file

#Reads the input text from file
with open("input_text.txt", "r") as inputFile:
    input_text=inputFile.read()
inputFile.close()

#Reads the Ten_Hundred_Dict.txt file
with open("Ten_Hundred_Dict.txt") as dictFile:
    ten_dict = dictFile.readlines()
dictFile.close()
ten_dict = [s.strip() for s in ten_dict]

#Reads the Ten_Hundred_Translation.csv file
translation_dict=[[],[]]
with open('Ten_Hundred_Translation.csv', 'rb') as csvFile:
    reader = csv.reader(csvFile, delimiter='\t')
    reader.next()
    for row in reader:
        translation_dict[0].append(row[0])
        translation_dict[1].append(row[1])
csvFile.close()

#Split the input text on either side of any punctuation
input_text = re.findall(r"[\w']+|[.,!?;:]", input_text)


#Below runs through the input text one word at a time
#If the word is in the Ten Hundred list, it gets added to the output right away
#Next, after the "try:", it tries to find the word in the translation dictionary
#If that it's found, after the "except:", it adds the word to a list of invalid words
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
            output_text.append("INVALID")
            if word.lower() not in invalid_words:
                invalid_words.append(word.lower())

#Joins the list of words back into congruent sentences
#The second line below here gets ride of the white space between
#	the last word of a sentence and its punctuation
#Add the punctuation between the "r'\s([" and "]"
#	if there is missing punctuation which is still
#	giving an error
output_text = ' '.join(output_text)
output_text = re.sub(r'\s([?.!":](?:\s|$))', r'\1', output_text)

#And, below, the text is output
#The "if len(invalid_words)" prints the list of invalid
#	words, but only if there is one
outputFile = open("output_text.txt", "wb")
if len(invalid_words):
	outputFile.write("Invalid words: ")
	outputFile.write(" ".join(invalid_words))
	outputFile.write("\n\n")
outputFile.write(output_text)
outputFile.close()
