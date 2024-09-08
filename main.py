from customtkinter import *
from download import Download
from catalog import Catalog

class App(CTk):
    def __init__(self):
        super().__init__()
        self.geometry("480x720")
        self.title('WinMe | Custom windows installer')
        self.frame = None
        self.switch_frame(MainView)

    def switch_frame(self, new_frame):
        if self.frame:
            self.frame.destroy()
        self.frame = new_frame(self)
        self.frame.pack(expand=True, fill=BOTH)


class MainView(CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        CTkLabel(self, text='WinMe Installer', font=(None, 28, 'bold')).pack(fill=X, pady=20)
        
        frame1 = CTkFrame(self)
        frame1.pack(expand=True, fill=BOTH)
        CTkLabel(frame1, text='Step 1: ReviOS', font=(None, 26, 'bold'), anchor=W).pack(fill=X, padx=(20, 0), pady=(20, 0))
        CTkLabel(frame1, text='Download latest version of AME Wizard and ReviOS Playbook and manually apply the playbook', font=(None, 18), anchor=W, wraplength=400, justify=LEFT).pack(fill=X, padx=(30, 0))
        CTkButton(frame1, text='Download files', command=self.downloadStep1).pack(pady=(30))

        frame2 = CTkFrame(self)
        frame2.pack(expand=True, fill=BOTH)
        CTkLabel(frame2, text='Step 2: WinaeroTweaker', font=(None, 26, 'bold'), anchor=W).pack(fill=X, padx=(20, 0), pady=(20, 0))
        CTkLabel(frame2, text='Download latest version of WinaeroTweaker and manually import settings from downloaded file', font=(None, 18), anchor=W, wraplength=400, justify=LEFT).pack(fill=X, padx=(30, 0))
        CTkButton(frame2, text='Download files', command=self.downloadStep2).pack(pady=(30))
        
        frame3 = CTkFrame(self)
        frame3.pack(expand=True, fill=BOTH)
        CTkLabel(frame3, text='Step 3: Additional software', font=(None, 26, 'bold'), anchor=W).pack(fill=X, padx=(20, 0), pady=(20, 0))
        CTkLabel(frame3, text='Choose from a list of custom software and configs', font=(None, 18), anchor=W, wraplength=400, justify=LEFT).pack(fill=X, padx=(30, 0))
        CTkButton(frame3, text='Choose software', command=lambda: master.switch_frame(SoftwareView)).pack(pady=(30))

    def downloadStep1(self):
        Download.github('meetrevision/playbook', '.apbx')
        Download.github('Ameliorated-LLC/trusted-uninstaller-cli', 'AME.*.exe')
        Download.show()

    def downloadStep2(self):
        Download.url('https://winaerotweaker.com/download/winaerotweaker.zip')
        Download.show()




class SoftwareView(CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.software = Catalog.read('catalog.json')

        CTkLabel(self, text='WinMe Installer', font=(None, 28, 'bold')).pack(fill=X, pady=20)
        CTkLabel(self, text='Additional software', font=(None, 26, 'bold'), anchor=W).pack(fill=X, padx=(20, 0), pady=(20, 0))
        
        frame = CTkScrollableFrame(self)
        frame.pack(expand=True, fill=BOTH, padx=10, pady=10)

        widgets = []
        self.checkbox_vars = {}
        for item in self.software['winget']:
            self.checkbox_vars[item['name']] = BooleanVar(value=True)
            widgets.append((
                CTkCheckBox(frame, text='', variable=self.checkbox_vars[item['name']], onvalue=True, offvalue=False),
                CTkLabel(frame, text=item['name'], anchor=W),
                CTkLabel(frame, text='winget', anchor=W)
            ))
        for i, group in enumerate(widgets):
            group[0].grid(row=i, column=0, sticky=NSEW)
            group[1].grid(row=i, column=1, sticky=NSEW)
            group[2].grid(row=i, column=2, sticky=NSEW)
        frame.columnconfigure(0, weight=1)
        frame.columnconfigure(1, weight=5)
        frame.columnconfigure(2, weight=2)

        CTkButton(self, text='Cancel', command=lambda: master.switch_frame(MainView)).pack(side=LEFT, expand=True, padx=10, pady=(10, 30))
        CTkButton(self, text='Install', command=self.install).pack(side=LEFT, expand=True, padx=10, pady=(10, 30))

    def install(self): 
        print()
        for name, checkbox in self.checkbox_vars.items():
            if checkbox.get():
                # winget
                for item in self.software['winget']:
                    if item['name'] == name:
                        Download.winget(item['package'])

                # case 2
                # case 3



if __name__ == '__main__':
    app = App()
    app.mainloop()
