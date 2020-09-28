# Session 10

This is the readme for session-10.
This file contains information for functions present in `session10.py` and `test_session10.py`.

## Run Tests 

```
pytest -v
```

## Functions in `session10.py`.


 The function definitions are as follows: 

### timed(fn: "function", reps: int, perf_dict: dict) -> "function"


    Decorator to time performance of functions.

### create_prof(n: int) -> "namedtuple and dict"


    Function to create profiles. Both decimal and namedtuple are created.

### get_mode_bloodgroup(obj_list: list, obj_type: str) -> "bloodgroup"


    Get the bloodgroup with highest frequency from a given

### get_mean_location(obj_list: list, obj_type: str) -> "Decimal Coordinates"


    Get mean x,y of all given coordinates.

### get_max_age(obj_list: list, obj_type: str) -> "Max age"


    Function to obtain the max age given a namedtuple or dict.

### get_avg_age(obj_list: list, obj_type: str) -> "Average age"


    Function to obtain the average age given a namedtuple or dict.

### prefix_creator(name: str) -> str


    Function to create unique prefixes given a company name.

### create_company(n: int) -> "namedtuple"


    Function to create fake stock market data for n companies.


## Functions in `test_session10.py`.


The test definitions are as follows: 

### test_readme_exists()


    Test funtion to check if README exists.                                                                                                                                  

### test_readme_contents()


    Test if README contains atleast 200 words.                                                                                                                               

### test_readme_proper_description()


    Check if README contains required functions..

### test_readme_file_for_formatting()


    Test function to check README file formatting.

### test_indentations()


    Returns pass if used four spaces for each level of syntactically \

### test_function_name_had_cap_letter()


    Test function to check if any function names have any capital letters.

### test_mode_bloodgroup()


    Test for the finding the most frequent blood group using tuple and dict.

### test_max_age()


    Test for finding max age using tuple and dict.

### test_mean_location()


    Test for finding the mean location using tuple and dict.

### test_avg_age()


    Test for finding the average age using tuple and dict.

### test_company_stock()


    Test for company stock question.

