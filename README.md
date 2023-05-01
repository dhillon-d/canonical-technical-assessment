**How much time spent**

- 5 hours total from start to finish

**Assumptions**

- Assume each file in the contents index is unique
  `some_file1--------some_package1,some_package2`
  `some_file2--------some_pacakge3,some_package2`

**How to use**

- Install dependencies `pip install -r requirements.txt`, recommend using virtual env
- Run the main program to get an output of packages with most files `python main.py <architecture>`, for example `python main.py amd64`

**Testing**

- Change the ARCHITECTURE constant, in the `manual_test.py` file, to the same architecture used as a command line option for `main.py`
- Run the file `python manual_test.py`, you should get a readable `.txt` file
- Perform a `ctrl + f` on the created `.txt` file from the previous step, search for a package outputted from the `main.py` command line tool
- The package name should appear the same number of times in the file as the output from the command line tool

**General Approach**

- download content index
- parse index for top packages:

```
map {packages : frequency}
for each line in file
	split line on spaces to seperate packages
	split packages on comma to get each package
	for each package in packages
		if package in map
			increment frequency of packages
		else
			set frequency of package to 1
sort map
```

- display top packages
