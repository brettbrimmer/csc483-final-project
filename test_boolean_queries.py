# DO NOT modify code except "YOUR CODE GOES HERE" blocks

from pytest import approx

import tfidf_engine

# ir = tfidf_engine.IRSystem(open("wiki-small.txt"))
ir = tfidf_engine.IRSystem("wikisubset")

# print("Running tests!")
with open("printstatements.txt", "a") as newFile: newFile.write("Running tests!\n\n")


## TODO: We have to change this to test for Jeopardy questions vs. answers:
"""

BROADWAY LYRICS
Song that says, "you make me smile with my heart; your looks are laughable, unphotographable"
My Funny Valentine

"""
## TODO: Ignore first line. It's just a Jeopardy category and is repeated among many questions
## I believe the query we will run is the second line
## result should == third line i.e. it will be a string result

def save_output_to_file(output, correct_answer, file_name):
    with open(file_name, "a", encoding="utf-8") as f:
        f.write(f"Correct Answer: {correct_answer}\n")

        if(correct_answer in output):
            f.write(f"ANSWER FOUND FOR {correct_answer}")

        if isinstance(output, list):
            for idx, item in enumerate(output[:600], start=1):
                f.write(f"{idx}. {item}\n")
        else:
            f.write(str(output).strip() + "\n")


def test_q1():
    result = ir.run_query('NEWSPAPERS The dominant paper in our nation\'s capital, it\'s among the top 10 U.S. papers in circulation')
    save_output_to_file(str(result), 'The Washington Post', "pytest_output.txt")
    assert result == 'The Washington Post'


def test_q2():
    result = ir.run_query('OLD YEAR\'S RESOLUTIONS The practice of pre-authorizing presidential use of force dates to a 1955 resolution re: this island near mainland China')
    save_output_to_file(str(result), 'Taiwan', "pytest_output.txt")
    assert result == 'Taiwan'


def test_q3():
    result = ir.run_query('NEWSPAPERS Daniel Hertzberg & James B. Stewart of this paper shared a 1988 Pulitzer for their stories about insider trading')
    save_output_to_file(str(result), 'The Wall Street Journal', "pytest_output.txt")
    assert result == 'The Wall Street Journal'


def test_q4():
    result = ir.run_query('BROADWAY LYRICS Song that says, "you make me smile with my heart; your looks are laughable, unphotographable"')
    save_output_to_file(str(result), 'My Funny Valentine', "pytest_output.txt")
    assert result == 'My Funny Valentine'


def test_q5():
    result = ir.run_query('POTPOURRI In 2011 bell ringers for this charity started accepting digital donations to its red kettle')
    save_output_to_file(str(result), 'The Salvation Army', "pytest_output.txt")
    save_output_to_file(str(result), 'Salvation Army', "pytest_output.txt")
    assert ((result == 'The Salvation Army') or (result == 'Salvation Army'))


def test_q6():
    result = ir.run_query('STATE OF THE ART MUSEUM (Alex: We\'ll give you the museum. You give us the state.) The Naples Museum of Art')
    save_output_to_file(str(result), 'Florida', "pytest_output.txt")
    assert result == 'Florida'


def test_q7():
    result = ir.run_query('"TIN" MEN This Italian painter depicted the "Adoration of the Golden Calf"')
    save_output_to_file(str(result), 'Tintoretto', "pytest_output.txt")
    assert result == 'Tintoretto'


def test_q8():
    result = ir.run_query('UCLA CELEBRITY ALUMNI This woman who won consecutive heptathlons at the Olympics went to UCLA on a basketball scholarship')
    save_output_to_file(str(result), 'Jackie Joyner-Kersee', "pytest_output.txt")
    assert result == 'Jackie Joyner-Kersee'


def test_q9():
    result = ir.run_query('SERVICE ORGANIZATIONS Originally this club\'s emblem was a wagon wheel; now it\'s a gearwheel with 24 cogs & 6 spokes')
    save_output_to_file(str(result), 'Rotary International', "pytest_output.txt")
    assert result == 'Rotary International'


