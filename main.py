def characterRemover(file, char):
  f = open(file, 'r')
  lines = f.readlines()
  newLines = []

  for line in lines:
    newLines.append(line.replace(char.lower(), '').replace(char.upper(), ''))
  
  newF = open(f"{char}-removed-{file}", 'w')
  newF.writelines(newLines)

  f.close()
  newF.close()
  print(f"Successfully removed all '{char}' from the file")

characterRemover("sample.txt", 'a')

# Remove all the lines that contain the character 'a' in a file and write it to another file.
def character_a_remover():
  f = open('sample.txt', 'r')
  lines = f.readlines()
  newLines = []

  for line in lines:
    newLines.append(line.replace('a', ''))
  
  newF = open('new-sample.txt', 'w')
  newF.writelines(newLines)

  f.close()
  newF.close()
  print("Successfully removed all 'a' characters from the file")

character_a_remover()