import re
import os
import pytest
import inspect
import session10
import datetime

README_CONTENT_CHECK_FOR = [
    "timed",
    "create_prof",
    "get_mode_bloodgroup",
    "get_mean_location",
    "get_max_age",
    "get_avg_age",
    "prefix_creator",
    "create_company",
]

num_reps = 100


def test_readme_exists():
    """                                                                                                                                                                      
    Test funtion to check if README exists.                                                                                                                                  
    """
    assert os.path.isfile("README.md"), "README.md file missing!"


def test_readme_contents():
    """                                                                                                                                                                      
    Test if README contains atleast 200 words.                                                                                                                               
    """
    readme = open("README.md", "r", encoding="utf-8")
    readme_words = readme.read().split()
    readme.close()
    assert (
        len(readme_words) >= 100
    ), "Make your README.md file interesting! Add atleast 500 words"


def test_readme_proper_description():
    """
    Check if README contains required functions..
    """
    READMELOOKSGOOD = True
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass

    assert (
        READMELOOKSGOOD == True
    ), "You have not described all the functions/class well in your README.md file"


def test_readme_file_for_formatting():
    """
    Test function to check README file formatting.
    """
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    assert content.count("#") >= 10


def test_indentations():
    """
    Returns pass if used four spaces for each level of syntactically \
    significant indenting.
    """
    lines = inspect.getsource(session10)
    spaces = re.findall("\n +.", lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert (
            len(re.sub(r"[^ ]", "", space)) % 4 == 0
        ), "Your code indentation does not follow PEP8 guidelines"


def test_function_name_had_cap_letter():
    """
    Test function to check if any function names have any capital letters.
    """
    functions = inspect.getmembers(session10, inspect.isfunction)
    for function in functions:
        assert (
            len(re.findall("([A-Z])", function[0])) == 0
        ), "You have used Capital letter(s) in your function names"


def test_mode_bloodgroup():
    """
    Test for the finding the most frequent blood group using tuple and dict.
    """
    test_prof_tuple, test_prof_dict = session10.create_prof(num_reps)
    num_runs = 100

    perf_tuples = dict()
    perf_dict = dict()

    session10.timed(session10.get_mode_bloodgroup, num_runs, perf_tuples)(
        test_prof_tuple, "nt"
    )

    session10.timed(session10.get_mode_bloodgroup, num_runs, perf_dict)(
        test_prof_dict, "dict"
    )
    assert perf_tuples["get_mode_bloodgroup"] > perf_dict["get_mode_bloodgroup"]


def test_max_age():
    """
    Test for finding max age using tuple and dict.
    """
    test_prof_tuple, test_prof_dict = session10.create_prof(num_reps)
    num_runs = 100

    perf_tuples = dict()
    perf_dict = dict()

    session10.timed(session10.get_max_age, num_runs, perf_tuples)(test_prof_tuple, "nt")
    session10.timed(session10.get_max_age, num_runs, perf_dict)(test_prof_dict, "dict")
    assert perf_tuples["get_max_age"] > perf_dict["get_max_age"]


def test_mean_location():
    """
    Test for finding the mean location using tuple and dict.
    """
    test_prof_tuple, test_prof_dict = session10.create_prof(num_reps)
    num_runs = 100

    perf_tuples = dict()
    perf_dict = dict()

    session10.timed(session10.get_mean_location, num_runs, perf_tuples)(
        test_prof_tuple, "nt"
    )
    session10.timed(session10.get_mean_location, num_runs, perf_dict)(
        test_prof_dict, "dict"
    )
    assert perf_tuples["get_mean_location"] > perf_dict["get_mean_location"]


def test_avg_age():
    """
    Test for finding the average age using tuple and dict.
    """
    test_prof_tuple, test_prof_dict = session10.create_prof(num_reps)
    num_runs = 100

    perf_tuples = dict()
    perf_dict = dict()

    session10.timed(session10.get_avg_age, num_runs, perf_tuples)(test_prof_tuple, "nt")
    session10.timed(session10.get_avg_age, num_runs, perf_dict)(test_prof_dict, "dict")
    assert perf_tuples["get_avg_age"] > perf_dict["get_avg_age"]


def test_company_stock():
    """
    Test for company stock question.
    """

    assert len(session10.create_company(100)) == 100
