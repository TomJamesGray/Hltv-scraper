from helpers import stripList
import pytest
def testStripList():
    assert(stripList([""," test"]) == ["test"])
def testStripListString():
    with pytest.raises(ValueError):
        stripList("A string")
