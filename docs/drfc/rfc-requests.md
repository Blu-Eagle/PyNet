# RFC retrival via `requests`

```python
# Downloading RFC with requests
import sys
import requests

try:
    rfc_number = int(sys.argv[1])
except:
    print ("It is necessary to pass the RFC number ex: python drfc-requests.py 2324")
    sys.exit(2)

# create a url template
template = "http://www.rfc-editor.org/rfc/rfc{}.txt"

url = template.format(rfc_number)

rfc = requests.get(url).text
print (rfc)


```