def test_q10():
    result = ir.run_query('AFRICAN CITIES Several bridges, including El Tahrir, cross the Nile in this capital')
    save_output_to_file(str(result), 'Cairo', "pytest_output.txt")
    assert result == 'Cairo'

def test_q11():
    result = ir.run_query('HISTORICAL QUOTES After the fall of France in 1940, this general told his country, "France has lost a battle. But France has not lost the war"')
    save_output_to_file(str(result), 'Charles de Gaulle', "pytest_output.txt")
    save_output_to_file(str(result), 'de Gaulle', "pytest_output.txt")
    assert ((result == 'Charles de Gaulle') or (result == 'de Gaulle'))

def test_q12():
    result = ir.run_query('STATE OF THE ART MUSEUM (Alex: We\'ll give you the museum. You give us the state.) The Taft Museum of Art')
    save_output_to_file(str(result), 'Ohio', "pytest_output.txt")
    assert result == 'Ohio'

def test_q13():
    result = ir.run_query('CEMETERIES The mast from the USS Maine is part of the memorial to the ship & crew at this national cemetery')
    save_output_to_file(str(result), 'Arlington National Cemetery', "pytest_output.txt")
    save_output_to_file(str(result), 'Arlington Cemetery', "pytest_output.txt")
    assert ((result == 'Arlington National Cemetery') or (result == 'Arlington Cemetery'))

def test_q14():
    result = ir.run_query('GOLDEN GLOBE WINNERS In 2009: Joker on film')
    save_output_to_file(str(result), 'Heath Ledger', "pytest_output.txt")
    assert result == 'Heath Ledger'

def test_q15():
    result = ir.run_query('HISTORICAL HODGEPODGE It was the peninsula fought over in the peninsular war of 1808 to 1814')
    save_output_to_file(str(result), 'Iberia', "pytest_output.txt")
    save_output_to_file(str(result), 'Iberian Peninsula', "pytest_output.txt")
    assert ((result == 'Iberia') or (result == 'Iberian Peninsula'))

def test_q16():
    result = ir.run_query('CONSERVATION In 1980 China founded a center for these cute creatures in its bamboo-rich Wolong Nature Preserve')
    save_output_to_file(str(result), 'Panda', "pytest_output.txt")
    save_output_to_file(str(result), 'Giant panda', "pytest_output.txt")
    assert ((result == 'Panda') or (result == 'Giant panda'))

def test_q17():
    result = ir.run_query('\'80s NO.1 HITMAKERS 1988: "Father Figure"')
    save_output_to_file(str(result), 'George Michael', "pytest_output.txt")
    assert result == 'George Michael'

def test_q18():
    result = ir.run_query('AFRICAN-AMERICAN WOMEN In an essay defending this 2011 film, Myrlie Evers-Williams said, "My mother was" this film "& so was her mother"')
    save_output_to_file(str(result), 'The Help', "pytest_output.txt")
    assert result == 'The Help'

def test_q19():
    result = ir.run_query('SERVICE ORGANIZATIONS Father Michael McGivney founded this fraternal society for Catholic laymen in 1882')
    save_output_to_file(str(result), 'Knights of Columbus', "pytest_output.txt")
    assert result == 'Knights of Columbus'

def test_q20():
    result = ir.run_query('CONSERVATION Early projects of the WWF, this organization, included work with the bald eagle & the red wolf')
    save_output_to_file(str(result), 'World Wide Fund', "pytest_output.txt")
    save_output_to_file(str(result), 'World Wide Fund for Nature', "pytest_output.txt")
    assert ((result == 'World Wide Fund') or (result == 'World Wide Fund for Nature'))

def test_q21():
    result = ir.run_query('CONSERVATION Indonesia\'s largest lizard, it\'s protected from poachers, though we wish it could breathe fire to do the job itself')
    save_output_to_file(str(result), 'Komodo dragon', "pytest_output.txt")
    assert result == 'Komodo dragon'

