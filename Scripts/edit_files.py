#!/user/bin

## copies gene names from uniprot text file to another file called clean_list##

input_file = "../Data/humchrx.txt"
output_file = "../Data/gene_names.txt"
def edit_files(input_file, output):
    with open('../Data/humchrx.txt','r') as myfile:
        with open('../Data/gene_names.txt','w') as clean_list:
            tag = False
            for line in myfile:
                if line.startswith("name"):
                  #print(line)
                    tag = True
                    if line.startswith("-"):
                        tag = False
                if tag:
                    linelist=line.split()
                    if len(linelist)>0:
                        lines = linelist[0]
                        #print(linelist[0])
                        clean_list.write(lines + '\n')
edit_files(input_file, output_file)