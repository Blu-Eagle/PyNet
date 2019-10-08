# Download RFC via `urllib`

Import the necessary libraries

```python
import sys
import urllib.request
```

Try to get the RFC number from the command-line arguments

```python
# first let us try to get the command line arguments
try:
    number_rfc_required = int (sys.argv[1])
except (IndexError, ValueError):
    print ('We require a RFC number to be passed as command line argument ex: python drfc.py 2324')
    sys.exit(2)
```

Create a template and format it accordingly

```python
rfc_template = "http://www.rfc-editor.org/rfc/rfc{}.txt"
url = rfc_template.format(number_rfc_required)
```

### A Note on `urllib.request`
The urllib.request module defines functions and classes which help in opening URLs (mostly HTTP) in a complex world — basic and digest authentication, redirections, cookies and more.

The urllib.request module defines the following functions:

```python
urllib.request.urlopen(url, data=None, [timeout, ]*, cafile=None, capath=None, cadefault=False, context=None)
```

Now perform the request

```python
raw_rfc_file = urllib.request.urlopen (url).read()
```

Decode and print the RFC text.

```python
rfc = raw_rfc_file.decode()
print(rfc)
```