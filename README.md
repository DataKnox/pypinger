# A Quick Way to Ping in Python

## Install
Currently in Test
```
pip install -i https://test.pypi.org/simple/ pypinger
```

## From the CLI

You can use Pyping from the CLI like so
```
pyping -s 10.10.10.1
```
Or ping a whole subnet with
```
pyping -s 10.10.10.0/24
```

## Programmatically 

The pypinger function will not only print the output to the console but also will return a list of hosts that had successful pings
```
from pypinger import pyping

hosts = pyping('10.10.21.0/24')
print(hosts)
```
Or you can be prompted at runtime for the hosts/subnet
```
from pypinger import pyping

hosts = pyping()
print(hosts)
```

# Contact
- https://twitter.com/data_knox
- https://youtube.com/c/dataknox