def test_q22():
    result = ir.run_query('1920s NEWS FLASH! Nov. 28, 1929! This man & his chief pilot Bernt Balchen fly to South Pole! Yowza! You\'ll be an admirable admiral, sir!')
    save_output_to_file(str(result), 'Richard Byrd', "pytest_output.txt")
    save_output_to_file(str(result), 'Richard E. Byrd', "pytest_output.txt")
    assert ((result == 'Richard Byrd') or (result == 'Richard E. Byrd'))

def test_q23():
    result = ir.run_query('CEMETERIES On May 5, 1878 Alice Chambers was the last person buried in this Dodge City, Kansas cemetery')
    save_output_to_file(str(result), 'Boot Hill', "pytest_output.txt")
    assert result == 'Boot Hill'

def test_q24():
    result = ir.run_query('CAMBODIAN HISTORY & CULTURE The Royal Palace grounds feature a statue of King Norodom, who in the late 1800s was compelled to first put his country under the control of this European power; of course, it was sculpted in that country')
    save_output_to_file(str(result), 'France', "pytest_output.txt")
    assert result == 'France'

def test_q25():
    result = ir.run_query('HISTORICAL HODGEPODGE In the 400s B.C. this Chinese philosopher went into exile for 12 years')
    save_output_to_file(str(result), 'Confucius', "pytest_output.txt")
    assert result == 'Confucius'

def test_q26():
    result = ir.run_query('AFRICAN-AMERICAN WOMEN Bessie Coleman, the first black woman licensed as a pilot, landed a street named in her honor at this Chicago airport')
    save_output_to_file(str(result), 'O\'Hare', "pytest_output.txt")
    save_output_to_file(str(result), 'O\'Hare International Airport', "pytest_output.txt")
    assert ((result == 'O\'Hare') or (result == 'O\'Hare International Airport'))

def test_q27():
    result = ir.run_query('HISTORICAL HODGEPODGE The Ammonites held sway in this Mideast country in the 1200s B.C. & the capital is named for them')
    save_output_to_file(str(result), 'Jordan', "pytest_output.txt")
    assert result == 'Jordan'

def test_q28():
    result = ir.run_query('HE PLAYED A GUY NAMED JACK RYAN IN... "The Sum of All Fears"; he also won a screenwriting Oscar for "Good Will Hunting"')
    save_output_to_file(str(result), 'Ben Affleck', "pytest_output.txt")
    assert result == 'Ben Affleck'

def test_q29():
    result = ir.run_query('POTPOURRI One of the N.Y. Times\' headlines on this landmark 1973 Supreme Court decision was "Cardinals shocked"')
    save_output_to_file(str(result), 'Roe v. Wade', "pytest_output.txt")
    assert result == 'Roe v. Wade'

def test_q30():
    result = ir.run_query('I\'M BURNIN\' FOR YOU France\'s Philip IV--known as "The Fair"--had Jacques De Molay, the last Grand Master of this order, burned in 1314')
    save_output_to_file(str(result), 'Knights Templar', "pytest_output.txt")
    assert result == 'Knights Templar'

def test_q31():
    result = ir.run_query('STATE OF THE ART MUSEUM (Alex: We\'ll give you the museum. You give us the state.) The Georgia O\'Keeffe Museum')
    save_output_to_file(str(result), 'New Mexico', "pytest_output.txt")
    assert result == 'New Mexico'

def test_q32():
    result = ir.run_query('AFRICAN CITIES The name of this largest Moroccan city combines 2 Spanish words')
    save_output_to_file(str(result), 'Casablanca', "pytest_output.txt")
    assert result == 'Casablanca'

def test_q33():
    result = ir.run_query('NAME THE PARENT COMPANY Jell-O')
    save_output_to_file(str(result), 'Kraft Foods', "pytest_output.txt")
    assert result == 'Kraft Foods'

def test_q34():
    result = ir.run_query('GOLDEN GLOBE WINNERS 2011: Chicago mayor Tom Kane')
    save_output_to_file(str(result), 'Kelsey Grammer', "pytest_output.txt")
    assert result == 'Kelsey Grammer'

