# add --post=serve to the ipython nbconvert command to serve the web server
.PHONY: clean

slides: 1-Introduction_to_Python.html  2-Python_Basics.html  3-NumPy_Basics.html  4-Plotting_Basics.html  5-Fusion_data.html
	mv *.html html/

%.html: %.ipynb
	jupyter nbconvert --to=slides $<

clean:
	rm html/*.html
