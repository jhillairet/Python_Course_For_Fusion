# Convert the ipynb into pdf files
#
# add --post=serve to the ipython nbconvert command to serve the web server
.PHONY: clean

pdf: PartI_Introduction.html PartII_Python.html PartIII_NumPy.html PartIV_plotting.html PartVI_Files.html PartV_Fusion-Data.html
	mv *.pdf pdf/

%.html: %.ipynb
	ipython nbconvert --to latex --post PDF $<

clean:
	rm pdf/*.pdf
