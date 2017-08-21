outfile = 'output.txt'
def readfile(filename):
    i = 0
    with open(filename, 'r') as file_h:
        while(True):
            line = file_h.readline()
            if not line:
                break
            else:
                if not line.startswith('Record'):
                    elements = line.split(',')
                    event = elements[2]
                    write_line = 'Event '+str(i) +': '+ event +'\n'
                    with open(outfile, 'a') as file_o:
                        file_o.write(write_line)
                    i = i + 1



readfile('sample.txt')

