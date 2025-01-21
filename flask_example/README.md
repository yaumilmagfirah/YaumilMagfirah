# web based MCDA
Multi criteria decision aids help us in decision making. 
This code is WEB based version of CLI Football example.
Just give it a try!

# install dependencies
pip install -r requirements.txt

# steps
1. buat table
python models/create_table.py

2. transfer data dari CSV ke table
python seed.py

3. running main apps
python waspas_rank_pl.py