from bs4 import BeautifulSoup
import requests
import glob

bracket_list = ["Herald-Crusader", "Archon", "Legend", "Ancient", "Divine-Immortal"]
response = requests.get("https://www.dotabuff.com/heroes/meta?view=played&metric=rating_bracket", headers = {'User-agent': 'your bot 0.1'}) 
web_page = response.text
soup = BeautifulSoup(web_page, "html.parser")                                               ## taking info from https://www.dotabuff.com ##

#-------------------- FINDING HERO NAMES ------------------------------------#
tbody_hero_names = soup.select(selector="tr td a")                                          ## returns table element which contains hero names, pick rates and win rates ##

tbody_hero_list = [a.get_text() for a in tbody_hero_names]                                  ## appending names and other leftover stuff from table ##
hero_names = tbody_hero_list[1::2]                                                          ## extracts names only ( filters out random stuff) ###
hero_names.sort()
#-------------------- FINDING HERO NAMES ------------------------------------#

#-------------------------- HERO IMAGES ------------------------------------#
hero_img_list = glob.glob("heroes/*jpg") 
#-------------------------- HERO IMAGES ------------------------------------#

#-------------------- FINDING HERO WIN RATES BY BRACKET------------------------------------#
tbody_hero_names_win_rates = soup.select(selector="tr td")                                  ## shows all hero names, win rates and pick rates ##

wr_list = [a.attrs.get("data-value") for a in tbody_hero_names_win_rates if a is not None]  ## same as above, this one is only for win rate ( which depends on bracket ) ##
herald_crusader_win_rate = wr_list[3::12]
archon_win_rate = wr_list[5::12]
legend_win_rate = wr_list[7::12]
ancient_win_rate = wr_list[9::12]
divine_immortal_win_rate = wr_list[11::12]
# #-------------------- FINDING HERO WIN RATES BY BRACKET------------------------------------#

#----------------------------DICT WITH NAMES AND WIN RATES----------------------------------#
hero_dict = dict(zip(hero_names, zip(herald_crusader_win_rate, archon_win_rate, legend_win_rate, ancient_win_rate, divine_immortal_win_rate, hero_img_list )))
#----------------------------DICT WITH NAMES AND WIN RATES----------------------------------#

# print(hero_dict[hero_names[2]][5])