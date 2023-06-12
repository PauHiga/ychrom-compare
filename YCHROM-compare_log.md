Notes on the YCHROM-compare project

Installing dependencies:

pip install python-docx

My new approach is
1- to scan through the tables of the docx file,
2- For each table: extract the data of the table,
3- regulate its format,
4- compare it with the data introduced by the user, returning the sample code and the status of the comparison.
5- Pass to the next table, until all the tables are processed.

The status code of return will be:

1 - Full match.
2 - Only one difference (not ND).
3 - A single ND of difference.
4 - Two ND of difference.
5 - Three ND differences.
6 - 4-6 ND differences.
7 - Less than 10 ND differences.
8 - Match with any number of ND differences.

The normalization rules I will follow are:

- All trailing whitespaces are removed. All characters become uppercase.
  This step is done at the beginning, in order to prevent sample name mismatch.

- All the fractions formats like like 18,2 become 18.2. This is because in several parts commas are used to divide data within a cell.

- - can be found to mark numbers that are not completely clear, eg 15* or \*15. "*" will be equal to "/ND/", in order to cover both the trailing and leading asterisk. Then the extra / should be removed via replace and strip.

- When there is more than one number in the cell, they will be separated with slashes (/). Cases considered: separation with comma and space (15, 16), separation with hyphen (15-16)

- All the unnecessary zeros are removed. (This step is performed when the lists to compare are created)

Rules for match in a single cell:

Method: I will create an array with the contain of both cells to compare, and apply set().intersection() to check if there are coincidences.

All cells except 'DYS385A/B':

Full match:

- Intersection returns one (or more) values, not counting ND.

ND match:

- Intersection doesn't return numeric values, but does return ND.

DYS385a/b cell:

Full match:
Consider the scenarios:
-17/18 becomes [17, 18] and matches another 17/18 (two coincidences are needed)
-15/15 becomes [15] and matches another 15 (a coincidence is enough)
-15/16/17 becomes [15, 16, 17] and matches any combination of those including the same number repeated twice (a coincidence is enough)

ND match:
There is no full match found, but any of the cells has a ND.

In resume, in 'DYS385A/B' if there are two values in any of the cells to compare, we need two coincidences to call a full match.
17/18 can match 17/18, or 17/18/19, but not 17 or 18
15/15 becomes 15, and matches 15 or 15/16/17, but not 15/16 (because 17/18 has two values, therefore needs two coincidences to be considered valid)

In any other case, any coincidence can be considered a full match.

If there is no full match, an ND in any of the cells returns a ND match

If none of those is true, there is a no coincidence.

------------------------------------------------

To use PyInstaller to create a standalone executable (.exe) of your Python project, you can follow these steps:

Install PyInstaller:

  pip install pyinstaller

Open a command prompt or terminal and navigate to the directory where your Python script is located.

Run the following command to create the executable:

  pyinstaller --onefile your_script_name.py

Replace your_script_name.py with the actual name of your Python script.

The --onefile option specifies that you want to generate a single executable file. If you prefer a directory containing multiple files, you can omit this option.

PyInstaller will analyze your script and its dependencies, and create the executable in the same directory. The output will be located in a subdirectory called dist.

You can now find your standalone executable in the dist directory. This file can be distributed and run on compatible systems without requiring Python or any additional dependencies.

It's important to note that PyInstaller may not handle certain complex scenarios or specific dependencies perfectly. In such cases, additional configuration might be necessary, such as including extra files or modifying the generated spec file. You can refer to the PyInstaller documentation for more advanced usage and troubleshooting: https://pyinstaller.readthedocs.io/

Additionally, it's recommended to test the generated executable on the target system to ensure all functionality works as expected, especially if your script relies on external resources or libraries.


ASCII art from https://www.asciiart.eu/

`-:-.   ,-;"`-:-. ,-;"`-:-.   ,-;"`-:-. ,-;"
`=`,'=/ `=`,'=/ `=`,'=/ `=`,'=/
y==/ y==/ y==/ y==/
,=,-<=`.    ,=,-<=`. ,=,-<=`.    ,=,-<=`.
,-'-' `-=_,-'-'   `-=_,-'-' `-=_,-'-' `-=\_

2702 vs 41337B