def test_q35():
    result = ir.run_query('THE RESIDENTS Title residence of Otter, Flounder, Pinto & Bluto in a 1978 comedy')
    save_output_to_file(str(result), 'Animal House', "pytest_output.txt")
    assert result == 'Animal House'

def test_q36():
    result = ir.run_query('UCLA CELEBRITY ALUMNI Neurobiologist Amy Farrah Fowler on "The Big Bang Theory", in real life she has a Ph.D. in neuroscience from UCLA')
    save_output_to_file(str(result), 'Mayim Bialik', "pytest_output.txt")
    assert result == 'Mayim Bialik'

def test_q37():
    result = ir.run_query('NOTES FROM THE CAMPAIGN TRAIL In "The Deadlocked Election of 1800", James R. Sharp outlines the fall of this dueling vice president')
    save_output_to_file(str(result), 'Aaron Burr', "pytest_output.txt")
    assert result == 'Aaron Burr'

def test_q38():
    result = ir.run_query('"TIN" MEN He served in the KGB before becoming president & then prime minister of Russia')
    save_output_to_file(str(result), 'Vladimir Putin', "pytest_output.txt")
    save_output_to_file(str(result), 'Putin', "pytest_output.txt")
    assert ((result == 'Vladimir Putin') or (result == 'Putin'))

def test_q39():
    result = ir.run_query('AFRICAN-AMERICAN WOMEN When asked to describe herself, she says first & foremost, she is Malia & Sasha\'s mom')
    save_output_to_file(str(result), 'Michelle Obama', "pytest_output.txt")
    assert result == 'Michelle Obama'

def test_q40():
    result = ir.run_query('POETS & POETRY She wrote, "My candle burns at both ends... but, ah, my foes, and oh, my friends--it gives a lovely light"')
    save_output_to_file(str(result), 'Edna St. Vincent Millay', "pytest_output.txt")
    assert result == 'Edna St. Vincent Millay'

def test_q41():
    result = ir.run_query('CAPITAL CITY CHURCHES (Alex: We\'ll give you the church. You tell us the capital city in which it is located.) In this Finnish city, the Lutheran Cathedral, also known as Tuomiokirkko')
    save_output_to_file(str(result), 'Helsinki', "pytest_output.txt")
    assert result == 'Helsinki'

def test_q42():
    result = ir.run_query('NAME THE PARENT COMPANY Milton Bradley games')
    save_output_to_file(str(result), 'Hasbro', "pytest_output.txt")
    assert result == 'Hasbro'

def test_q43():
    result = ir.run_query('OLD YEAR\'S RESOLUTIONS The Kentucky & Virginia resolutions were passed to protest these controversial 1798 acts of Congress')
    save_output_to_file(str(result), 'The Alien and Sedition Acts', "pytest_output.txt")
    assert result == 'The Alien and Sedition Acts'

def test_q44():
    result = ir.run_query('\'80s NO.1 HITMAKERS 1983: "Beat It"')
    save_output_to_file(str(result), 'Michael Jackson', "pytest_output.txt")
    assert result == 'Michael Jackson'

def test_q45():
    result = ir.run_query('GOLDEN GLOBE WINNERS In 2009: Sookie Stackhouse')
    save_output_to_file(str(result), 'Anna Paquin', "pytest_output.txt")
    assert result == 'Anna Paquin'

def test_q46():
    result = ir.run_query('HISTORICAL HODGEPODGE This member of the Nixon & Ford cabinets was born in Furth, Germany in 1923')
    save_output_to_file(str(result), 'Henry Kissinger', "pytest_output.txt")
    assert result == 'Henry Kissinger'

def test_q47():
    result = ir.run_query('CAPITAL CITY CHURCHES (Alex: We\'ll give you the church. You tell us the capital city in which it is located.) The High Kirk of St. Giles, where John Knox was minister')
    save_output_to_file(str(result), 'Edinburgh', "pytest_output.txt")
    assert result == 'Edinburgh'

