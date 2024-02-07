import csv
import pandas as pd
# Search up Python Dictionary; https://www.w3schools.com/python/python_dictionaries.asp

# Prompt the user for the file path
#change the file path to the AL Authors csv
# maybe use matplot lib or some other visualization to determine frequency. 


# Prompt the user for the column to sort by
column = 'County'
# want it to specifically be the county column

# Prompt the user for the sorting order
'''order = input("Enter the sorting order (asc/desc): ")
order = order.lower()
# Convert the sorting order to a boolean value
ascending = True if order.lower() == 'asc' else False
descending = False if order.lower() == 'desc' else True'''

#A place to put the First Name and Last Name column to return such, for ex. HENRY AARON 
import os
print(os.getcwd())
# making the list of the couunty associations 
# all 67 counties in Alabama 
county_list = [ 
        'Autauga',
        'Baldwin',
        'Barbour',
        'Bibb ',
        'Blount',
        'Bullock',
        'Butler',
        'Calhoun',
        'Chambers',
        'Cherokee',
        'Chilton',
        'Choctaw',
        'Clarke',
        'Clay',
        'Cleburne',
        'Coffee',
        'Colbert',
        'Conecuh',
        'Coosa',
        'Covington',
        'Crenshaw',
        'Cullman',
        'Dale',
        'Dallas',
        'DeKalb',
        'Elmore',
        'Escambia',
        'Etowah',
        'Fayette',
        'Franklin',
        'Geneva',
        'Greene',
        'Hale',
        'Henry',
        'Houston',
        'Jackson',
        'Jefferson',
        'Lamar',
        'Lauderdale',
        'Lawrence',
        'Lee',
        'Limestone',
        'Lowndes',
        'Macon',
        'Madison',
        'Marengo',
        'Marion',
        'Marshall',
        'Mobile',
        'Monroe',
        'Montgomery',
        'Morgan',
        'Perry',
        'Pickens',
        'Pike',
        'Randolph',
        'Russell',
        'St. Clair',
        'Shelby',
        'Sumter',
        'Talladega',
        'Tallapoosa',
        'Tuscaloosa',
        'Walker',
        'Washington',
        'Wilcox',
        'Winston'
    ]


