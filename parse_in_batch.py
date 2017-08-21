input_filename = 'sample.txt'
output_file2 = 'output_batch.txt'
batch_size = 4


def process(batch):
    for each_line in batch:
        tokens = each_line.split(',')
        with open(output_file2, 'a') as file_o:
            file_o.write('Event : '+tokens[2]+'\n')




def parase_in_batch(input_filename):
    with open(input_filename, 'r') as file:
        batch = []
        while True:
            line = file.readline()
            if not line:
                print len(batch)
                process(batch)
                break
            else:
                if not line.startswith('Record'):
                    if len(batch) == batch_size:
                        process(batch)
                        batch = []
                        print "Batch processed"
                    else:
                        batch.append(line)


parase_in_batch(input_filename)

