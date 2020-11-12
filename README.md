# A Quick Way to Ping in Python

## Install
Currently in Test
```
pip install pypinger==2.0.3
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
Specify ping count
```
pyping -s 10.15.0.0/28 -c 1
```
Suppress Printed Output
```
pyping -s 10.15.0.0/28 -c 2 -p False
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
Specify counts and print suppression - Note that Printer is string!
```
from pypinger import pyping

hosts = pyping(subnet="10.15.0.0/28", count=2, printer="False")
print(hosts)
```

# Contact
- https://twitter.com/data_knox
- https://youtube.com/c/dataknox