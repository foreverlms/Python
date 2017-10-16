#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Date    : 2017-10-16 17:04:57
# @Author  : Bob Liao
# @Email   : codechaser1@gmail.com
# @Link    : https://github.com/coderchaser
# @Path : E:\Code\Python\sublimeText\hipython_cousera\matplotlib_.py


import numpy as np
from matplotlib import pyplot as plt
from matplotlib import pylab as pb

x=np.linspace(0,1)
pb.tile('ss')
pb.plot(np.sin(4*np.pi*x)*np.exp(-5*x),'bo')
pb.show()