authors_names_array = [
    "Agee, James",
    "Andrews Shipman, Mary Raymond",
    "Atkins, Ace",
    "Bailey, Douglas Fields",
    "Baldwin, Joseph Glover",
    "Barr, John Gorman",
    "Barrax, Gerald W.",
    "Barton, Marlin",
    "Bartram, William",
    "Beecher, John",
    "Bell, Robert",
    "Bensko, John",
    "Bethea, Jack",
    "Blassingame, Wyatt",
    "Bontemps, Arna",
    "Bragg, Rick",
    "Brown, Joe David",
    "Brown, Mary Ward",
    "Brown, Virginia Pounds",
    "Buffett, Jimmy",
    "Butler, Darren J.",
    "Butterworth, W.E.",
    "Capote, Truman",
    "Carmer, Carl",
    "Carr, Archie",
    "Carter, Forrest",
    "Cason, Clarence",
    "Childers, James Saxon",
    "Childress, Mark",
    "Clarke, John Henrik",
    "Clemens, Jeremiah",
    "Cline Jr., C. Terry",
    "Cobb, William",
    "Cocke, Zitella",
    "Cohen, Octavus Roy",
    "Coleman, Lonnie",
    "Cook, Thomas H.",
    "Counselman, Mary Elizabeth",
    "Covington, Dennis",
    "Covington, Vicki",
    "Davis, Rebecca Harding",
    "Deal, Babs H.",
    "Deal, Borden",
    "Dewberry, Elizabeth",
    "Dorsey, Tim",
    "Ellison, Lucile Watkins",
    "export-authors_list_Dec-22-Geography_list 2",
    "Fellows, Alice",
    "Fenollosa, Mary McNeil",
    "Fields, Julia",
    "Finlay, John",
    "Fitzgerald, Zelda",
    "Flagg, Fannie",
    "Ford, Jesse Hill",
    "Francis, H.E.",
    "Franklin, Tom",
    "Gaillard, Frye",
    "Gaines, Charles",
    "George, Anne",
    "Ghigna, Charles",
    "Gibbons, Faye",
    "Gilman, Rebecca",
    "Godwin, Gail",
    "Gosse, Philip Henry",
    "Grau, Shirley Ann",
    "Green, John",
    "Greenhaw, Wayne",
    "Groom, Winston",
    "Haardt, Sara",
    "Haines, Carolyn",
    "Harrington, Janice",
    "Harris, George Washington",
    "Hasford, Gustav",
    "Haskins, James",
    "Hassel, Harriet",
    "Hay, Sara Henderson",
    "Hearne, Betsy",
    "Heath, W.L.",
    "Hellman, Lillian",
    "Hemphill, Paul",
    "Henderson, Aileen Kilgore",
    "Henderson, George Wylie",
    "Hentz, Caroline Lee",
    "Hickam, Homer",
    "Hoffman, Roy",
    "Hooper, Johnson Jones",
    "Howard, Milford W.",
    "Hudgins, Andrew",
    "Huggins, Peter",
    "Huie, William Bradford",
    "Hurston, Zora Neale",
    "Ingraham, J.H.",
    "Inman, Robert",
    "Johnson, Angela",
    "Johnson, Rheta Grimsley",
    "Johnston, Mary",
    "Jones, Madison",
    "Jones, Rodney",
    "Keller, Helen",
    "King Jr., Martin Luther",
    "King, Cassandra",
    "Knight, Michael",
    "Laan, Nancy Van",
    "Lanier, Sidney",
    "Le Vert, Octavia Walton",
    "Lee, Harper",
    "Liddell, Viola Goode",
    "Lincoln, Eric C.",
    "Lytle, Andrew",
    "March, William",
    "McAfee, Thomas",
    "McCammon, Robert R.",
    "Meek, A.B.",
    "Miller, William",
    "Moore, Idora McClellan",
    "Moore, John Trotwood",
    "Murray, Albert",
    "Naslund, Sena Jeter",
    "Nolan, Han",
    "Norris, Helen",
    "Packer, Nancy Huddleston",
    "Palmer, Florence Glass",
    "Patterson, Richard North",
]
 # Add correlation between column and County Name
# Possibly compose a sub list or conditional if it finds the county name in the list, then it will return the authors in that county  
print(county_list) #sanity check

# county is unnamed column 7 in the csv file 
csvData = pd.read_csv('/Users/coreymcdaniels/Desktop/Al Authors Local /Al-authors/Spring Semester dataset 2.csv')
print(csvData.columns, '\n')
present_counties = csvData['Unnamed: 6'].unique()#ACTUALLY WORKS; let me specify it can specify the counties that are in the list already.
print("Based upon the data given, here are the counties with author representation:", present_counties, '\n')
# let me give an number return to say the number of counties missing
missing_counties = [county for county in county_list if county.strip() not in present_counties]
print("Missing counties:", missing_counties)
#present_authors = csvData['Unnamed: 6'].unique() #unamed 2 is Author_first_name_last_name
#print(present_authors)
# got all of them as missing counties;
# I think that maybe it's pointing to the wrong column. 

#csvData.sort_values(["County"], axis=0, ascending=[False], inplace=True)
#filtered_csvData = csvData[csvData['County'].isin(county_list)]
#print(filtered_csvData)
#print(csvData)'''

def Author_names(file_path, encoding):
    with open(file_path, 'r', encoding=encoding) as file:
        file_path = '/Users/coreymcdaniels/Desktop/Al Authors Local /Al-authors/Spring Semester dataset 2.csv'
        # change the file path to the csv file to your own device; the excel file is on box 
        dialect = csv.Sniffer().sniff(file.read(1024))
        dialect.skipinitialspace = True
        file.seek(0)
        reader = csv.DictReader(file, dialect=dialect)
        author_names = [column['Author_First_Name_Last_Name'] for column in reader]
        print(author_names)
    return author_names
# need to clean up code and then assess from here 

