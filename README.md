# image2mass_2025version

本项目基于 tstandley/image2mass 库。本项目更新了依赖管理和运行流程，以确保代码能在现代 Windows/Anaconda 系统上运行。本项目讲原项目的英寸和磅改为了厘米（cm）和克（g）

原地址https://github.com/tstandley/image2mass

还需下载pklzs模型到同级目录https://drive.google.com/drive/folders/17yEukxIyjyen3vJ8nuX_YklnsVBZBol4

# Environment Construction
```
conda create -n image2mass_py35 python=3.5 -c conda-forge --no-default-packages

conda activate image2mass_py35

conda install -c conda-forge numba

pip install Pillow

pip install lz4

pip install opencv-python

pip install tensorflow==1.4.0

pip install keras==2.1.1

pip install h5py==2.7.1
```


# Example usage
```
(image2mass_py35) D:\Desktop\image2mass-master>python predict_mass.py test_set_images/airplane_clock_1.jpg 15.875 3.175 5.4
```
