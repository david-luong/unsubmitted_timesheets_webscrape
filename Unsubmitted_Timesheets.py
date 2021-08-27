#importing BeautifulSoup library
import bs4

#opening HTML file
HTMLFile = open("Timesheet – Insert Organisation Name – Harvest.html","r")

#reading HTML file
index = HTMLFile.read()

#creating BeautifulSoup object
soup = bs4.BeautifulSoup(index,"lxml")

#selecting td class containing name of employees with unsubmitted timesheets
results = soup.select("td")

#for loop to remove non-name values present with tag "td" and print name values
for res in results:
    #getText from within "td" tags
    name = res.getText()
    #remove empty spaces before first character and after last character
    strip_name = name.strip()
    #remove new line entries to create single line of text
    new_name = strip_name.replace("\n","")
    #replace all spaces to create concatenated single line sting
    string_name = new_name.replace(" ","")
    #condition for empty result
    if string_name == "":
        continue
    #condition for hour values on timesheets extracted (e.g. 0:00 or 40:00)
    if ":" in string_name:
        continue
    #condition for "View Timesheet" result returned
    if "ViewTimesheet" in string_name:
        continue
    # [optional] other conditions such as employees set as contractor on Harvest
    #if "Contractor" in string_name:
        #continue
      
    #else print name of employee (e.g. "John Smith")
    print(new_name)
