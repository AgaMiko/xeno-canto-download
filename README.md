xeno-canto-download
===================

Script for downloading bird sound files from www.xeno-canto.org based on search terms.

## Usage: 
Use python to execute a program with selected search terms. Remember to change the dirctory to the folder containing xcdl.py file, so it can be executed.
```python
python xcdl.py searchTerm1 searchTerm2 ... searchTermN
```

## Examples:
Downloading sounds under one or many search terms (i.e. one bird type)
```python
python xcdl.py apus apus
```
You can also try filtering your results. For example to search for a bird "apus apus" but only in Poland and with quality of recordings  and B type this.
For more advance search terms check [xeno-canto search tips](https://www.xeno-canto.org/help/search) website.
```python
python xcdl.py apus apus cnt:poland q>:C
```
downloading with multiple search term (i.e. download dataset of polish bird sounds - [Women in Machine Learning Project - Bird sound recognition](https://github.com/wimlds-trojmiasto/birds))
```python
python xcdl.py 	Dendrocopos major	&
python xcdl.py 	Chloris chloris	&
python xcdl.py 	Corvus frugilegus	&
python xcdl.py 	Coccothraustes coccothraustes	&
python xcdl.py 	Columba palumbus	&
python xcdl.py 	Delichon urbicum	&
python xcdl.py 	Apus apus	&
python xcdl.py 	Sitta europaea	&
python xcdl.py 	Corvus monedula	&
python xcdl.py 	Phoenicurus ochruros	&
python xcdl.py 	Turdus merula	&
python xcdl.py 	Turdus pilaris	&
python xcdl.py 	Passer montanus	&
python xcdl.py 	Phylloscopus trochilus	&
python xcdl.py 	Phylloscopus collybita	&
python xcdl.py 	Phoenicurus phoenicurus	&
python xcdl.py 	Motacilla alba	&
python xcdl.py 	Erithacus rubecula	&
python xcdl.py 	Streptopelia decaocto	&
python xcdl.py 	Parus major	&
python xcdl.py 	Parus caeruleus	&
python xcdl.py 	Alauda arvensis	&
python xcdl.py 	Luscinia luscinia	&
python xcdl.py 	Garrulus glandarius	&
python xcdl.py 	Turdus philomelos	&
python xcdl.py 	Pica pica	&
python xcdl.py 	Troglodytes troglodytes	&
python xcdl.py 	Carduelis carduelis	&
python xcdl.py 	Sturnus vulgaris	&
python xcdl.py 	Emberiza citrinella	&
python xcdl.py 	Passer domesticus	&
python xcdl.py 	Corvus corone	&
python xcdl.py 	Fringilla coelebs	
```
## Reading json file:
To read the data from all json files found under the *searchTerms* use *readData((searchTerm, pathToJsonCatalogue)* function
### for example
```python
soundTypes = readData("type", path)
spicies = readData("sp",path)
```

## Example json file
```json
{
 "id": "489414",
 "gen": "Apus",
 "sp": "apus",
 "ssp": "",
 "en": "Common Swift",
 "rec": "Daniel Noesgaard",
 "cnt": "Denmark",
 "loc": "K\u00f8benhavn, Copenhagen Municipality, Capital Region of Denmark",
 "lat": "55.6852",
 "lng": "12.5651",
 "type": "call",
 "file": "//www.xeno-canto.org/489414/download",
 "lic": "//creativecommons.org/licenses/by-nc-sa/4.0/",
 "url": "https://www.xeno-canto.org/489414",
 "q": "no score",
 "time": "21:30",
 "date": "2019-07-29"
 }
 ```
 
