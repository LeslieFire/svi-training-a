from ConfigParser import SafeConfigParser

parser = SafeConfigParser()
parser.read('simple.ini')

print parser.get('bug_tracker', 'url')

# read() returns a list containing the names of the files\
# successfully loaded, so the program can discover which configuration\
# files are missing and decide whether to ignore them.

from ConfigParser import SafeConfigParser
import glob

parser = SafeConfigParser()

candidates = ['does_not_exist.ini','also-does-not-exist.ini',
			  'simple.ini','multisection.ini',
			 ]

found = parser.read(candidates)

missing = set(candidates) - set(found)

print 'Found config files:', sorted(found)
print 'Missing files     :', sorted(missing)

#To open files with the correct encoding

from ConfigParser import SafeConfigParser
import codecs

parser = SafeConfigParser()

with codecs.open('unicode.ini', 'r', encoding='utf-8') as f:
	parser.readfp(f)

password = parser.get('bug_tracker', 'password')

print 'Password:' password.encode('utf-8')
print 'Type:' type(password)
print 'repr:' repr(password)

#Exercise on the different methods for looking at config data.
from ConfigParser import SafeConfigParser

parser = SafeConfigParser()
parser.read('multisection.ini')

for section.name in parser.sections():
	print 'Section:', section_name
	print ' Options:', parser.options(section_name)
	for name, value in parser.items(section_name):
		print "%s = %s" % (name, value)

#To test if a section exists, use has_section(), passing the section name.
from ConfigParser import SafeConfigParser

parser = SafeConfigParser()
parser.read('multisection.ini')

for candidate in ['wiki', 'bug_tracker', 'dvcs']
	print '%-12s: %s: ' % (candidate, parser.has_section(candidate))

#Use has_option() to test if an option exists within a section.
from ConfigParser import SafeConfigParser

parser = SafeConfigParser()
parser.read('multisection.ini')

for section in ['wiki', 'none']:
	print '%s Exists: %s' % (section, parser.has_section(section))
	for candidate in ['username', 'password', 'url', 'description']:
		print '%s %-12s: %s' % (section, candidate, parser.has_option(section, candidate))

#SafeConfigParser does not make any attempt to understand the option type.
#The application is expected to use the correct method to fetch the value as the desired type.
#get() always returns a string.
#Use getint() for integers, getfloat() for floating point numbers, and getboolean() for boolean values.

from ConfigParser import SafeConfigParser

parser = SafeConfigParser()
parser.read('types.ini')

print 'Integers:'
for name in parser.options('ints'):
	string_value = parser.get('ints', name)
	value = parser.getint('ints', name)
	print ' %-12s : %-7r -> %d' % (name, string_value, value)

print '\nFloats:'
for name in parser.options('floats'):
	string_value = parser.get('floats', name)
	value = parser.getfloat('floats', name)
	print ' %-12s : %-7r -> %d' % (name, string_value, value)

print '\nBooleans:'
for name in parser.options('booleans')
	string_value = parser.get('booleans', name)
	value = parser.getboolean('booleans', name)
	print ' %-12s : %-7r -> %d' % (name, string_value, value)
