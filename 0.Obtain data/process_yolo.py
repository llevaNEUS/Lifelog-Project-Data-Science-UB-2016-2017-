
import multiprocessing
import subprocess
import os.path as path
from multiprocessing import Pool
import sys
import glob2

def work(image_file):
    if path.exists(image_file[:-3]+'txt'):
        pass
    else:
        print image_file
        output = subprocess.check_output(['./darknet', 'detector', 'test', 'cfg/coco.data', 'cfg/yolo.cfg', 'yolo.weights',image_file,'-thresh','0.1'])
        f = open(image_file[:-3]+'txt',"w")
        f.write(output)
        f.close()
        
if __name__ == '__main__':
    
    print len(sys.argv)
    if len(sys.argv) == 2:
        
        image_directory = sys.argv[1]
        image_files = glob2.glob(image_directory+'/**/*.jpg')
        
        for image_file in image_files:
            work(image_file)
        
    else:
        "Please enter the image path"