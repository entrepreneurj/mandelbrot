See http://pillow.readthedocs.org/en/latest/installation.html

for a fresh Ubuntu 14.4 box the following commands were helpful:

```
sudo apt-get update
sudo apt-get install -y python-pip python-devel
sudo apt-get install -y libjpeg8 libpng12-0 libfreetype6 zlib1g
sudo apt-get install -y zlib1g-dev
sudo apt-get install -y git
git clone https://github.com/entrepreneurj/mandelbrot
cd mandelbrot
sudo pip install -r requirements.txt
```

This:
* Updates packages on the server
* Installs python pip and python development libraries
* Installs some imaging libraries
* Installs git
* Clones repository
* Installs necessary python modules (numPy, Pillow)
