# Premier League Standings

A simple API showing the current Premier League standings and the number of goals scored by each team.

The data is downloaded from the official Premier League website.


## Installation
After cloning the repository follow the steps below:


Create a new virtual environment.
```
python -m venv myvenv
```
Run the virtual environment.
```
source /path/to/myvenv/Scripts/activate
```
Upgrade pip.
```
python -m pip install --upgrade pip
```
Install the required packages.
```
pip install -r requirements.txt
```
Run the development server.
```
python api.py
```


## Consuming the API

Getting the current Premier League standings and the number of goals scored by each team:
`GET http://127.0.0.1:5000`
