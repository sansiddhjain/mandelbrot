import numpy as np 
import cmath
import matplotlib.pyplot as plt
from matplotlib.colors import *

dim_len = 1600

#Real :-1.74995768370609350360221450607069970727110579726252077930242837820286008082972804887218672784431700831100544507655659531379747541999999995
#Imag :0.00000000000000000278793706563379402178294753790944364927085054500163081379043930650189386849765202169477470552201325772332454726999999995

# for rn in range(1885, 1985):
arr = 100*np.arange(-1, 50)
# for rn in range(1015, 1020):
print(arr)
for rn in arr:

	# x = np.linspace(-0.75-(1/(1.01**rn)), -0.75+(1/(1.01**rn)), dim_len)
	# y = np.linspace(0-(1/(1.01**rn)), 0+(1/(1.01**rn)), dim_len)
	# x = np.linspace(-1.74692730-(1/(1.01**rn)), -1.74692730+(1/(1.01**rn)), dim_len)
	# y = np.linspace(0.0130502-(1/(1.01**rn)), 0.0130502+(1/(1.01**rn)), dim_len)
	x = np.linspace(-1.740062382579339905220844167065825638296641720436171866879862-(1/(1.01**rn)), -1.740062382579339905220844167065825638296641720436171866879862+(1/(1.01**rn)), dim_len)
	y = np.linspace(0.028175339779211048992411521144319509687539076742990608570401-(1/(1.01**rn)), 0.028175339779211048992411521144319509687539076742990608570401+(1/(1.01**rn)), dim_len)

	n1, n2 = np.meshgrid(x, y, indexing='xy')

	z = (0j)*(np.zeros(dim_len*dim_len).reshape((dim_len, dim_len)))
	z.real = n1
	z.imag = -n2
	c = c_dash = z
	index = np.zeros(z.shape)

	n_iter = rn + 200
	horizon = 40
	for i in range(n_iter):
		z = z*z+c
		paul_pierce = np.absolute(z)>(2**horizon)
		index[paul_pierce] = i+1
		index[paul_pierce] = index[paul_pierce] + 1 - np.log(np.log(np.absolute(z[paul_pierce])))/np.log(2)
		z[paul_pierce] = 0j
		c[paul_pierce] = 0j

	print(index)

	# index = index/n_iter

	my_dpi = 227.0
	fig = plt.figure(figsize=(dim_len/my_dpi, dim_len/my_dpi), dpi=my_dpi, frameon=False)
	size = fig.get_size_inches()*fig.dpi
	print(size)
	fig = plt.gcf()
	size = fig.get_size_inches()*fig.dpi
	print(size)
	plt.imshow(index, cmap='nipy_spectral', interpolation=None, norm=Normalize())
	plt.axis('off')
	# plt.show()
	plt.savefig('test_images1/mandelbrot'+str(rn+115)+'.png', dpi = my_dpi, bbox_inches='tight', pad_inches=0)
	plt.close()
	print(rn)