import socket

socket.getaddrinfo('localhost', 8080)
import requests
from bs4 import BeautifulSoup

# Make a GET request to the LEA Global groups page
url = "https://leaglobal.com/index.cfm?fuseaction=main.groups"
response = requests.get(url)

# Parse the HTML response using Beautiful Soup
soup = BeautifulSoup(response.text, "html.parser")

# Find the section of the page that contains the group names
group_section = soup.find("div", {"class": "group-listing"})

# Extract the group names from the section
group_names = []
for group_link in group_section.find_all("a"):
    group_names.append(group_link.text.strip())

# Print the list of group names
print(group_names)
