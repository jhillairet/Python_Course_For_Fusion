# Python Crash Course 
## for Fusion Scientists in a hurry

_Crash course: a class in which a lot of information is taught in a short period of time_ [merriam-webster]

This is a Python elementary course for scientists (physicists or engineers and eventually students) who already know how to use Matlab. 

Much of the content of this course is very inspired from the book [Effective Computation in Physics](http://physics.codes/) from Anthony Scopatz and Kathryn D.Huff (which I really recommand!). 
 
The goal of this course is to empower the audience for typical control room work: retrieving, manipulating and plotting data. The duration is expected to be one or two days at max. 

This objective is certainly somewhat limited with respect to the potential of Python for science, and thus criticable. This choice is motivated mainly for time and utility purpose, as the audience will be faced to a crude problem during WEST restart: a reduced number of Matlab licences. They will be busy beside on other projects and won't have few days available for a complete (and proper) Python course. 

Because this solution does not please me (but rather circunstance imposed), the first part of the course is dedicated to carefully explain what is Python and to show how broad its usage can be (i.e.: Python is not only a cheap Matlab-replacement). 

Moreover, each course sections include a _where could I find more information?_, in order to insist on the fact that the online ressources concerning Python are significant (numerous but scattered!), which is a change in habits over Matlab for which the documentation is very well centralized.


The course topics slides are the following:

1.Introduction Générale: Python et les outils à l'IRFM
2.Introduction au langage Python
3.Introduction à NumPy, la librairie Python pour manipuler des tableaux numériques
4.Réaliser des graphiques avec la librairie Matplotlib
5.Accéder aux données des bases de données Fusion avec la TSlib (WEST)
6.Lire et écrire des fichiers (texte ou Matlab)

## Vous avez dit Python? / _You said Python?_

 - Whats is Python?
 - Why should I care?
 - Python at IRFM
 - The hard-way: Python terminal and IPython
 - The easier-way: Jupyter and Spyder
 - The super-easier-way: IRFM Jupyterlab 
 - Need help?

## Les bases indispensables de Python / _Python Language Basics_

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


## (Introduction to) Numpy

- Numpy arrays
- Opérations et manipulation des arrays, slicing
- Ouvrir des fichiers de données (`.csv`, `.mat`)
- Où trouver de l’aide ?


## Représentation graphique (des signaux) avec matplotlib / _Plotting with Matplotlib_

- Simple plot
- Changer les options graphiques, depuis l'interface  ou en commandes (`axes`, `set_`, etc.)
- Exporter une figure depuis l'interface ou en commandes
- Subplots
- `pcolor` ou assimilé
- Figures en 3D (`projection=3D`)
- Où trouver de l’aide ?


## Récupération des signaux de la base de donnée / _Getting signals for the database_

- Le module PyWed : tsbase. Scalaires, Signaux, Groupes de signaux
- Travailler avec les données réduites (et pandas)


## Write or read text files


## Manipulating Images

## The SciPy module, examples

## SymPy

## Ressources and references

- [Scipy Lecture Notes](http://www.scipy-lectures.org/)
- [MATLAB synonymous commands in Python/NumPy](http://mathesaurus.sourceforge.net)

- [Scientific Python Library Development Guide ](https://learn.scientific-python.org/development/)
- [Lectures on scientific computing with Python, Robert Johansson](https://github.com/jrjohansson/scientific-python-lectures)
