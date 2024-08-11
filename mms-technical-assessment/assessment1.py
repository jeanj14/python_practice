import pandas as pd
import matplotlib.pyplot as mpl

#opens csv file and stores into file variable flotationfile
flotationfile = open("flotation_data.csv", "r")

# =============================================================================
# using class object to contain all the neccesary functions
#     to calculate the statistics for 
#       Recovery and Grade columns
# =============================================================================

class FlotClass(): #takes in dataframe object only
    def __init__(self, df: pd.DataFrame):
        self.df = df
        
    def find_min(self, key):
        minval = self.df[key][0]
        for x in self.df[key]:
            if x<minval:
                minval=x
        return minval
    
    def find_max(self, key):
        maxval = self.df[key][0]
        for x in self.df[key]:
            if x>maxval:
                maxval=x
                
        return maxval
    
    def find_mean(self, key):
        if key == "Date":
            print("cannot calculate mean of date")
        else:
            tally = 0
            for x in self.df[key]:
                tally+=x
                
            mean = tally / len(self.df[key])
            
            return mean
        
    def find_median(self, key):
        if key == "Date":
            print("Cannot find median of date")
        else:
            median = self.df[key][0]
            length = len(self.df[key])
        
        if length % 2 == 0:
            res = length / 2
            median = self.df[key][res]
        elif length % 2 != 0:
            res = length // 2
            median = self.df[key][res]
        return median
    


# =============================================================================
# creates DataFrame object from the csv file
# while also dropping any rows with null values
# =============================================================================
flotdf = pd.read_csv(flotationfile).dropna()
# =============================================================================
# Creates both types of plots needed for the assessment
# The first one is the histogram for Recovery and Grade
# The second one is the scatter plot using Recovery and Grade 
# as x and y variables
# =============================================================================
flotdf.plot(kind="hist")
flotdf.plot(kind="scatter", x="Recovery", y="Grade")
mpl.show()
# =============================================================================
# The DataFrame object is used as a Parameter 
# for creating the Class Object FlotClass
# The reason for using a Class Object is 
# to have all the neccessary functions kept inside one class
# Each class function takes in a key parameter,
# this key is used to go through a specific column 
# The statistic regarding the column is returned 
# All statistics is returned including correlation coefficient
# =============================================================================
flot = FlotClass(flotdf)
rec_max = flot.find_max("Recovery")
grd_max = flot.find_max("Grade")
print(f"The max values for Grade and Recovery is {rec_max} and {grd_max}\n")
rec_min = flot.find_min("Recovery")
grd_min = flot.find_min("Grade")
print(f"The min values for Grade and Recovery is {rec_min} and {grd_min}\n")
rec_mid = flot.find_median("Recovery")
grd_mid = flot.find_median("Grade")
print(f"The median values for Grade and Recovery is {rec_mid} and {grd_mid}\n")
rec_avg = flot.find_mean("Recovery")
grd_avg = flot.find_mean("Grade")
print(f"The mean values for Grade and Recovery is {rec_avg} and {grd_avg}\n")
print(f"\nThe correlation coefficient of Recovery and Grade \n{flotdf.corr()}")
