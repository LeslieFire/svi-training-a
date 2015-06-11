#[ConfigParser - Working with configuration files](http://pymotw.com/2/ConfigParser/)

###Summary
Use the ConfigParser module to manage user-editable configuration files for an application. The configuration files are organized into sections, and each section can contain name-value pairs for configuration data. Value interpolation using Python formatting strings is also supported, to build values that depend on one another (this is especially handy for URLs and message strings).

The file format used by ConfigParser is similar to the format used by older versions of Microsoft Windows. It consists of one or more named sections, each of which can contain individual options with names and values.

Config file sections are identified by looking for lines starting with [ and ending with ]. The value between the square brackets is the section name, and can contain any characters except square brackets.

Options are listed one per line within a section. The line starts with the name of the option, which is separated from the value by a colon (:) or equal sign (=). Whitespace around the separator is ignored when the file is parsed.

###Notes

**repr()** - returns a string representation of an object.

* do not put apostrophes at the ends of string values as ConfigParser will take it literally with the value.