# probably should pull all the author first names followed by their last names and put them in a list;
# pull all names from the csv file and then put them in a list; then sort them by county association
# then return the list of authors in that county
#have to change file path to the csv file to your own device
file_path = '/Users/coreymcdaniels/Desktop/Al Authors Local /Al-authors/Spring Semester dataset 2.csv'
# Have to double check
encoding = 'utf-8' # to handle the invisible unicode characters 
county = 'Jefferson'

# Authors by county association 
def get_authors_by_county(file_path, encoding, county_list):
    with open(file_path, 'r', encoding=encoding) as file:
        dialect = csv.Sniffer().sniff(file.read(1024))
        dialect.skipinitialspace = True
        file.seek(0)
        reader = csv.DictReader(file, dialect=dialect)
        authors = [column.get('Author_First_Name_Last_Name', '') for column in reader if column.get('Jefferson') == county_list]
    return authors
#This works but has an empty list that it returns 
# I think the problem is that it's not returning the authors in the county; it's just returning the authors in the csv file

#can likely test it with Jefferson since I know it will return a lot of authors; then make it determined on user input
# will likely have to reverse this; I want to be able to search for the county and return the authors in that county

authors = get_authors_by_county(file_path, encoding, county)

# Print the associated authors

'''def get_county_values(file_path, encoding):
    with open(file_path, 'r', encoding=encoding) as file:
        reader = csv.DictReader(file)
        county_values = [column['County'] for column in reader]

    return county_values

county_values = get_county_values(file_path, encoding)'''

# Print the county values
'''for county in county_values:
    print(county)'''
#Sanity check  
# REMEMBER THIS IS COLUMN 7 IN THE CSV FILE , "COUNTY"
# this will be helpful for the 400+ authors on the list, but for the other amount, we will likely need something to sort out the html text
# Sort the CSV file
#COLUMN 3 is the column for 'Author_First_Name_Last_Name'

'''def sort_csv(file_path,encoding, column, column_name, ascending=True):
    with open(file_path, 'r', encoding='utf-8') as file: #if this doesn't work, go back to 'r' instead of encoding; I tried utf-8 instead; neither worked lol 
        reader = csv.DictReader(file)
        data = list(reader)
    
    data.sort(key=lambda row: row[column], reverse=not ascending)
    return data

sorted_data = sort_csv(file_path, encoding, column,column_name, ascending)'''


# Print the sorted data
#for row in sorted_data:
    #print(row)







# HTML COLUMN NOTES BELOW:
# still need a way to sort through the HTML code* in the right three columns for Authors 463-1750; Do this after the first 400+ authors are able to be sorted effciently. 
# I will likely need to use the BeautifulSoup library to sort through the HTML code; I will need to do some research on how to do this.(https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

#PROBLEMS:
# Approach 1: So there's really one of two ways we can do this; I can make it so the User can ask which county they want to search and then it will return the authors in that county based on the csv file
# or I can make it so the user can search for a specific author and it will return the county that author is from( this can be in tandem with the line above)
#Approach 2: I could just have it return all AUTHOR associations with All Counties County; displaying a list with the Authors and their respective counties
# PSUEDOCODE:  
    
# FIRST RUN ERROR: need to remove Unicode; https://www.pythonpool.com/remove-unicode-characters-python/#:~:text=Explanation%3A%201%20Firstly%2C%20we%20will%20take%20an%20input,output%20string%20with%20all%20the%20removed%20Unicode%20characters.
# this error popped up, UnicodeDecodeError: 'charmap' codec can't decode byte 0x9d in position 7428: character maps to <undefined>
# searched up the article to solve the error above and found this; https://stackoverflow.com/questions/49562499/how-to-fix-unicodedecodeerror-charmap-codec-cant-decode-byte-0x9d-in-position
# SOLVED THE ERROR ABOVE BY CHANGING THE ENCODING TO UTF-8;

#SECOND RUN ERROR: Now this is the new problem; it's saying the County has a KeyError; I think it's because the County column has a space after the word Bibb; I'm going to try to remove the space and see if that works 
#https://stackoverflow.com/questions/10116518/im-getting-key-error-in-python   
    
#THIRD RUN ERROR: FileNotFoundError: [Errno 2] No such file or directory: '/Users/coreymcdaniels/Desktop/Al Authors Local /Al-authors/ALL Author Geography Metadata.csv'