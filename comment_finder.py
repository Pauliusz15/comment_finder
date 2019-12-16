import os

print('Input a path to a folder:')
print('For example: /home/[name]/Desktop/[folder name]')
directory = input('>>')


# returns an array of all names of files in directory
def list_files(dir):
    fileNames = []
    for _, _, files in os.walk(dir):
        for name in files:
            fileNames.append(name)
    return fileNames


# returns an array of all paths to files in directory
def list_paths(dir):
    paths = []
    for dirpath, _, files in os.walk(dir):
        for name in files:
            paths.append(dirpath + '/' + name)
    return paths


# returns an array of comments of particular text
def list_comments(text):
    # a boolean to know if characters are in a string between single quotes
    isQuoteString = False
    # a boolean to know if characters are in a string between double quotes
    isDoubleQuoteString = False
    index = 0
    comments = []
    while index <= len(text):
        if index + 1 < len(text):  # prevent from index error
            # checks if is a single quote string
            if text[index] == '\'' and text[index - 1] != '\\':
                isQuoteString = not isQuoteString
            # checks if is a double quote string
            elif text[index] == '\"' and text[index - 1] != '\\':
                isDoubleQuoteString = not isDoubleQuoteString
            # checks if is a multi line comment
            elif text[index] + text[index + 1] == '/*' and not isQuoteString and not isDoubleQuoteString:
                comment = ''
                # if is a comment, gets characters till the comment ends
                while index < len(text) and text[index] + text[index + 1] != '*/':
                    comment += text[index]
                    index += 1
                comment += text[index] + text[index + 1]
                comments.append(comment)
            # checks if is a single line comment
            elif text[index] == '/' and text[index + 1] == '/' and not isQuoteString and not isDoubleQuoteString:
                comment = ''
                # if is a comment, gets characters till the end of the line
                while index < len(text) and text[index] != '\n':
                    comment += text[index]
                    index += 1
                comments.append(comment)
        index += 1
    return comments


# writes the comments into a file
def output(outputFileName):
    paths = list_paths(directory)  # file paths of directory
    files = list_files(directory)  # file names of directory
    index = 0
    outputFile = open(directory + '/' + outputFileName, "w+")
    while index < len(files):
        inputFile = open(paths[index])
        try:
            text = inputFile.read()
        except:
            pass
        comments = list_comments(text)  # comments of a file
        if len(comments) != 0:
            outputFile.write('==========' + files[index] + '==========\n')
            nr = 1  # number of a comment in a file
            for comment in comments:
                outputFile.write(str(nr) + '. ' + comment + '\n')
                nr += 1
            outputFile.write('\n')
        index += 1


outputName = 'output.txt'
output(outputName)
print('Output file ' + outputName + ' is created at ' + directory)
