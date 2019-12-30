# Budget Tracker
Budget Tracker is designed to allow you to track your actual spend against a defined budget to find where you might be overspending.  

While there are many programs out there that help you set a budget, and a few that will let you track spend, I couldn't find any (at least free ones) that did both.

## Current Functionality
### Budget Tracker will:  
* Read in a configuration file which defines the budget categories and regexes to match against a 'Spend' file
* Read in a 'Spend' file in CSV format (comma delimited)
* Parse that file, putting each line into a defined budget Category
* Output the total spend for each category for that 'Spend' file

### Budget Tracker can't (yet):
* Allow you to set up a budget
* Compare the spend against that budget
* Present any data in graphical format
* Persist any data
* Collate data across multiple datasets
* Handle 'Spend' files in any format other than CSV with comma delimiters
* Any form of GUI (i.e. it is currently command line only)

## Data Formats
The configuration file is a JSON file.  
The 'Spend' files is a CSV file.  
See the examples_files for the JSON definition and examples_files

## Releases
Currently there are no plans to do formal releases into deployable containers (i.e. deb, rpm, etc), this may come once Budget Tracker has a more complete feature set.

### Prerequisites  
It uses Python 3.X but I am specifically running 3.6 so I make no promises about it working on earlier versions of 3.X.  
No other Python libraries are currently required.

### Installation & running
* Clone this repository
* Create a directory to contain your 'Spend' files and configuration file. Note that the .gitignore is set up to ignore 'realdata' so you can create this folder in the repo tree to contain your data safely.
* Run with:  
```$ python budget.py -c examples_files/config.json -d examples_files/data.csv```  
replacing the examples_files with the path to your real data as appropriate

## Config Creator 
The Budget Tracker currently contains a standalone utility to help create and manage configuration file - inventively called 'settings.py'
In the future this feature set will be rolled into the main BudgetTracker program.

###  Running

```$ python settings.py -c myConfigFile.json -d sampleDataFile.csv```
myConfigFile doesn't need to exist, but if it does it will be read in, allowing the user to edit an existing configuration file. Note this file will be overwritten on exit - i.e. there is no "save" or undo functionality currently.
The sampleDataFile should be a real Spend file that you intend to use with the main BudgetTracker program, as the Config Creater uses this to prompt you in creating appropriate Regexes for the categories

### Notes
The Config Creator currently doesn't help you set up the section of the Configuration file regarding the dataType of the Spend File, you will need to do this manually prior to running the Config Creator
