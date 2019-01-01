from webAccess import *

root = Tk()
root.resizable(False, False)
root.title('Chrome - Google - Dictionary')


class UserInterface:

    def stage1(self):
        self.frame1 = ttk.LabelFrame(root, height = 250, width = 200, text = 'SEARCH FIELD', )
        self.frame1.config(relief=RIDGE)
        self.frame1.pack(side=LEFT)

    def inputField(self):
        self.entry = ttk.Entry(self.frame1, text = 'Enter the value to Search')
        self.entry.place(x = 10, y = 30 , width=170, height=25)

    def searchCommand(self):
        inputValue = self.entry.get()

        a = Searching()
        t1 = threading.Thread(target=lambda: a.googleSearch(root, self.frame1, inputValue, self.button))
        t1.setDaemon(True)
        t1.start()
        self.button.configure(state = 'disabled')

    def search(self):
        self.button = ttk.Button(self.frame1, text='Search', command=self.searchCommand)
        self.button.place(x=50, y=60, width=90, height=25)