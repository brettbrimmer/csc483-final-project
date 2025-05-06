# DO NOT modify code except "YOUR CODE GOES HERE" blocks

from pytest import approx

import tfidf_engine

# ir = tfidf_engine.IRSystem(open("wiki-small.txt"))
ir = tfidf_engine.IRSystem("wikisubset")

print("Running tests!")

## TODO: We have to change this to test for Jeopardy questions vs. answers:
"""

BROADWAY LYRICS
Song that says, "you make me smile with my heart; your looks are laughable, unphotographable"
My Funny Valentine

"""
## TODO: Ignore first line. It's just a Jeopardy category and is repeated among many questions
## I believe the query we will run is the second line
## result should == third line i.e. it will be a string result

def test_q1():
    result = ir.run_query('NEWSPAPERS The dominant paper in our nation\'s capital, it\'s among the top 10 U.S. papers in circulation')
    assert result == 'The Washington Post'


def test_q2():
    result = ir.run_query('OLD YEAR\'S RESOLUTIONS The practice of pre-authorizing presidential use of force dates to a 1955 resolution re: this island near mainland China')
    assert result == 'Taiwan'


def test_q3():
    result = ir.run_query('NEWSPAPERS Daniel Hertzberg & James B. Stewart of this paper shared a 1988 Pulitzer for their stories about insider trading')
    assert result == 'The Wall Street Journal'


def test_q4():
    result = ir.run_query('BROADWAY LYRICS Song that says, "you make me smile with my heart; your looks are laughable, unphotographable"')
    assert result == 'My Funny Valentine'


def test_q5():
    result = ir.run_query('POTPOURRI In 2011 bell ringers for this charity started accepting digital donations to its red kettle')
    assert ((result == 'The Salvation Army') or (result == 'Salvation Army'))


def test_q6():
    result = ir.run_query('STATE OF THE ART MUSEUM (Alex: We\'ll give you the museum. You give us the state.) The Naples Museum of Art')
    assert result == 'Florida'


def test_q7():
    results = ir.run_query('"TIN" MEN This Italian painter depicted the "Adoration of the Golden Calf"')
    assert results == 'Tintoretto'


def test_q8():
    result = ir.run_query('UCLA CELEBRITY ALUMNI This woman who won consecutive heptathlons at the Olympics went to UCLA on a basketball scholarship')
    assert result == 'Jackie Joyner-Kersee'


def test_q9():
    result = ir.run_query('SERVICE ORGANIZATIONS Originally this club\'s emblem was a wagon wheel; now it\'s a gearwheel with 24 cogs & 6 spokes')
    assert result == 'Rotary International'


def test_q10():
    result = ir.run_query('AFRICAN CITIES Several bridges, including El Tahrir, cross the Nile in this capital')
    assert result == 'Cairo'

def test_q11():
    result = ir.run_query('HISTORICAL QUOTES After the fall of France in 1940, this general told his country, "France has lost a battle. But France has not lost the war"')
    assert ((result == 'Charles de Gaulle') or (result == 'de Gaulle'))

def test_q12():
    result = ir.run_query('STATE OF THE ART MUSEUM (Alex: We\'ll give you the museum. You give us the state.) The Taft Museum of Art')
    assert result == 'Ohio'

def test_q13():
    result = ir.run_query('CEMETERIES The mast from the USS Maine is part of the memorial to the ship & crew at this national cemetery')
    assert ((result == 'Arlington National Cemetery') or (result == 'Arlington Cemetery'))

def test_q14():
    result = ir.run_query('GOLDEN GLOBE WINNERS In 2009: Joker on film')
    assert result == 'Heath Ledger'

def test_q15():
    result = ir.run_query('HISTORICAL HODGEPODGE It was the peninsula fought over in the peninsular war of 1808 to 1814')
    assert ((result == 'Iberia') or (result == 'Iberian Peninsula'))

def test_q16():
    result = ir.run_query('CONSERVATION In 1980 China founded a center for these cute creatures in its bamboo-rich Wolong Nature Preserve')
    assert ((result == 'Panda') or (result == 'Giant panda'))

def test_q17():
    result = ir.run_query('\'80s NO.1 HITMAKERS 1988: "Father Figure"')
    assert result == 'George Michael'

def test_q18():
    result = ir.run_query('AFRICAN-AMERICAN WOMEN In an essay defending this 2011 film, Myrlie Evers-Williams said, "My mother was" this film "& so was her mother"')
    assert result == 'The Help'

def test_q19():
    result = ir.run_query('SERVICE ORGANIZATIONS Father Michael McGivney founded this fraternal society for Catholic laymen in 1882')
    assert result == 'Knights of Columbus'

def test_q20():
    result = ir.run_query('CONSERVATION Early projects of the WWF, this organization, included work with the bald eagle & the red wolf')
    assert ((result == 'World Wide Fund') or (result == 'World Wide Fund for Nature'))

def test_q21():
    result = ir.run_query('CONSERVATION Indonesia\'s largest lizard, it\'s protected from poachers, though we wish it could breathe fire to do the job itself')
    assert result == 'Komodo dragon'

def test_q22():
    result = ir.run_query('1920s NEWS FLASH! Nov. 28, 1929! This man & his chief pilot Bernt Balchen fly to South Pole! Yowza! You\'ll be an admirable admiral, sir!')
    assert ((result == 'Richard Byrd') or (result == 'Richard E. Byrd'))

def test_q23():
    result = ir.run_query('CEMETERIES On May 5, 1878 Alice Chambers was the last person buried in this Dodge City, Kansas cemetery')
    assert result == 'Boot Hill'

def test_q24():
    result = ir.run_query('CAMBODIAN HISTORY & CULTURE The Royal Palace grounds feature a statue of King Norodom, who in the late 1800s was compelled to first put his country under the control of this European power; of course, it was sculpted in that country')
    assert result == 'France'

def test_q25():
    result = ir.run_query('HISTORICAL HODGEPODGE In the 400s B.C. this Chinese philosopher went into exile for 12 years')
    assert result == 'Confucius'

def test_q26():
    result = ir.run_query('AFRICAN-AMERICAN WOMEN Bessie Coleman, the first black woman licensed as a pilot, landed a street named in her honor at this Chicago airport')
    assert ((result == 'O\'Hare') or (result == 'O\'Hare International Airport'))

def test_q27():
    result = ir.run_query('HISTORICAL HODGEPODGE The Ammonites held sway in this Mideast country in the 1200s B.C. & the capital is named for them')
    assert result == 'Jordan'

def test_q28():
    result = ir.run_query('HE PLAYED A GUY NAMED JACK RYAN IN... "The Sum of All Fears"; he also won a screenwriting Oscar for "Good Will Hunting"')
    assert result == 'Ben Affleck'

def test_q29():
    result = ir.run_query('POTPOURRI One of the N.Y. Times\' headlines on this landmark 1973 Supreme Court decision was "Cardinals shocked"')
    assert result == 'Roe v. Wade'

def test_q30():
    result = ir.run_query('I\'M BURNIN\' FOR YOU France\'s Philip IV--known as "The Fair"--had Jacques De Molay, the last Grand Master of this order, burned in 1314')
    assert result == 'Knights Templar'