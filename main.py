# Function to generate html options tags files
def createTagsFile(fileName, tagsFileName):
    # Creating the file of html tags
    f = open(tagsFileName, "w")

    # Open the list of medocs file
    list = open(fileName, "r")
    for x in list:
        # Create the html tags
        data = x.strip()
        f.write("<option value=\"" + data + "\">" + data + "</option>\n")
    print("Tags file generated")

# Testing the function
#createTagsFile("medicaments.txt", "medocs_tags.txt")