from bs4 import BeautifulSoup
import requests

URL = "https://www.projecthoneypot.org/list_of_ips.php"
html_content = requests.get(URL)
soup = BeautifulSoup(html_content.content, "html.parser") # Parse html_content with BeautifulSoup html.parser

ip_addresses = []
for row in soup.select('table.manmx tr')[1:]:  # Select the table rows within the table with a class of manmx. Skip the header row
    ip_cell = row.select_one('td a.bnone') # Select the first cell in the row that contains an anchor tag with a class of bnone
    if ip_cell:
        ip_addresses.append(ip_cell.text.strip()) # If the cell exists, extract the text, strip any leading/trailing whitespace, and add it to the ip_addresses list

with open("blacklisted_ips.txt", "w") as file: # Open a file named blacklisted_ips.txt in write mode
    for ip in ip_addresses:
        file.write(ip + "\n") # Write each IP address to the file, followed by a newline character