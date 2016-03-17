# Convert the ipynb into html files
#
# add --post=serve to the ipython nbconvert command to serve the web server
.PHONY: clean

html:  PartII_Python.html PartIII_NumPy.html PartIV_plotting.html PartVI_Files.html PartV_Fusion-Data.html PartI_Introduction.html
	mv *.html html/

%.html: %.ipynb
	jupyter nbconvert --to html $<

clean:
	rm html/*.html
