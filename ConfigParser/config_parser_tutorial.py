from ConfigParser import SafeConfigParser

parser = SafeConfigParser()
parser.read('simple.ini')

print parser.get('bug_tracker', 'url')

#read() returns a list containing the names of the files
successfully loaded, so the program can discover which configuration files are missing and decide whether to ignore them.

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
