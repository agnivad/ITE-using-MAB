# Individual-treatment-effect optimisation in dynamic environments
## Overview
Code is split in simulation code, found in the folder `simulation-code` and code for the experiments, found in the folder `u-cmab`.

To install `pylift`, we refer to [pylift](https://github.com/wayfair/pylift), for `cs-um` we refer to [cs-um](https://github.com/vub-dl/cs-um)

## Running the code
All code is provided in Python 3.6.6. Before running any experiments, make sure all dependencies are installed (this could take a few minutes):

```shell
pip install -r requirements.txt
```

and for `pylift` specifically:
```shell
git clone https://github.com/wayfair/pylift
cd pylift
pip install .
cd ..
```

After [installation](https://jupyter.readthedocs.io/en/latest/install.html), all experiments can be run in `jupyter notebook`