def test_q48():
    result = ir.run_query('UCLA CELEBRITY ALUMNI For the brief time he attended, he was a rebel with a cause, even landing a lead role in a 1950 stage production')
    save_output_to_file(str(result), 'James Dean', "pytest_output.txt")
    assert result == 'James Dean'

def test_q49():
    result = ir.run_query('NAME THE PARENT COMPANY Fisher-Price toys')
    save_output_to_file(str(result), 'Mattel', "pytest_output.txt")
    assert result == 'Mattel'

def test_q50():
    result = ir.run_query('HISTORICAL QUOTES In a 1959 American kitchen exhibit in Moscow, he told Khrushchev, "In America, we like to make life easier for women"')
    save_output_to_file(str(result), 'Richard Nixon', "pytest_output.txt")
    save_output_to_file(str(result), 'Nixon', "pytest_output.txt")
    assert ((result == 'Richard Nixon') or (result == 'Nixon'))

def test_q51():
    result = ir.run_query('POETS & POETRY One of his "Tales of a Wayside Inn" begins, "Listen, my children, and you shall hear of the midnight ride of Paul Revere"')
    save_output_to_file(str(result), 'Henry Wadsworth Longfellow', "pytest_output.txt")
    assert result == 'Henry Wadsworth Longfellow'

def test_q52():
    result = ir.run_query('NOTES FROM THE CAMPAIGN TRAIL This bestseller about problems on the McCain-Palin ticket became an HBO movie with Julianne Moore')
    save_output_to_file(str(result), 'Game Change', "pytest_output.txt")
    assert result == 'Game Change'

def test_q53():
    result = ir.run_query('THAT 20-AUGHTS SHOW A 2-part episode of "JAG" introduced this Mark Harmon drama')
    save_output_to_file(str(result), 'NCIS', "pytest_output.txt")
    assert result == 'NCIS'

def test_q54():
    result = ir.run_query('AFRICAN CITIES This port is the southernmost of South Africa\'s 3 capitals')
    save_output_to_file(str(result), 'Cape Town', "pytest_output.txt")
    assert result == 'Cape Town'

def test_q55():
    result = ir.run_query('THE QUOTABLE KEATS Keats was quoting this Edmund Spenser poem when he told Shelley to "\'load every rift\' of your subject with ore"')
    save_output_to_file(str(result), 'The Faerie Queene', "pytest_output.txt")
    assert result == 'The Faerie Queene'

def test_q56():
    result = ir.run_query('THE QUOTABLE KEATS In an 1819 letter Keats wrote that this lord & poet "cuts a figure, but he is not figurative"')
    save_output_to_file(str(result), 'Lord Byron', "pytest_output.txt")
    assert result == 'Lord Byron'

def test_q57():
    result = ir.run_query('GREEK FOOD & DRINK This clear Greek liqueur is quite potent, so it\'s usually mixed with water, which turns it white & cloudy')
    save_output_to_file(str(result), 'Ouzo', "pytest_output.txt")
    assert result == 'Ouzo'

def test_q58():
    result = ir.run_query('OLD YEAR\'S RESOLUTIONS Feb. 1, National Freedom Day, is the date in 1865 when a resolution sent the states an amendment ending this')
    save_output_to_file(str(result), 'Slavery', "pytest_output.txt")
    save_output_to_file(str(result), 'Slavery in the United States', "pytest_output.txt")
    assert ((result == 'Slavery') or (result == 'Slavery in the United States'))

def test_q59():
    result = ir.run_query('RANKS & TITLES This person is the queen\'s representative in Canada; currently the office is held by David Johnston')
    save_output_to_file(str(result), 'Governor General of Canada', "pytest_output.txt")
    assert result == 'Governor General of Canada'

def test_q60():
    result = ir.run_query('"TIN" MEN He earned the "fifth Beatle" nickname by producing all of the Beatles\' albums')
    save_output_to_file(str(result), 'George Martin', "pytest_output.txt")
    assert result == 'George Martin'

