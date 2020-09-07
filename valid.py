'''
Functions in this module are independenant of the unique/uuid-generator function that calls them.
Therefore there is the asumption they could work in other scenarios too.
'''

import re

def is_fqdn(hostname):
	'''
	FQDNs contain an empty element to the right of the TLD that signifies the unnamed domain root zone, and thus a
	trailing period follows the TLD "www.adambonner.co.uk.". However, today’s software (including internet browsers)
	usually processes the trailing period for us. The unnamed domain root zone essentially represents the internet.
	'''
	# if there is a trailing dot, remove it:
	if hostname[-1] == ".": # [-1] means last/ultimate element [-2] would be penultimate
		hostname = hostname[:-1] # [:-1] is array minus the last element

	# check length, and re pattern, if neither apply then True
	if len(hostname) > 253: #length/253: https://stackoverflow.com/questions/32290167/what-is-the-maximum-length-of-a-dns-name
		return False
	elif not re.search(r"^(?:(?=[a-z0-9-]{1,63}\.)(xn--)?[a-z0-9]+(?:-[a-z0-9]+)*\.)+[a-z]{2,63}$",hostname.lower()): #regex buddy: dns, international, strict
		return False
	else:
		return True

def is_oid(oid):
	'''
	An OID corresponds to a node in the "OID tree" or hierarchy, which is formally defined using the ITU's OID
	standard, X.660. The root of the tree contains the following three arcs:

	0: ITU-T
	1: ISO
	2: joint-iso-itu-t

	Each node in the tree is represented by a series of integers separated by periods, corresponding to the path
	from the root through the series of ancestor nodes, to the node. Thus, an OID denoting Intel Corporation
	appears as follows

		1.3.6.1.4.1.343

	and corresponds to the following path through the OID tree:

	1 ISO
	1.3 identified-organization,
	1.3.6 dod,
	1.3.6.1 internet,
	1.3.6.1.4 private,
	1.3.6.1.4.1 IANA enterprise numbers,
	1.3.6.1.4.1.343 Intel Corporation
	'''
	if not re.search(r"^(?=.{0,64}$).*^([1-9][\d]*([\.][1-9][\d]*)*)$",oid): #https://www.regextester.com/107735
		return False
	else:
		return True

def is_url(url):
	'''
	the string is a URL.
	'''
	return False
def is_x500(x500):
	'''
	the string is an X.500 DN in DER or a text output format
	'''
	return False

'''
last item of array
some_list = [1, 2, 3]
some_list[-1] = 5 # Set the last element
some_list[-2] = 3 # Set the second to last element
some_list
[1, 3, 5]

array minus 1
In [1]: [1, 2, 3, 4][:-1]
Out[1]: [1, 2, 3]
In [2]: "Hello"[:-1]
Out[2]: "Hell"
first item would be [1:]

a[start:end]
a[1:2]
[2]
a[start:]
a[1:]
[2, 3, 4, 5, 6]
'''
