# import scipy.io
# mat = scipy.io.loadmat('file.mat')

# ## v7.3以上
# import numpy as np
# import h5py
# f = h5py.File('somefile.mat','r')
# data = f.get('data/variable1')
# data = np.array(data) # For converting to a NumPy array

# # matlab engine
# import matlab.engine
# eng = matlab.engine.start_matlab()
# content = eng.load("example.mat", nargout=1)


## save
import numpy as np
from scipy.io import savemat
a = np.arange(20) 
mdic = {
  "a": a,
  "label": "experiment"
}
savemat("matlab_matrix.mat", mdic)