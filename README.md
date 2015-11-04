# Python Crash Course 
## for Fusion Scientists in a hurry

_Crash course: a class in which a lot of information is taught in a short period of time_ [merriam-webster]

This is a Python elementary course for scientists (physicists or engineers and eventually students) who already know how to use Matlab. 

Much of the content of this course is very inspired from the book [Effective Computation in Physics](http://physics.codes/) from Anthony Scopatz and Kathryn D.Huff (which I really recommand!). 
 
The goal of this course is to empower the audience for typical control room work: retrieving, manipulating and plotting data. The duration is expected to be one or two days at max. 

This objective is certainly somewhat limited with respect to the potential of Python for science, and thus criticable. This choice is motivated mainly for time and utility purpose, as the audience will be faced to a crude problem during WEST restart: a reduced number of Matlab licences. They will be busy beside on other projects and won't have few days available for a complete (and proper) Python course. 

Because this solution does not please me (but rather circunstance imposed), the first part of the course is dedicated to carefully explain what is Python and to show how broad its usage can be (i.e.: Python is not only a cheap Matlab-replacement). 

Moreover, each course sections include a _where could I find more information?_, in order to insist on the fact that the online ressources concerning Python are significant (numerous but scattered!), which is a change in habits over Matlab for which the documentation is very well centralized.



The course topics are the following:

## [Vous avez dit Python? / _You said Python?_](http://nbviewer.ipython.org/format/slides/github/jhillairet/Fusion/blob/master/Python_Crash_Course/Slides/1-Introduction_to_Python.ipynb#/)

 - Whats is Python?
 - Why should I care?
 - Python at IRFM
 - Python terminal
 - IPython
 - Jupyter (ex-IPython notebook)
 - Spyder
 - Need help?
 
## [Les bases indispensables de Python / _Python Language Basics_](http://nbviewer.ipython.org/format/slides/github/jhillairet/Fusion/blob/master/Python_Crash_Course/Slides/2-Python_Basics.ipynb#/)

- Python Files
- Comments
- Variables
- Dealing with Errors
- (Some) Python Operators
- Strings
- String Manipulations
- Blocks : `if/else`, `for`, `while`
- Functions
- Exceptions
- List comprehension

## [(Introduction to) Numpy](http://nbviewer.ipython.org/format/slides/github/jhillairet/Fusion/blob/master/Python_Crash_Course/Slides/3-NumPy_Basics.ipynb#/)

- Numpy arrays
- Opérations et manipulation des arrays, slicing
- Ouvrir des fichiers de données (`.csv`, `.mat`)
- Où trouver de l’aide ?


## [Représentation graphique (des signaux) avec matplotlib / _Plotting with Matplotlib_](http://nbviewer.ipython.org/format/slides/github/jhillairet/Fusion/blob/master/Python_Crash_Course/Slides/4-Plotting_Basics.ipynb#/)

- Simple plot
- Changer les options graphiques, depuis l'interface  ou en commandes (`axes`, `set_`, etc.)
- Exporter une figure depuis l'interface ou en commandes
- Subplots
- `pcolor` ou assimilé
- Figures en 3D (`projection=3D`)
- Où trouver de l’aide ?

## [Récupération des signaux de la base de donnée / _Getting signals for the database_](http://nbviewer.ipython.org/format/slides/github/jhillairet/Fusion/blob/master/Python_Crash_Course/Slides/5-Fusion_data.ipynb#/)

- Le module PyWed : tsbase. Scalaires, Signaux, Groupes de signaux
- Accessing data via MDSplus: Tore Supra, JET 


## Ressources and references

- [MATLAB synonymous commands in Python/NumPy](http://mathesaurus.sourceforge.net)
- [Scipy Lecture Notes](http://www.scipy-lectures.org/)

- [Scientific Computing With Python, Jake Vanderplas](http://www.astro.washington.edu/users/vanderplas/Astr599_2014/)
- [Lectures on scientific computing with Python, Robert Johansson](https://github.com/jrjohansson/scientific-python-lectures)
- [Scientific programming in Python, Jakub Urban (IPP Prague)](http://www.pythonic.eu/fjfi/en/index.html)
