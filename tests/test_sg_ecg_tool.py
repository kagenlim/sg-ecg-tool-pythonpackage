from sg_ecg_tool import __version__
from sg_ecg_tool import sg_ecg_tool as sg
import pytest
import pandas as pd
import matplotlib.pyplot as plt
from unittest.mock import patch

def test_version():
    assert __version__ == '0.1.0'

def test_explore_study():
    result = pd.DataFrame(sg.explore_study(sg.Business)).shape
    expected = (120, 13)
    assert result == expected

def test_get_employed():
    result = pd.DataFrame(sg.get_employed(sg.Law, sg.SMU)).shape
    expected = (12, 6)
    assert result == expected

def test_see_employ():
    with patch("matplotlib.pyplot.plot") as show_patch:
        sg.see_employ(sg.Law, sg.SMU)
        assert show_patch.called

def test_get_paid():
    result = pd.DataFrame(sg.get_paid(sg.Humanities_SocialSci, sg.NTU)).shape
    expected = (96, 7)
    assert result == expected

def test_see_paid():
    with patch("matplotlib.pyplot.plot") as show_patch:
        sg.see_paid(sg.Law, sg.SMU)
        assert show_patch.called

def test_explore_opening():
    result = pd.DataFrame(sg.explore_opening('transportation and storage')).shape
    expected = (59, 5)
    assert result == expected

def test_see_opening():
    with patch("matplotlib.pyplot.plot") as show_patch:
        sg.see_opening('transportation and storage')
        assert show_patch.called


