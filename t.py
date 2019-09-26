import os
import shutil
import sys


if __name__ == '__main__':
    path="/home/mtz/asr-data/datatang1505h/data"
    path2="/home3/hn3/1805/data/data_aishell/wav"
    path3="/home3/hn3/1805/data/data_aishell/wav"
    files=os.listdir(path+"/category1/G0002/session01")
    for cata in ["/category1/", "/category2/", "/category3/", "/category4/"]:
        weizhi=os.listdir(path+cata)
        for w in weizhi:
            weizhi2=os.listdir(path+cata+w+"/")
            for h in weizhi2:
                files=os.listdir(path+cata+w+"/"+h);
                for file in files:
                    print(os.path.splitext(file)[1])
                    if(os.path.splitext(file)[1]==".wav"):
                        print(path2+"/"+w)
                        if(not os.path.exists(path2+"/"+w)):
                            pass
                            # os.mkdir(path2+"/"+w)
                        print(path+cata+w+"/"+h+'/'+file, path2+"/"+w+"/"+file)
                        # shutil.copyfile(path+cata+w+"/"+h+'/'+file, path2+"/"+w+"/"+file)
                    if(os.path.splitext(file)[1]==".txt"):
                        with open(path+"/"+"aishell_transcript_v0.8.txt","a") as f:
                            with open(path+cata+w+"/"+h+"/"+file, "r") as f2:
                                imformation=f2.readline()
                            f.writelines(os.path.splitext(file)[0]+"\t"+imformation)
                    pass


