import cv2
import os
import time
from joblib import Parallel, delayed
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-p", "--path", required=True, help="path to input directory of images")
args = vars(ap.parse_args())

#path = r'C:\Users\selwyn77\Desktop'
path = args["path"]
img_formats = ['.png', '.jpg', '.jpeg']

def weight(im):
    addweighted = cv2.addWeighted(im, 0.7, cv2.GaussianBlur(im, (15, 15), 0), 0.3, 0)
    return addweighted
 

#--- Using joblib -----
start_time = time.time()

new_dir = os.path.join(path, 'add_Weighted_4_joblib')
if not os.path.exists(new_dir):
    os.makedirs(new_dir)
    
def joblib_loop():
#    Parallel(n_jobs=4)(delayed(weight)(f) if f.endswith('.jpg') for f in os.listdir(path))
    for f in os.listdir(path):
        if any(c in f for c in img_formats):
            img = cv2.imread(os.path.join(path, f))
            r = delayed(weight)(img)
#            cv2.imwrite(os.path.join(new_dir, f + '_add_weighted_.jpg'), r)

elapsed_time = time.time() - start_time
print('Using Joblib : {} seconds'.format(elapsed_time))
 
#--- Without joblib ---
start_time = time.time()

#--- Check whether directory exists if not make one
new_dir = os.path.join(path, 'add_Weighted_4')
if not os.path.exists(new_dir):
    os.makedirs(new_dir)

for f in os.listdir(path):
    if any(c in f for c in img_formats):
        img = cv2.imread(os.path.join(path, f))
        r = weight(img)
#        cv2.imwrite(os.path.join(new_dir, f + '_add_weighted_.jpg'), r)
        
elapsed_time = time.time() - start_time
print('Without Joblib : {} seconds'.format(elapsed_time))



