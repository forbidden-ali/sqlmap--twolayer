import os

path = "G:\\py\\wooyunsites\\output\\"
fp=open('final_results.txt',"a")	
def gci(filepath):
  files = os.listdir(filepath)
  for fi in files:
    fi_d = os.path.join(filepath,fi)            
    if os.path.isdir(fi_d):
      gci(fi_d)                  
    else:
      pfiles = os.path.join(filepath,fi_d)
      if os.path.basename(pfiles) == 'log' and os.path.getsize(pfiles)>0:
        fp.write(pfiles+'\n')
        print pfiles

gci(path)
fp.close()
os.system("pause")