def test_q61():
    result = ir.run_query('NEWSPAPERS Early in their careers, Mark Twain & Bret Harte wrote pieces for this California city\'s Chronicle')
    save_output_to_file(str(result), 'San Francisco', "pytest_output.txt")
    assert result == 'San Francisco'

def test_q62():
    result = ir.run_query('POTPOURRI Large specimens of this marsupial can leap over barriers 6 feet high')
    save_output_to_file(str(result), 'Kangaroo', "pytest_output.txt")
    assert result == 'Kangaroo'

def test_q63():
    result = ir.run_query('GREEK FOOD & DRINK Because it\'s cured & stored in brine, this crumbly white cheese made from sheep\'s milk is often referred to as pickled cheese')
    save_output_to_file(str(result), 'Feta', "pytest_output.txt")
    assert result == 'Feta'

def test_q64():
    result = ir.run_query('1920s NEWS FLASH! 1927! Gene Tunney takes a long count in the squared circle but rises to defeat this "Manassa Mauler"! Howzabout that!')
    save_output_to_file(str(result), 'Jack Dempsey', "pytest_output.txt")
    assert result == 'Jack Dempsey'

def test_q65():
    result = ir.run_query('RANKS & TITLES Italian for "leader", it was especially applied to Benito Mussolini')
    save_output_to_file(str(result), 'Duce', "pytest_output.txt")
    assert result == 'Duce'

def test_q66():
    result = ir.run_query('STATE OF THE ART MUSEUM (Alex: We\'ll give you the museum. You give us the state.) The Kalamazoo Institute of Arts')
    save_output_to_file(str(result), 'Michigan', "pytest_output.txt")
    assert result == 'Michigan'

def test_q67():
    result = ir.run_query('STATE OF THE ART MUSEUM (Alex: We\'ll give you the museum. You give us the state.) The Sun Valley Center for the Arts')
    save_output_to_file(str(result), 'Idaho', "pytest_output.txt")
    assert result == 'Idaho'

def test_q68():
    result = ir.run_query('"TIN" MEN You can\'t mention this shortstop without mentioning his double-play associates Evers & Chance')
    save_output_to_file(str(result), 'Joe Tinker', "pytest_output.txt")
    assert result == 'Joe Tinker'

def test_q69():
    result = ir.run_query('NEWSPAPERS In 1840 Horace Greeley began publishing "The Log Cabin", a weekly campaign paper in support of this Whig candidate')
    save_output_to_file(str(result), 'William Henry Harrison', "pytest_output.txt")
    assert result == 'William Henry Harrison'

def test_q70():
    result = ir.run_query('I\'M BURNIN\' FOR YOU Pierre Cauchon, Bishop of Beauvais, presided over the trial of this woman who went up in smoke May 30, 1431')
    save_output_to_file(str(result), 'Joan of Arc', "pytest_output.txt")
    save_output_to_file(str(result), 'Jeanne d\'Arc', "pytest_output.txt")
    assert ((result == 'Joan of Arc') or (result == 'Jeanne d\'Arc'))

def test_q71():
    result = ir.run_query('COMPLETE DOM-INATION(Alex: Not "domination.") This Wisconsin city claims to have built the USA\'s only granite dome')
    save_output_to_file(str(result), 'Madison', "pytest_output.txt")
    assert result == 'Madison'

def test_q72():
    result = ir.run_query('NEWSPAPERS This Georgia paper is known as the AJC for short')
    save_output_to_file(str(result), 'The Atlanta Journal-Constitution', "pytest_output.txt")
    assert result == 'The Atlanta Journal-Constitution'

def test_q73():
    result = ir.run_query('AFRICAN CITIES Wooden 2-story verandas in this Liberian capital are an architectural link to the U.S. south')
    save_output_to_file(str(result), 'Monrovia', "pytest_output.txt")
    assert result == 'Monrovia'

def test_q74():
    result = ir.run_query('COMPLETE DOM-INATION(Alex: Not "domination.") This New Orleans venue reopened Sept. 25, 2006')
    save_output_to_file(str(result), 'Mercedes-Benz Superdome', "pytest_output.txt")
    save_output_to_file(str(result), 'The Superdome', "pytest_output.txt")
    assert ((result == 'Mercedes-Benz Superdome') or (result == 'The Superdome'))

