jqcref
------
A repository with a python file to convert bibtex references to a standard labelling and also with a references.bib that will hopefully be useful to members of the JQC.

#### Shared references?
Feel free to use the resulting references.bib file in your latex documents, and to extend the database by sending a pull request.

#### What's this python file?
The python file converts a bibtex entry styled like this:
```
@article{PhysRevLett.71.1375,
  title = {Vortex reconnection in superfluid helium},
  author = {Koplik, Joel and Levine, Herbert},
  journal = {Phys. Rev. Lett.},
  volume = {71},
  issue = {9},
  pages = {1375--1378},
  numpages = {0},
  year = {1993},
  month = {Aug},
  publisher = {American Physical Society}
}
```
into this:
```
@article{koplik_levine_1993,
  title = {Vortex reconnection in superfluid helium},
  author = {Koplik, Joel and Levine, Herbert},
  journal = {Phys. Rev. Lett.},
  volume = {71},
  issue = {9},
  pages = {1375--1378},
  numpages = {0},
  year = {1993},
  month = {Aug},
  publisher = {American Physical Society}
}
```
In other words, the file takes the entries author names and year of publication and makes the entry label "author1_author2_year".


#### Neat! How do I use it?
Type the following into a unix terminal to get the latest copy of the repository:
```
git clone https://github.com/extigy/jqcref.git
```
Inside the jqcref folder is the references.bib file, copy it to where ever you need it.

To run the python code on your own, appropriately styled, bib file, run:
```
cat old.bib |  python refs.py > references.bib
```
where old.bib is your old bib file, and references.bib is to contain the new bib file. An example old.bib is included.