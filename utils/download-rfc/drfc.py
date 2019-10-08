# import sys to get command line arguments
import sys

# import urllib.request to open url's
import urllib.request

# first let us try to get the command line arguments
try:
    number_rfc_required = int (sys.argv[1])
except (IndexError, ValueError):
    print ('We require a RFC number to be passed as command line argument ex: python drfc.py 2324')
    sys.exit(2)

# template format for the RFC we are going to download
rfc_template = "http://www.rfc-editor.org/rfc/rfc{}.txt"

# format the url according to the RFC number provided
url = rfc_template.format(number_rfc_required)

# read the raw file
raw_rfc_file = urllib.request.urlopen (url).read()

# decode into readable format
rfc = raw_rfc_file.decode()

# print the decoded string
print(rfc)