def test_q75():
    result = ir.run_query('HE PLAYED A GUY NAMED JACK RYAN IN... "The Hunt for Red October"; he went more comedic as Jack Donaghy on "30 Rock"')
    save_output_to_file(str(result), 'Alec Baldwin', "pytest_output.txt")
    assert result == 'Alec Baldwin'

def test_q76():
    result = ir.run_query('AFRICAN-AMERICAN WOMEN Rita Dove titled a collection of poems "On the Bus with" this woman')
    save_output_to_file(str(result), 'Rosa Parks', "pytest_output.txt")
    assert result == 'Rosa Parks'

def test_q77():
    result = ir.run_query('HE PLAYED A GUY NAMED JACK RYAN IN... "Patriot Games"; he\'s had other iconic roles, in space & underground')
    save_output_to_file(str(result), 'Harrison Ford', "pytest_output.txt")
    assert result == 'Harrison Ford'

def test_q78():
    result = ir.run_query('COMPLETE DOM-INATION(Alex: Not "domination.") This sacred structure dates from the late 600\'s A.D.')
    save_output_to_file(str(result), 'Dome of the Rock', "pytest_output.txt")
    assert result == 'Dome of the Rock'

def test_q79():
    result = ir.run_query('\'80s NO.1 HITMAKERS 1988: "Man In The Mirror"')
    save_output_to_file(str(result), 'Michael Jackson', "pytest_output.txt")
    assert result == 'Michael Jackson'

def test_q80():
    result = ir.run_query('CAPITAL CITY CHURCHES (Alex: We\'ll give you the church. You tell us the capital city in which it is located.) Matthias Church, or Matyas Templom, where Franz Joseph was crowned in 1867')
    save_output_to_file(str(result), 'Budapest', "pytest_output.txt")
    assert result == 'Budapest'

def test_q81():
    result = ir.run_query('UCLA CELEBRITY ALUMNI Attending UCLA in the \'60s, he was no "Meathead", he just played one later on television')
    save_output_to_file(str(result), 'Rob Reiner', "pytest_output.txt")
    assert result == 'Rob Reiner'

def test_q82():
    result = ir.run_query('THE RESIDENTS Kinch, Carter & LeBeau were all residents of Stalag 13 on this TV show')
    save_output_to_file(str(result), 'Hogan\'s Heroes', "pytest_output.txt")
    assert result == ''

def test_q83():
    result = ir.run_query('1920s NEWS FLASH! News flash! This less-than-yappy pappy is sixth veep to be nation\'s top dog after chief takes deep sleep!')
    save_output_to_file(str(result), 'Calvin Coolidge', "pytest_output.txt")
    assert result == 'Calvin Coolidge'

def test_q84():
    result = ir.run_query('GOLDEN GLOBE WINNERS In 2001: The president of the United States on television')
    save_output_to_file(str(result), 'Martin Sheen', "pytest_output.txt")
    assert result == 'Martin Sheen'

def test_q85():
    result = ir.run_query('\'80s NO.1 HITMAKERS 1989: "Miss You Much"')
    save_output_to_file(str(result), 'Janet Jackson', "pytest_output.txt")
    assert result == 'Janet Jackson'

def test_q86():
    result = ir.run_query('1920s NEWS FLASH! 1922: It\'s the end of an empire! This empire, in fact! After 600 years, it\'s goodbye, this, hello, Turkish Republic!')
    save_output_to_file(str(result), 'Ottoman Empire', "pytest_output.txt")
    assert result == 'Ottoman Empire'

def test_q87():
    result = ir.run_query('NAME THE PARENT COMPANY Crest toothpaste')
    save_output_to_file(str(result), 'Procter & Gamble', "pytest_output.txt")
    assert result == 'Procter & Gamble'

