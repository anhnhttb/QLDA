from tkinter.font import BOLD

from packages import *
from colors import *
from tkinter_colors import *


# Main scrapper frame class initialization
class Scrapper(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()


# Main Initialization
myapp = tk.Tk()
myapp.title("Monster Job Search")

job_position_info = Label(myapp, font='Roboto', text="Job Position:")
job_position_info.pack()
# User Text Input for Job Position
e = Entry(myapp)
e.pack()
e.focus_set()

job_position_location = Label(myapp, font='Roboto', text="Location:")
job_position_location.pack()
e1 = Entry(myapp)
e1.pack()
e1.focus_set()

# Scrollbar widget
scrollbar = Scrollbar(myapp)
scrollbar.pack(side=RIGHT, fill=Y)


# Text scrap definition
def urlscrap():
    job_position_info_input = e.get()
    job_position_location_input = e1.get()
    user_job_search = 'https://www.monster.com/jobs/search/?q=' + job_position_info_input + '&where=' + \
                      job_position_location_input

    if job_position_info_input == '' or job_position_location_input == '':
        tk.messagebox.showinfo('ERROR', 'Your Input is empty please' + '\n'
                               + 'type in your job position & location')
    else:
        response = requests.get(user_job_search)
        soup = BeautifulSoup(response.text, "html.parser")
        results = soup.find(id='ResultsContainer')
        job_elements = results.find_all('section', class_='card-content')
        for job_element in job_elements:
            job_title_element = job_element.find('h2', class_='title')

            job_filter = results.find_all('h2', string=lambda text: job_position_info_input in text.lower())

        for posted_job in job_filter:
            link = posted_job.find('a')['href']
            print(posted_job.text.strip())
            print(f"Click here to apply: {link}\n")

            company_name_element = job_element.find('div', class_='company')
            location_element = job_element.find('div', class_='location')

            if None in (job_title_element, company_name_element, location_element):
                continue

            print(red + bold + str(job_title_element.text.strip()) + end)
            print(green + bold + str(company_name_element.text.strip()) + end)
            print(blue + bold + str(location_element.text.strip()) + end)
            # Spaces between the other job postings
            print()

        # Results
        job_text_info = tk.Text(myapp, background='gray25', wrap=CHAR, yscrollcommand=scrollbar.set, width=220)
        job_text_info.configure(font=(BOLD, 12), fg='orange')
        # Pack
        # link for more info https://www.tutorialspoint.com/python/tk_pack.htm
        job_text_info.pack()

        # Job Title
        job_text_info.insert(tk.END, 'Job Title: ' + posted_job.text.strip() + '\n')

        # Company Name
        job_text_info.insert(tk.END, 'Company Name: ')
        job_text_info.insert(tk.END, company_name_element.text.strip() + '\n')

        # Location
        job_text_info.insert(tk.END, 'Location: ' + location_element.text.strip() + '\n')

        # Link
        # job_text_info.insert(tk.END, posted_job.text.strip() + '\n')
        job_link = posted_job.find('a')['href']
        job_text_info.insert(tk.END, 'Link: ' + f"{job_link}\n")

        # Scroll Bar
        scrollbar.config(command=job_text_info.yview)

        result_from_monster_scrap.config(state=DISABLED)


# Scrapper button
result_from_monster_scrap = Button(myapp, text="Search", command=urlscrap)
result_from_monster_scrap.pack()

# start the program
myapp.mainloop()
