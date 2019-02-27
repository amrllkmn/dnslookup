import glob
import os
def process(filename):
    file = filename
    with open(filename, "r") as tr:
        routes = tr.readlines()
        processed = []
        for route in routes[1:]:
            if "*\n" in route:
                continue
            else:
                processed.append(route.split()[1])

    file = file[:-4]+"_processed"+".txt"
    with open(file,"w") as pr:
        for i in range(len(processed)-1):
            text="\""+processed[i]+"\""+" -- "+"\""+processed[i+1]+"\""+"\n"
            pr.write(text)



def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    to_be_processed=raw_input()
    files = []
    c=0
    txt_files = glob.glob(dir_path+"/*.txt")
    for path in txt_files:
        files.append(path[len(dir_path)+1:])
    #for file in txt_files:
    #    process(file)
    for file in files:
        if to_be_processed+"ip" in file:
            process(file)
            c=c+1
        else:
            continue
    if c==0:
        print "Sorry, something wrong occured."
    else:
        print "success!"
main()
