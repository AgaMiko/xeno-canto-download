xeno-canto-download
===================

Script for downloading bird sound files from www.xeno-canto.org based on search terms.

## Usage: 
```python
python xcdl.py searchTerm1 searchTerm2 ... searchTermN
```

## Examples:
Downloading sounds under one or many search terms (i.e. one bird type)
```python
python xcdl.py apus apus
```
downloading with multiple search term (i.e. many bird types)
```python
python xeno-canto-download/xcdl.py frugilegus &
python xeno-canto-download/xcdl.py coccothraustes &
python xeno-canto-download/xcdl.py palumbus &
python xeno-canto-download/xcdl.py Delichon urbicum
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
 
