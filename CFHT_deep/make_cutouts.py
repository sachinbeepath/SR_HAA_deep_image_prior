from astropy.io import fits
from astropy import wcs
from astropy.nddata.utils import Cutout2D

file = input("give_input")

i = 0
result = None
print(file)
while result is None:
    try:
        data, hdr = fits.getdata(file, i, header=True) #'sci' image[1] data and header
        w = wcs.WCS(hdr)
        pixcrd2 = w.wcs_world2pix([[150.437, 2.643]], 0)
        centered_cut = Cutout2D(data, (pixcrd2[0][0], pixcrd2[0][1]), (256, 256))
        print(i)
        print(pixcrd2)
        result = centered_cut.data
        fits.writeto('./cutout_' + file, result, header=hdr, overwrite =True)
        print("done " + file)
#        norm = ImageNormalize(centered_cut.data, interval = ZScaleInterval())
 #       plt.imshow(centered_cut.data,norm=norm)
  #      plt.show()
    except:
#        print("no")
        if i == 40:
            result = "done"
            print("object not found in " + file)
        else:
            pass
    i +=1
