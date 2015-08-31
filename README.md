# Python Crash Course 
## for Fusion Scientists in a hurry

_Crash course: a class in which a lot of information is taught in a short period of time_ [merriam-webster]

This is a Python elementary course for scientists (physicists or engineers and eventually students) who already know how to use Matlab.
 
The goal of this course is to empower the audience for typical control room work: retrieving, manipulating and plotting data. The duration is expected to be one or two days at max. 

This objective is certainly somewhat limited with respect to the potential of Python for science, and thus criticable. This choice is motivated mainly for time and utility purpose, as the audience will be faced to a crude problem during WEST restart: a reduced number of Matlab licences. They will be busy beside on other project and won't have few days available for a complete (and proper) Python course. 

Because this solution does not please me (but rather imposed), the first part of the course is dedicated to carefully explain what is Python and to show how broad its usage can be (ie.: Python is not only a cheap Matlab-replacement). 

Moreover, each course sections include a _where do find more information_, in order to insist on the fact that the online ressources concerning Python are significant (numerous but scattered!), which is a change in habits over Matlab for which the documentation is very well centralized.



The course topics are the following:

## [Vous avez dit Python? / _You said Python?_](http://nbviewer.ipython.org/format/slides/github/Hash--/Fusion/blob/master/Python_Crash_Course/1%2520-%2520Introduction%2520to%2520Python.ipynb#/)

 - Whats is Python?
 - Why should I care?
 - Python at IRFM
 - Python terminal
 - IPython
 - Jupyter (ex-IPython notebook)
 - Spyder
 - Need help?
 
## Les bases indispensables de Python / _Python Language Basics_

- Python Files
- Comments
- Variables
- Dealing with Errors
- (Some) Python Operators
- Strings
- String Manipulations
- Blocks : `if`, `for`, `while`
- Functions
- Gestion des erreurs ? ~~Exceptions~~
- Importer un module
- ~~classes et programmation objet~~
- ~~conteneurs: tuples, dictionnaires, etc.~~
- ~~itérateurs et générateurs~~
- Où trouver de l’aide ?

## Numpy

- Numpy arrays
- Opérations et manipulation des arrays, slicing
- ~~Fonctions de numpy (`ufunc`, etc) ~~
- Ouvrir des fichiers de données (`.csv`, `.mat`)
- Où trouver de l’aide ?

## Récupération des signaux de la base de donnée / _Getting signals for the database_

- Le module PyWed : tsbase. Scalaires, Signaux, Groupes de signaux
- ~~Utilisation d’outils avancés de visualisation des signaux (ThermaVIP, piScope, etc)~~

## Représentation graphique (des signaux) avec matplotlib / _Plotting with Matplotlib_

- Simple plot
- Changer les options graphiques, depuis l'interface  ou en commandes (`axes`, `set_`, etc.)
- Exporter une figure depuis l'interface ou en commandes
- Subplots
- `pcolor` ou assimilé
- Figures en 3D (`projection=3D`)
- ~~backend~~
- Où trouver de l’aide ?

## ~~Scipy~~

- http://docs.scipy.org/doc/scipy/reference
- Intégration numérique ?
- FFT ?
- Interpolation ?
- Traitement d’image ?
- Calcul symbolique (SymPy)

## Pour aller plus loin ?  _further information_
- ~~débugger~~
- ~~Pandas~~
- ~~interfaçage C/Fortran (f2py, etc)~~
- ~~travailler avec des strings~~
- ~~Explore the Python standard library~~
- ~~unit tests~~
- ~~Object Oriented Programming~~
- ~~optimisation and parallalisation~~
- ~~version control~~

## Ressources and references

- https://scipy-lectures.github.io/
- https://github.com/jakevdp/2014_fall_ASTR599/blob/master/notebooks/00_intro.ipynb
- https://github.com/jrjohansson/scientific-python-lectures
- http://www.pythonic.eu/fjfi/en/index.html
