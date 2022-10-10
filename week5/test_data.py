import pytest, csv, random
from time import time

dataset = "./drive/MyDrive/the-reddit-climate-change-dataset-comments.csv"

class Schedule():
  def __init__(self, dataset): # step 2
        with open(dataset) as f: # step 3
            reader = csv.reader(f)
            rows = list(reader)
        self.header = rows[0]         # step 4
        self.rows = rows[1:]
        for row in self.rows:         # step 5
            row[-1] = int(row[-1])
        self.id_comment = {}             
        self.score = {}           
        for row in self.rows:                       
            self.id_comment[row[1]] = row
            self.score[int(row[9])] = row
  def messages_from_id(self, message_id):   # step 1
    for row in self.rows:                  # step 2
      if row[1] == message_id:
        return row
    return None  
  def fast_messages_from_id(self, message_id): 
    if message_id in self.id_comment:           
            return self.id_comment[message_id]
    return None                          # step 3
  def sentiment(self, lower, upper):
    sentiments = []   
    if lower > upper:
      return -1
    if lower <= 0:
      return -1
    for row in self.rows[lower:upper+1]:
        sentiments.append(row[7])    
    return sentiments
  def messages_by_sum(self, p):
    for i in (self.rows):
      for j in (self.rows):
        if int(i[9]) + int(j[9]) == p:
          return i, j
    return -1
  def fast_messages_by_sum(self, p):
    for i in (self.score):
      for j in (self.score):
        if i + j == p:
          return self.score[i], self.score[j]
    return -1

@pytest.fixture(scope="session")
def data():
    schedule = Schedule(dataset) 
    return schedule

def test_find_message_id(data):
    """
    Test 1 - Look up a dataset row based on an id, knowing that the id exists in the dataset (without using dictonary)
    """
    assert data.messages_from_id('imlddn9') == ['comment', 'imlddn9', '2qh3l', 'news', 'false', '1661990368', 'https://old.reddit.com/r/news/comments/x2cszk/us_life_expectancy_down_for_secondstraight_year/imlddn9/', 'Yeah but what the above commenter is saying is their base doesn’t want any of that. They detest all of those things, even the small gradual changes. Investing in nuclear energy is a tacit acknowledgement of man made climate change. Any acknowledgement or concession and they will be primaried out in a minute', '0.5719', 2]


def test_doesnt_find_message_id(data):
    """
    Test 2 - Look up a dataset row based on an id, knowing that the id doesn't exist in the dataset (without using dictonary)
    """
    assert data.messages_from_id('abcd1234') == None

def test_find_fast_message_id(data):
    """
    Test 3 - Look up a dataset row based on an id, knowing that the id exists in the dataset (using dictonary)
    """
    assert data.fast_messages_from_id('imlddn9') == ['comment', 'imlddn9', '2qh3l', 'news', 'false', '1661990368', 'https://old.reddit.com/r/news/comments/x2cszk/us_life_expectancy_down_for_secondstraight_year/imlddn9/', 'Yeah but what the above commenter is saying is their base doesn’t want any of that. They detest all of those things, even the small gradual changes. Investing in nuclear energy is a tacit acknowledgement of man made climate change. Any acknowledgement or concession and they will be primaried out in a minute', '0.5719', 2]

def test_doesnt_find_fast_message_id(data):
    """
    Test 4 - Look up a dataset row based on an id, knowing that the id doesn't exist in the dataset (using dictonary)
    """
    assert data.fast_messages_from_id('abcd1234') == None

def test_wout_lower_limit(data):
    """
    Test 5
    """
    assert data.sentiment(-1, 1) == -1


def test_wout_upper_limit(data):
    """
    Test 6
    """
    assert data.sentiment(2, 1) == -1

def test_w_limits(data):
    """
    Test 7
    """
    assert data.sentiment(1, 5) == ["Any comparison of efficiency between solar and fossil fuels is nonsensical at best and intentionally misleading at worst. In no universe is light -&gt; photovoltaic cell -&gt; electricity less efficient than light -&gt; entire food chain -&gt; biomass -&gt; decomposition -&gt; millions of years of geothermal heat and pressure -&gt; extraction -&gt; refining and transport -&gt; burning -&gt; turbine generator -&gt; electricity.\n\nUgly? More ugly than power lines, roads, apartment buildings, tractors, fences, etc etc etc? You're simply not used to it. Also, who cares? Sure, millions of people died in the displacement from sea rise, famines cause by climate change, and wars from resource scarcity, but thank God we didn't have to look at those solar panels occasionally.\n\nOffshore fracking? Fucks sake. Have you already forgotten the deepwater horizon disaster? Think about the damage that did to the gulf coast, add a few million barrels of highly toxic fracking fluid to the mix, and there you have our next major environmental disaster courtesy of offshore fracking. But oh man, those solar panels sure are ugly.\n\nStop repeating the lies fed to you by the people getting rich from fossil fuels, who couldn't care less about you or your descendants as long as they get theirs. We can deal with the less environmentally friendly aspects of solar power. We cannot deal with the consequences of continuing to pump carbon into the atmosphere. Y'all need to grow the fuck up and stop whining about the view.", "I'm honestly waiting for climate change and the impacts of that to kick some fucking sense into people. But who am I kidding itll still just be more of the poor suffering while the rich claim victim hood for handouts while letting us all starve. Its honestly hard some days to not just give up, and I truly wonder if and when anything will ever actually be done.", "Not just Sacramento. It's actually happening all over the world. Climate change is real, believe it or not.", 'I think climate change tends to get some people riled up. \n\nWhen I was part of a debate club, they loved throwing that subject in. One case we had to discuss was whether or not it was okay to fly if it pollutes the air. A friend of mine on the team got very worked up because he loves to travel. At the end, we actually had to make up because our disagreement about flying got very heated.', 'Naaa how could anyone be mad at a face like that... Must definitely be climate change'] 
