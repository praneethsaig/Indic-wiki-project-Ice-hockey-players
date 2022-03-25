!pip install tewiki, writePage

import pickle
import ast
from jinja2 import Environment, FileSystemLoader

from genXML import tewiki, writePage


def getData(row,i):
	data = {
		'Index': (row.Index.values[0]),
		'Name':row.Name.values[0],
		'Date_of_birth':row.Date_of_birth.values[0],
		'Season_year':row.Season_year.values[0],
		'Season':row.Season.values[0],
		'Number':row.Number.values[0],
		'Team':(row.Team.values[0]),	
		'Games_Played':row.Games_Played.values[0],
		'Goals':row.Goals.values[0],
		'Assists':row.Assists.values[0],
		'Points':row.Points.values[0],
		'PlusMinus_Ratings':row.PlusMinus_Ratings.values[0],
		'Penalty_Minutes':row.Penalty_Minutes.values[0],
		'Shots_on_Goal':row.Shots_on_Goal.values[0],
		'Shooting_Percentage':row.Shooting_Percentage.values[0],
		#'PowerPlay_Goals':(row.PowerPlay_Goals.values[0]),
		'PowerPlay_Assists':row.PowerPlay_Assists.values[0],
		'Short_Goals':row.Short_Goals.values[0],
		'Short_Assists':row.Short_Assists.values[0],
		'Game_Winning_Goals':row.Game_Winning_Goals.values[0],
		'Game_Tying_Goals':row.Game_Tying_Goals.values[0],
		'Time_on_Ice_per_Game':row.Time_on_Ice_per_Game.values[0],
		'Games_Started': row.Games_Started.values[0],
		'Wins':row.Wins.values[0],
		'Losses':row.Losses.values[0],
		'Ties':row.Ties.values[0],
		'Overtime_Losses':row.Overtime_Losses.values[0],
		'Goals_Against':row.Goals_Against.values[0],
		'Goals_Against_Average': row.Goals_Against_Average.values[0],
		'Shots_Against': row.Shots_Against.values[0],
		'Saves': row.Saves.values[0],
		'Save_Percentage':row.Save_Percentage.values[0],
		'Shutouts':row.Shutouts.values[0],
		'Position':row.Position.values[0],
		'Height':row.Height.values[0],
		'Weight':row.Weight.values[0],
		'Body_mass_index':row.Body_mass_index.values[0],
		'Place_of_birth':row.Place_of_birth.values[0],
		'Age':row.Age.values[0],
		'Experience':row.Experience.values[0]
	}
	return data



def main():
	# Load the template
	file_loader = FileSystemLoader('./templates')
	env = Environment(loader=file_loader)
	template = env.get_template('main_template.j2')

	# Load the data (.pkl)
	hockeyDF =pickle.load(open('./123.pkl', 'rb'))


	#remove this to generate articles for all movies
	ids = hockeyDF.Index.tolist()
	#ids = ids[:1]
	# print(ids)

	# print(type(hockeyDF.iloc[0]))
	# Initiate the file object
	fobj = open('1.xml', 'w')
	fobj.write(tewiki+'\n')

	# Give the page_id from which you want to generate the articles in
	initial_page_id = 500000

	# Loop to grab all data from the .pkl and generate articles using the template
	for i in range(len(ids)):
		row = hockeyDF.loc[(hockeyDF['Index']==i+1)]
		title = row.Name.values[0]
		text = template.render(getData(row,i))
		# print(text)

		writePage(initial_page_id,title,text,fobj)
		initial_page_id += 1
		print(text, '\n')

	fobj.write('</mediawiki>')
	fobj.close()

if __name__ == '__main__':
	main()
