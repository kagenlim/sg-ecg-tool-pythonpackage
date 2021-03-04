# sg_ecg_tool 

![](https://github.com/kagenlim/sg_ecg_tool/workflows/build/badge.svg) [![codecov](https://codecov.io/gh/kagenlim/sg_ecg_tool/branch/main/graph/badge.svg)](https://codecov.io/gh/kagenlim/sg_ecg_tool) ![Release](https://github.com/kagenlim/sg_ecg_tool/workflows/Release/badge.svg) [![Documentation Status](https://readthedocs.org/projects/sg_ecg_tool/badge/?version=latest)](https://sg_ecg_tool.readthedocs.io/en/latest/?badge=latest)

Python package that generates statistics on higher education and employment, for Singaporean students. 

## Installation

```bash
$ pip install -i https://test.pypi.org/simple/ sg_ecg_tool
```

## Features

There are seven functions in this package, that help students with varying levels of readiness prepare for their higher education decisions.

## Dependencies

[tool.poetry.dependencies]
python = "^3.7"
pandas = "^1.1.5"
requests = "^2.25.1"
matplotlib = "^3.3.3"
pytest = "^6.2.1"

[tool.poetry.dev-dependencies]
pytest = "^6.2.1"
pytest-cov = "^2.10.1"
sphinx = "^3.3.1"
sphinxcontrib-napoleon = "^0.7"

## Usage

DESCRIPTION
    This package will allow you to enter Subjects you are interested in, or Universities you are keen on, so that you can
    access statistics/information on the latest employment rates and salaries associated with certain courses. This package
    also contains information on the latest openings, for various industries.
    
    To that end, there are 7 functions in this package that provide different capabilities, to empower you on your
    education and career guidance journey.
    
    There is important information in this documentation, as there are some key permissible values that must be keyed into
    certain slots ('arguments'). It will otherwise not be possible to use this package. Where necessary, these will be
    reiterated throughout the documentation.
    
    Values for university_shortname
    ----------
    This is a comprehensive list of the six autonomous universities in Singapore.
    
    You will need to key in the values on the left of the assignment operator ('='), for the
    university_shortname argument. The full names of the universities are to the right of the assignment operator.
    
    The 'sg' in front of the acronyms is an alias that I recommend.
    This can change depending on how you import this package.
    
    - sg.NTU = 'Nanyang Technological University'
    - sg.NUS = 'National University of Singapore'
    - sg.SUTD = 'Singapore University of Technology and Design'
    - sg.SUSS = 'Singapore University of Social Sciences'
    - sg.SIT = 'Singapore Institute of Technology'
    - sg.SMU = 'Singapore Management University'
    
    Values for subject
    ----------
    This is a list of potential subjects you may be interested in pursuing.
    
    These subjects have been titled in a self-explanatory way. You just need to key them in as they are rendered here.
    
    The 'sg' in front of the acronyms is an alias that I recommend.
    This can change depending on how you import this package.
    
    - sg.Business
    - sg.Engineering
    - sg.Computing
    - sg.Education
    - sg.Law
    - sg.Humanities_SocialSci
    - sg.Healthcare
    - sg.Science
    - sg.Design_Art
    
    Values for industry
    ----------
    This is a list of potential industries you may be keen on pursuing.
    
    These values, unlike for the two lists above, must be entered as strings, therefore the inverted commas around them.
    There will be a reminder, for specific modules that utilize industry.
    
    - 'accommodation and food services',
    - 'administrative and support services',
    - 'business and real estate services',
    - 'community, social and personal services',
    - 'construction',
    - 'electrical products',
    - 'electronic products',
    - 'electronic, computer and optical products',
    - 'fabricated metal products',
    - 'fabricated metal products, machinery and equipment',
    - 'financial and insurance services',
    - 'financial intermediation',
    - 'financial services',
    - 'food, beverages and tobacco',
    - 'hotels and restaurants',
    - 'information and communications',
    - 'machinery and equipment',
    - 'medical and precision instruments',
    - 'other manufacturing industries',
    - 'others',
    - 'paper products and printing',
    - 'paper products and publishing',
    - 'paper,rubber,plastic products and printing',
    - 'petroleum and chemical products',
    - 'petroleum, chemical and pharmaceutical products',
    - 'professional services',
    - 'real estate and leasing services',
    - 'real estate services',
    - 'rubber and plastic products',
    - 'textile and wearing apparel',
    - 'transport and storage',
    - 'transport equipment',
    - 'transport, storage and communications',
    - 'transportation and storage',
    - 'wholesale and retail trade'
    
    Enjoy!
    
    FUNCTIONS
    explore_opening(industry2, csv=False)
        If you are particularly interested in how many available job openings there are in a particular industry, this function can provide you with that information. This can be used in conjunction with see_opening().
        You can key in an industry that you have some form of interest in, and get a full list of job vacancy rates, over quarters.
        
        Parameters
        ----------
        industry2: str. One of the preset strings, which signify a given industry. This is a compulsory argument to enter.
        
        csv: bool. If set to true, a csv file with this information will be saved to your working directory. It is False by default.
        
        Returns
        -------
        A Pandas DataFrame, containing the queried information regarding job vacancies for a given industry.
        
        If csv=True, a csv file will also be generated.
        
        Examples
        --------
        >>> from sg_ecg_tool import sg_ecg_tool as sg
        >>> sg.explore_opening('transportation and storage')
        [DataFrame of 59 rows x 5 columns]
    
    explore_study(subject, csv=False)
        If you do not know what you would like to study, this is a good start. You can key in a subject that you have some form of interest in, and get a full list of options.
        
        Parameters
        ----------
        subject: List of Dicts. One of the preset list comprehensions that have been pre-defined. This is a compulsory argument to enter.
        
        csv: bool. If set to true, a csv file with this information will be saved to your working directory. It is False by default.
        
        Returns
        -------
        A Pandas DataFrame, containing the queried information regarding the subject of study.
        If csv=True, a csv file will also be generated.
        
        Examples
        --------
        >>> from sg_ecg_tool import sg_ecg_tool as sg
        >>> sg.explore_study(sg.Business)
        [Dataframe of 120 rows x 13 columns]
        >>> sg.explore_stdy(sg.Healthcare)
        [DataFrame of 49 rows x 13 columns]
    
    get_employed(subject, university_shortname, csv=False)
        If you already have some sense of what you might like to do, and where you might like to do it, this function can be especially helpful. This can be used in conjunction with see_employ().
        
        You can key in a subject and university that you have some form of interest in, and get a full list of options.
        
        Parameters
        ----------
        subject: List of Dicts. One of the preset list comprehensions that have been pre-defined. This is a compulsory argument to enter.
        
        university_shortname: str. However, you can simply key in the variables that have been created as part of this package (e.g., sg.NUS, sg.NTU) for convenience. This is a compulsory argument to enter.
        
        
        csv: bool. If set to true, a csv file with this information will be saved to your working directory. It is False by default.
        
        Returns
        -------
        A Pandas DataFrame, containing the queried information regarding the subject, school of study and the employment rates.
        If csv=True, a csv file will also be generated.
        
        Examples
        --------
        >>> from sg_ecg_tool import sg_ecg_tool as sg
        >>> sg.get_employed(sg.Law, sg.SMU)
        [DataFrame of 12 rows x 6 columns]
    
    get_paid(subject, university_shortname, csv=False)
        If you are particularly interested in how much you can expect to be paid, after graduating from your intended course, this function can be especially helpful. This can be used in conjunction with see_paid().
        You can key in a subject and university that you have some form of interest in, and get a full list of courses and the salary statistics of their graduates.
        
        Parameters
        ----------
        subject: List of Dicts. One of the preset list comprehensions that have been pre-defined. This is a compulsory argument to enter.
        
        university_shortname: str. However, you can simply key in the variables that have been created as part of this package (e.g., sg.NUS, sg.NTU) for convenience. This is a compulsory argument to enter.
        
        csv: bool. If set to true, a csv file with this information will be saved to your working directory. It is False by default.
        
        Returns
        -------
        A Pandas DataFrame, containing the queried information regarding the subject, school of study and the anticipated salary rates.
        If csv=True, a csv file will also be generated.
        
        Examples
        --------
        >>> from sg_ecg_tool import sg_ecg_tool as sg
        >>> sg.get_paid(sg.Humanities_SocialSci, sg.NTU)
        [DataFrame of 96 rows x 7 columns]
    
    see_employ(subject, university_shortname)
        If you already have some sense of what you might like to do, and where you might like to do it, this function can be especially helpful. This can be used in conjunction with get_employed().
        You can key in a subject and university that you have some form of interest in, and get a visualization of overall employment rate, over time.
        
        Parameters
        ----------
        subject: List of Dicts. One of the preset list comprehensions that have been pre-defined. This is a compulsory argument to enter.
        
        university_shortname: str. However, you can simply key in the variables that have been created as part of this package (e.g., sg.NUS, sg.NTU) for convenience. This is a compulsory argument to enter.
        
        Returns
        -------
        A matplotlib.pyplot visualization, with year as the x-axis and mean employment rate as the y-axis.
        
        Examples
        --------
        >>> from sg_ecg_tool import sg_ecg_tool as sg
        >>> sg.see_employ(sg.Law, sg.SMU)
        [Visualization]
    
    see_opening(industry2)
        If you are particularly interested in how many available job openings there are in a particular industry, this function can provide you with that information. This can be used in conjunction with explore_opening().
        You can key in an industry that you have some form of interest in, and get visualization of job vacancy rates, over 7 recent quarters.
        
        Parameters
        ----------
        industry2: str. One of the preset strings, which signify a given industry. This is a compulsory argument to enter.
        
        Returns
        -------
        A matplotlib.pyplot visualization, with quarters as the x-axis and job vacancy rate as the y-axis.
        
        Examples
        --------
        >>> from sg_ecg_tool import sg_ecg_tool as sg
        >>> sg.see_opening('paper products and publishing')
        [Visualization]
    
    see_paid(subject, university_shortname)
           If you are particularly interested in how much you can expect to be paid, after graduating from your intended course, this function can be especially helpful. This can be used in conjunction with get_paid().
        
           You can key in a subject and university that you have some form of interest in, and get a visualization of gross median salary of graduates from a particular type of course and university, over time.
        
           Parameters
           ----------
           subject: List of Dicts. One of the preset list comprehensions that have been pre-defined. This is a compulsory argument to enter.
        
           university_shortname: str. However, you can simply key in the variables that have been created as part of this package (e.g., sg.NUS, sg.NTU) for convenience. This is a compulsory argument to enter.
        
           Returns
           -------
           A matplotlib.pyplot visualization, with year as the x-axis and average gross monthly median salary as the y-axis.
        
           Examples
           --------
           >>> from sg_ecg_tool import sg_ecg_tool as sg
           >>> sg.see_paid(sg.Education, sg.NTU)
        [Visualization]

## Documentation

The official documentation is hosted on Read the Docs: https://sg_ecg_tool.readthedocs.io/en/latest/

## Contributors

We welcome and recognize all contributions. You can see a list of current contributors in the [contributors tab](https://github.com/kagenlim/sg_ecg_tool/graphs/contributors).

### Credits

This package was created with Cookiecutter and the UBC-MDS/cookiecutter-ubc-mds project template, modified from the [pyOpenSci/cookiecutter-pyopensci](https://github.com/pyOpenSci/cookiecutter-pyopensci) project template and the [audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage).
