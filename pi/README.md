# Installation instructions

## Prerequisites

* Raspberry pi running python 3.8 with pip
* Adafrui BNO085 sensor https://www.adafruit.com/product/4754

## Installation for Pi

`sudo pip3 install -r requirements.txt`

## Execution

First it is necessary to calibrate the IMU using the included `calibrate.py` script.
Once calibrated, use the `train.py` script to generate the necessary test data.
Next, generate your model using [libsvm](https://github.com/cjlin1/libsvm) after following their instructions listed to install the tools, the included `easy.py` script works perfect. After generating our model, we can use the `run.py` script to connect to mqtt and run the model. 

Note: Sudo is necessary to ensure proper permission for serial