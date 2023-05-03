def characterRemover(file, char):
  # open the file now using a dynamic file name and read the lines
  f = open(file, 'r')
  lines = f.readlines()

  newLines = []
  for line in lines:
    # replace both 'a' and 'A' into a new list
    newLines.append(line.replace(char.lower(), '').replace(char.upper(), ''))
  
  # create a new file with a more dynamic name and write the new lines
  newF = open(f"{char}-removed-{file}", 'w')
  newF.writelines(newLines)

  # close and print the final output
  f.close()
  newF.close()
  print(f"Successfully removed all '{char}' from the file")

characterRemover("sample.txt", 'a')

# Remove all the lines that contain the character 'a' in a file and write it to another file.
def character_a_remover():
  # open the file and get all the lines
  f = open('sample.txt', 'r')
  lines = f.readlines()

  # replace the lines to be without 'a' and add them to a new list
  newLines = []
  for line in lines:
    newLines.append(line.replace('a', ''))
  
  # create a new file and write the lines
  newF = open('new-sample.txt', 'w')
  newF.writelines(newLines)

  # close files and print the result
  f.close()
  newF.close()
  print("Successfully removed all 'a' characters from the file")

character_a_remover()