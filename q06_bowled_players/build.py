# %load q06_bowled_players/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):
    bowled_players =[] 
    for i in data['innings'][1]['2nd innings']['deliveries']:
        k=list(i.values())
        if ('wicket' in k[0] ):
            if(k[0]['wicket']['kind']=='bowled'):
                bowled_players.append(k[0]['wicket']['player_out'])
                

    # Write your code here


    return bowled_players




