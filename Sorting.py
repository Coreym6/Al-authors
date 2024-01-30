import csv
# Search up Python Dictionary; https://www.w3schools.com/python/python_dictionaries.asp

# Prompt the user for the file path
#change the file path to the AL Authors csv
file_path = 'ALL Author Geography Metadata.csv'
encoding = 'utf-8'

# Prompt the user for the column to sort by
column = 'County'
# want it to specifically be the county column

# Prompt the user for the sorting order
order = input("Enter the sorting order (asc/desc): ")
order = order.lower()
# Convert the sorting order to a boolean value
ascending = True if order.lower() == 'asc' else False
descending = False if order.lower() == 'desc' else True

#A place to put the First Name and Last Name column to return such, for ex. HENRY AARON 
column_name = 'Author_First_Name_Last_Name'
# making the list of the couunty associations 
# all 67 counties in Alabama 
county_list = [ [
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
] # Add correlation between column and County Name 


def get_county_values(file_path, encoding):
    with open(file_path, 'r', encoding=encoding) as file:
        reader = csv.DictReader(file)
        county_values = [row['County'] for row in reader]

    return county_values

county_values = get_county_values(file_path, encoding)

# Print the county values
for county in county_values:
    print(county)
#Sanity check  
# REMEMBER THIS IS COLUMN 7 IN THE CSV FILE , "COUNTY"
# this will be helpful for the 400+ authors on the list, but for the other amount, we will likely need something to sort out the html text
# Sort the CSV file
#COLUMN 3 is the column for 'Author_First_Name_Last_Name'

def sort_csv(file_path,encoding, column, column_name, ascending=True):
    with open(file_path, 'r', encoding='utf-8') as file: #if this doesn't work, go back to 'r' instead of encoding; I tried utf-8 instead; neither worked lol 
        reader = csv.DictReader(file)
        data = list(reader)
    
    data.sort(key=lambda row: row[column], reverse=not ascending)
    return data

sorted_data = sort_csv(file_path, encoding, column,column_name, ascending)


# Print the sorted data
for row in sorted_data:
    print(row)







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