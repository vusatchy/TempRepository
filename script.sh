echo 'Installing numpy'
pip install numpy
echo 'Installing matplotlib'
pip install matplotlib
echo 'Installing Cython'
pip install Cython
echo 'Installing opencv'
pip install opencv-python
echo 'Installing tensorflow'
pip install tensorflow
echo 'Cloning darkflow'
git clone https://github.com/thtrieu/darkflow.git
cd darkflow
echo 'Installing darkflow'
python setup.py build_ext --inplace
pip install .