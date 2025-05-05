# DO NOT modify code except "YOUR CODE GOES HERE" blocks

from pytest import approx

import tfidf_engine

# ir = tfidf_engine.IRSystem(open("wiki-small.txt"))
ir = tfidf_engine.IRSystem("wikisubset")

## TODO: We have to change this to test for Jeopardy questions vs. answers:
"""

BROADWAY LYRICS
Song that says, "you make me smile with my heart; your looks are laughable, unphotographable"
My Funny Valentine

"""
## TODO: Ignore first line. It's just a Jeopardy category and is repeated among many questions
## I believe the query we will run is the second line
## result should == third line i.e. it will be a string result

def test_1word_query_10points():
    result = ir.run_query('The dominant paper in our nation\'s capital, it\'s among the top 10 U.S. papers in circulation')
    assert result == 'The Washington Post'


def test_1word_repeated1_query_10points():
    result = ir.run_query('The practice of pre-authorizing presidential use of force dates to a 1955 resolution re: this island near mainland China')
    assert result == 'Taiwan'


def test_1word_repeated2_query_10points():
    result = ir.run_query('Daniel Hertzberg & James B. Stewart of this paper shared a 1988 Pulitzer for their stories about insider trading')
    assert result == 'The Wall Street Journal'


def test_1word_unknown_query_10points():
    result = ir.run_query('Song that says, "you make me smile with my heart; your looks are laughable, unphotographable"')
    assert result == 'My Funny Valentine'


def test_1word_infrequent_query_10points():
    result = ir.run_query('In 2011 bell ringers for this charity started accepting digital donations to its red kettle')
    assert ((result == 'The Salvation Army') or (result == 'Salvation Army'))


def test_2words_query_10points():
    result = ir.run_query('The Naples Museum of Art')
    assert result == 'Florida'


def test_2words_reversed_query_10points():
    results = ir.run_query('This Italian painter depicted the "Adoration of the Golden Calf"')
    assert results == 'Tintoretto'


def test_1word_infrequent_query1_10points():
    result = ir.run_query('This woman who won consecutive heptathlons at the Olympics went to UCLA on a basketball scholarship')
    assert result == 'Jackie Joyner-Kersee'


def test_1word_infrequent_query2_10points():
    result = ir.run_query('Originally this club\'s emblem was a wagon wheel; now it\'s a gearwheel with 24 cogs & 6 spokes')
    assert result == 'Rotary International'


def test_2words_infrequent_query_10points():
    result = ir.run_query('Several bridges, including El Tahrir, cross the Nile in this capital')
    assert result == 'Cairo'

