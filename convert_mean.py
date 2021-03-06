import os  
caffe_root = '/home/lein/caffe/'  
os.chdir(caffe_root)  
import sys  
sys.path.insert(0,'./python')  
  
import caffe  
import numpy as np  

if len(sys.argv)!=3:
    print "Usage: python convert_mean.py mean.binaryproto mean.npy"
    sys.exit()
os.chdir(r'/home/lein/caffe/finetunning_thesis/data')
blob = caffe.proto.caffe_pb2.BlobProto()
bin_mean = open( sys.argv[1] , 'rb' ).read()
blob.ParseFromString(bin_mean)
arr = np.array( caffe.io.blobproto_to_array(blob) )
npy_mean = arr[0]
np.save( sys.argv[2] , npy_mean )
