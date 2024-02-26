output = ''
mode = input('Enter mode: f(ile), t(ext into terminal)\n')
if mode == 't':
    originalFormat = input('original format: c(sv)\n')
    if originalFormat == 'c':
        deliminer = input('deliminer:\n')
        text = input('value:\n').split('/n')
        output += '['
        for i in text:
            output += ' ['
            for j in i.split(deliminer):
                output += ' "'+j+'" ,'
            output = output[:-1]
            output += '] ,'
        output = output[:-1]
        output += ']'
print(output)