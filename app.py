import mmap
import argparse
import gc

domains = []
ap = argparse.ArgumentParser()
ap.add_argument("-f","-file", required=True, help="File in name")
ap.add_argument("-o","-output", required=True, help="File output name")
ap.add_argument("-d","-debug", required=False, help="Debug flag")

agrs = vars(ap.parse_args())

DEBUG = agrs["d"]
filein = agrs["f"]
fileout = agrs["o"]

def process_large(filename):

    count = 0
    global domains

    with open(filename, "r+b") as f:

        map_file = mmap.mmap(f.fileno(), 0, prot=mmap.PROT_READ)
        
        while True:

            count = count + 1
            line = map_file.readline()

            if count % 1000000 == 0:
                domains = list(set(domains))
                if DEBUG != None:
                    print(count)
                
                gc.collect()

            line = line[:-1]
            line = line.decode("ISO-8859-1")

            if line == '': break
                
            try:
                domain = str(line).split(":")[0].split("@")[1]
                domains.append(domain)
            except Exception as e:
                    pass
        

def main():

    print("---Starting---")
    process_large(filein)

    d = list(set(domains))
    with open(fileout,"w") as w:     
        for domain in d:
            w.write(domain + "\n")
    
if __name__ == '__main__':
    main()
