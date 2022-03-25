import pickle
import pandas as pd

# Makes a .pkl file which can be for loading data into the template
def main():
    HockeyFile = 'data/players_datafinal.csv'
    hockeyDF = pd.read_csv(hockeyFile)
    pickle.dump(hockeyDF, open('./123.pkl', 'wb'))

if __name__ == '__main__':
    main()
