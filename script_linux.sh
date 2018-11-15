echo 'Installing numpy'
python3 -m pip install numpy
echo 'Installing matplotlib'
python3 -m pip install matplotlib
echo 'Installing Cython'
python3 -m pip install Cython
echo 'Installing opencv'
python3 -m pip install opencv-python
echo 'Installing tensorflow'
python3 -m pip install tensorflow
echo 'Cloning darkflow'
git clone https://github.com/thtrieu/darkflow.git
cd darkflow
echo 'Installing darkflow'
python3 setup.py build_ext --inplace
python3 -m pip install .