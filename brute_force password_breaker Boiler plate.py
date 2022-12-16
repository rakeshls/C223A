import PyPDF2 as pd
filename = input('Path to the file: ')
file = open(filename,'rb')
pdfReader = pd.PdfFileReader(file)

tried = 0

if not pdfReader.isEncrypted:
    print('The file is not password protected! You can successfully open it!')
else:
    wordListFile = open('wordList.txt','r',errors='ignore')
    body = wordListFile.read().lower()
    words = body.split('\n')
    for i in range(len(words)):
        word = words[i]
        print('Trying to decode password {}'.format(word))
        result = pdfReader.decrypt(word)
        if result == 1:
            print('success is '+word)
            break
        elif result == 0 :
            tried+=1
            print('password tried ' +str(tried))
            continue

            