def test_q88():
    result = ir.run_query('HISTORICAL QUOTES In 1888 this Chancellor told the Reichstag, "we Germans fear God, but nothing else in the world"')
    save_output_to_file(str(result), 'Otto von Bismarck', "pytest_output.txt")
    save_output_to_file(str(result), 'Von Bismarck', "pytest_output.txt")
    assert ((result == 'Otto von Bismarck') or (result == 'Von Bismarck'))

def test_q89():
    result = ir.run_query('POETS & POETRY In 1787 he signed his first published poem "Axiologus"; axio- is from the Greek for "worth"')
    save_output_to_file(str(result), 'William Wordsworth', "pytest_output.txt")
    assert result == 'William Wordsworth'

def test_q90():
    result = ir.run_query('CAMBODIAN HISTORY & CULTURE Not to be confused with karma, krama is a popular accessory sold in cambodia; the word means "scarf" in this national language of Cambodia')
    save_output_to_file(str(result), 'Khmer language', "pytest_output.txt")
    assert result == 'Khmer language'

def test_q91():
    result = ir.run_query('CAMBODIAN HISTORY & CULTURE Phnom Penh\'s notorious gridlock is circumvented by the nimble tuk-tuk, a motorized taxi that\'s also known as an auto this, a similar Asian conveyance.')
    save_output_to_file(str(result), 'Rickshaw', "pytest_output.txt")
    assert result == 'Rickshaw'

def test_q92():
    result = ir.run_query('\'80s NO.1 HITMAKERS 1980: "Rock With You"')
    save_output_to_file(str(result), 'Michael Jackson', "pytest_output.txt")
    assert result == 'Michael Jackson'

def test_q93():
    result = ir.run_query('NOTES FROM THE CAMPAIGN TRAIL The Pulitzer-winning "The Making of the President 1960" covered this man\'s successful presidential campaign')
    save_output_to_file(str(result), 'JFK', "pytest_output.txt")
    save_output_to_file(str(result), 'John F. Kennedy', "pytest_output.txt")
    assert ((result == 'JFK') or (result == 'John F. Kennedy'))

def test_q94():
    result = ir.run_query('SERVICE ORGANIZATIONS In 1843 Isaac Dittenhoefer became the first pres. of this Jewish club whose name means "children of the covenant"')
    save_output_to_file(str(result), 'B\'nai B\'rith', "pytest_output.txt")
    assert result == 'B\'nai B\'rith'

def test_q95():
    result = ir.run_query('THE RESIDENTS Don Knotts took over from Norman Fell as the resident landlord on this sitcom')
    save_output_to_file(str(result), 'Three\'s Company', "pytest_output.txt")
    assert result == 'Three\'s Company'

def test_q96():
    result = ir.run_query('OLD YEAR\'S RESOLUTIONS U.N. Res. 242 supports "secure and recognized boundaries" for Israel & neighbors following this June 1967 war')
    save_output_to_file(str(result), 'The Six Day War', "pytest_output.txt")
    assert result == 'The Six Day War'

def test_q97():
    result = ir.run_query('UCLA CELEBRITY ALUMNI This blonde beauty who reprised her role as Amanda on the new "Melrose Place" was a psychology major')
    save_output_to_file(str(result), 'Heather Locklear', "pytest_output.txt")
    assert result == 'Heather Locklear'

def test_q98():
    result = ir.run_query('GREEK FOOD & DRINK The name of this dish of marinated lamb, skewered & grilled, comes from the Greek for "skewer" & also starts with "s"')
    save_output_to_file(str(result), 'Souvlaki', "pytest_output.txt")
    assert result == 'Souvlaki'

def test_q99():
    result = ir.run_query('NAME THE PARENT COMPANY Post-it notes')
    save_output_to_file(str(result), '3M', "pytest_output.txt")
    assert result == '3M'

def test_q100():
    result = ir.run_query('GOLDEN GLOBE WINNERS In 2010: As Sherlock Holmes on film')
    save_output_to_file(str(result), 'Robert Downey, Jr.', "pytest_output.txt")
    assert result == 'Robert Downey, Jr.'