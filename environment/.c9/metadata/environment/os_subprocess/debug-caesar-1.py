{"filter":false,"title":"debug-caesar-1.py","tooltip":"/os_subprocess/debug-caesar-1.py","undoManager":{"mark":4,"position":4,"stack":[[{"start":{"row":0,"column":0},"end":{"row":2,"column":3},"action":"remove","lines":["\"\"\"","Your module description","\"\"\""],"id":5}],[{"start":{"row":0,"column":0},"end":{"row":55,"column":24},"action":"insert","lines":["# Module Lab: Caesar Cipher Program Bug #1","#","# In a previous lab, you created a Caesar cipher program. This version of","# the program is buggy. Use a debugger to find the bug and fix it.","","# Double the given alphabet","def getDoubleAlphabet(alphabet):","    doubleAlphabet = alphabet + alphabet","    return doubleAlphabet","","# Get a message to encrypt","def getMessage():","    stringToEncrypt = input(\"Please enter a message to encrypt: \")","    return stringToEncrypt","","# Get a cipher key","def getCipherKey():","    shiftAmount = input(\"Please enter a key (whole number from 1-25): \")","    return shiftAmount","","# Encrypt message","def encryptMessage(message, cipherKey, alphabet):","    encryptedMessage = \"\"","    uppercaseMessage = \"\"","    uppercaseMessage = message.upper()","    for currentCharacter in uppercaseMessage:","        position = alphabet.find(currentCharacter)","        newPosition = position + cipherKey","        if currentCharacter in alphabet:","            encryptedMessage = encryptedMessage + alphabet[newPosition]","        else:","            encryptedMessage = encryptedMessage + currentCharacter","    return encryptedMessage","","# Decrypt message","def decryptMessage(message, cipherKey, alphabet):","    decryptKey = -1 * int(cipherKey)","    return encryptMessage(message, decryptKey, alphabet)","","# Main program logic","def runCaesarCipherProgram():","    myAlphabet=\"ABCDEFGHIJKLMNOPQRSTUVWXYZ\"","    print(f'Alphabet: {myAlphabet}')","    myAlphabet2 = getDoubleAlphabet(myAlphabet)","    print(f'Alphabet2: {myAlphabet2}')","    myMessage = getMessage()","    print(myMessage)","    myCipherKey = getCipherKey()","    print(myCipherKey)","    myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet2)","    print(f'Encrypted Message: {myEncryptedMessage}')","    myDecryptedMessage = decryptMessage(myEncryptedMessage, myCipherKey, myAlphabet2)","    print(f'Decrypted Message: {myDecryptedMessage}')","","# Main logic","runCaesarCipherProgram()"],"id":6}],[{"start":{"row":27,"column":33},"end":{"row":27,"column":34},"action":"insert","lines":["i"],"id":7},{"start":{"row":27,"column":34},"end":{"row":27,"column":35},"action":"insert","lines":["n"]},{"start":{"row":27,"column":35},"end":{"row":27,"column":36},"action":"insert","lines":["t"]}],[{"start":{"row":27,"column":36},"end":{"row":27,"column":37},"action":"insert","lines":["("],"id":8}],[{"start":{"row":27,"column":46},"end":{"row":27,"column":47},"action":"insert","lines":[")"],"id":9}]]},"ace":{"folds":[],"scrolltop":350.5,"scrollleft":0,"selection":{"start":{"row":27,"column":47},"end":{"row":27,"column":47},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":24,"state":"start","mode":"ace/mode/python"}},"timestamp":1696992790329,"hash":"05a4b989316c3c4b3e388ab6212bdc9e22dcda68"}