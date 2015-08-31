# add --post=serve to the ipython nbconvert command to serve the web server
.PHONY: slides clean

slides: 1-Introduction_to_Python.html 2-Python_Basics.html
	mv *.html Slides/

1-Introduction_to_Python.html: 1-Introduction_to_Python.ipynb
	ipython nbconvert  --to=slides 1-Introduction_to_Python.ipynb

2-Python_Basics.html: 2-Python_Basics.ipynb
	ipython nbconvert  --to=slides 2-Python_Basics.ipynb

clean:
	rm Slides/*.html
