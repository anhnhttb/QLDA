from packages import *
from colors import *

# Button Urls
github_url = 'https://github.com/CyborgVillager?tab=repositories'
bitchute_url = 'https://www.bitchute.com/channel/jonathanai/'



def get_user_job_search_data(entry1, entry4):
    user_site_combination = 'https://www.monster.com/jobs/search/?q=' + entry1 + '&where=' + entry4
    url = user_site_combination
    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find(id='ResultsContainer')




##Functions##

window = Tk()

##Top info Start##

# Title for Window Screen
window.wm_title('Monster Job Search')
# Title
l1title = Label(window, text='Keyword or Title of Position:')
l1title.grid(row=0, column=0)

# Location
l2locationbn = Label(window, text='Location:')
l2locationbn.grid(row=1, column=0)

####Entries Start####
# Title of Position
title_text = StringVar()
# textvariable is spatial datatype
entry1 = Entry(window, textvariable=title_text)
entry1.grid(row=0, column=1)

# Location
isbn_text = StringVar()
entry4 = Entry(window, textvariable=isbn_text)
entry4.grid(row=1, column=1)

# Search Results
# box info width and height
list1 = Listbox(window, height=8, width=65)
list1.grid(row=3, column=0, rowspan=6, columnspan=2)
####Entries End####







# Binding the list t get the the selected row
# From user input
list1.bind('<<ListboxSelect>>', get_selected_row)


###Scroll Bar End###


#### Button Start ####
# Search



searchbt = Button(window, text='Search', width=15, command=lambda: get_user_job_search_data(entry1.get(), entry4.get()))
searchbt.grid(row=1, column=3)

# Close
closebt = Button(window, text='Exit', width=12, command=window.destroy)
closebt.grid(row=10, column=3)


# Social Buttons
# GitHub
def Open_GitHub_Url():
    webbrowser.open_new(github_url)


social0bt = Button(window, text='Github', width=12, command=Open_GitHub_Url)
social0bt.grid(row=10, column=0)


# BitChute
def Open_BitChute_Url():
    webbrowser.open_new(bitchute_url)


social1bt = Button(window, text='BitChute', width=12, command=Open_BitChute_Url)
social1bt.grid(row=10, column=1)

# wrap all all widgets
# End of Program
window.mainloop()
