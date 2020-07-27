from summarizer import Summarizer

fread = open("input.txt", "r")

text = ""

if fread.mode == 'r':
    contents = fread.read()
    text += contents
    fread.close()


model = Summarizer()
result = model(text, min_length=60)
full = ''.join(result)

fwrite = open("output.txt", "w")
fwrite.write(full)
fwrite.close()



