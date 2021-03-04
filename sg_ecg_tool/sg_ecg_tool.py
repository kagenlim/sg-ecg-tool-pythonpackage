"""
Python package that generates statistics on higher education and employment, for Singaporean students.

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
"""

import re
import pandas as pd
import matplotlib.pyplot as plt
import requests
import json

# university_short_name values
NTU = 'Nanyang Technological University'
NUS = 'National University of Singapore'
SUTD = 'Singapore University of Technology and Design'
SUSS = 'Singapore University of Social Sciences'
SIT = 'Singapore Institute of Technology'
SMU = 'Singapore Management University'

##Dataset 1
r1 = requests.get(
    'https://data.gov.sg/api/action/datastore_search?resource_id=9326ca53-9153-4a9c-b93f-8ae032637b70&limit=703')  # this limit ensures that all the observations are included

j1 = r1.json()

x1 = j1['result']['records']

# Base list comprehensions for subjects
Business = [y for y in x1 if re.findall(r'(Business|Accountancy|Management|Finance|Marketing|Estate)', y['degree'])]

Engineering = [y for y in x1 if
               (re.findall(r'(Engineering)', y['degree']) or re.match(r'^[A-z]engineering', y['degree']))]

Computing = [y for y in x1 if re.findall(r'(Comput(er|ing|ational)|Information)', y['degree'])]

Education = [y for y in x1 if re.findall(r'(Education|Sports)', y['degree'])]

Law = [y for y in x1 if re.findall(r'(La(w|ws))', y['degree'])]

Humanities_SocialSci = [y for y in x1 if re.findall(
    r'(Social|Ar(t|s)|Public|Economics|Philosophy|Psychology|Sociology|Linguistics|English|Studies|Chinese)',
    y['degree'])]

Healthcare = [y for y in x1 if (
        re.findall(r'(Dental|Medicine|Nursing|Therapy|Diagnostic)', y['degree']) or re.match(r'^[A-z]therapy',
                                                                                             y['degree']))]

Science = [y for y in x1 if re.findall(r'(Science|Biological|Chemistry|Physics)', y['degree'])]

Design_Art = [y for y in x1 if
              (re.findall(r'(Fine|Culinary|Design|Media)', y['degree']) or re.match(r'Archi[a-z]', y['degree']))]

##Dataset 2
r2 = requests.get(
    'https://data.gov.sg/api/action/datastore_search?resource_id=37e76c40-789d-422e-880e-db2689804939&limit=2390')

j2 = r2.json()

x2 = j2['result']['records']


def explore_study(subject, csv=False):
    """
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
    """
    r = subject
    df = pd.DataFrame(r)
    if csv == True:
        df.to_csv('data.csv')
    return df


def get_employed(subject, university_shortname, csv=False):
    """
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
    """
    r = [y for y in subject if (y['university'] == university_shortname)]
    df = pd.DataFrame(r)
    if csv == True:
        df[['year', 'university', 'school', 'degree', 'employment_rate_overall', 'employment_rate_ft_perm']].to_csv('data.csv')
    return df[['year', 'university', 'school', 'degree', 'employment_rate_overall', 'employment_rate_ft_perm']]

def see_employ(subject, university_shortname):
    """
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
     """
    r = [y for y in subject if (y['university'] == university_shortname)]
    df = pd.DataFrame(r, dtype=float)
    return plt.plot(df.employment_rate_overall.groupby(df.year).mean())


def get_paid(subject, university_shortname, csv=False):
    """
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
    """
    r = [y for y in subject if (y['university'] == university_shortname)]
    df = pd.DataFrame(r)
    if csv == True:
        df[['year', 'university', 'school', 'degree', 'gross_mthly_25_percentile', 'gross_monthly_median', 'gross_mthly_75_percentile']].to_csv('data.csv')
    return df[['year', 'university', 'school', 'degree', 'gross_mthly_25_percentile', 'gross_monthly_median', 'gross_mthly_75_percentile']]

def see_paid(subject, university_shortname):
    """
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
        """
    r = [y for y in subject if (y['university'] == university_shortname)]
    df = pd.DataFrame(r, dtype=float)
    return plt.plot(df.gross_monthly_median.groupby(df.year).mean())

def explore_opening(industry2, csv=False):
    """
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
    """
    r = [y for y in x2 if (y['industry2'] == industry2)]
    df = pd.DataFrame(r)
    if csv == True:
        df.to_csv('data.csv')
    return df

def see_opening(industry2):
    """
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
       """
    r = [y for y in x2 if (y['industry2'] == industry2)]
    df = pd.DataFrame(r, dtype=float)
    return plt.plot(df.job_vacancy_rate.tail(7).groupby(df.quarter).mean())