
Run with

~~~bash
# In first terminal (kill with ctrl-c)
python cameraToMMap.py tmpImage.bin 1 1280 720

# In second terminal (kill with q)
python mmapToFigure.py tmpImage.bin 1 1280 720
~~~

Requires

- opencv (I installed with `conda install -c conda-forge opencv`)
- numpy
