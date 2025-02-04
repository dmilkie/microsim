# microsim

[![License](https://img.shields.io/pypi/l/microsim.svg?color=green)](https://github.com/tlambert03/microsim/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/microsim.svg?color=green)](https://pypi.org/project/microsim)
[![Python Version](https://img.shields.io/pypi/pyversions/microsim.svg?color=green)](https://python.org)
[![CI](https://github.com/tlambert03/microsim/actions/workflows/ci.yml/badge.svg)](https://github.com/tlambert03/microsim/actions/workflows/ci.yml)
[![codecov](https://codecov.io/gh/tlambert03/microsim/branch/main/graph/badge.svg)](https://codecov.io/gh/tlambert03/microsim)

Light microscopy simulation in python

### Install
* Clone this git repo
* cd into this directory

```shell
pip install .
pip install matlab
python setup.py build_ext --inplace
```

If it complains about needing "Microsoft Visual C++ 14.0", you can download it [here](https://visualstudio.microsoft.com/visual-cpp-build-tools/).  The Visual Studio Installer you download will bring up a dialog showing the available Visual Studio Build Tools workloads. Check the "Desktop development with C++" workload and select "Install".

### Getting started
Try this:
```python

from microsim.util import uniformly_spaced_xarray
from microsim.samples import MatsLines
from microsim.simulate import simulate_camera
from microsim.models import Camera
import matplotlib.pyplot as plt

camera = Camera(
  photodiode_size=6.45,
  qe=0.70,
  gain=1,
  full_well=18000,  # e/pix
  dark_current=0.0005,  # e/pix/sec
  clock_induced_charge=1,
  read_noise=6,
  bit_depth=12,
  offset=100,
  readout_rate=14
  )

space = uniformly_spaced_xarray(shape=(256, 256))

photons = MatsLines().render(space)

img = camera.simulate(photons)

plt.imshow(img, cmap="gray")
plt.show()
```

