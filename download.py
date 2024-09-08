import os

class Download:
    @staticmethod
    def url(url):
        Download.prepareDirectory()
        os.system(f'curl -O {url}')

    @staticmethod
    def github(repo, identifier):
        Download.prepareDirectory()
        os.system(f'''
            for /f "tokens=1,* delims=:" %a in \
            ('curl -s https://api.github.com/repos/{repo}/releases/latest ^| findstr "browser_download_url" ^| findstr "{identifier}"') \
            do \
            (curl -kOL %b)
        ''')

    @staticmethod
    def winget(name):
        os.system(f'winget install {name} --accept-package-agreements --accept-source-agreements')
    
    @staticmethod
    def prepareDirectory():
        directory = os.path.expanduser('~/Downloads/WinMe-downloads')
        if not os.path.exists(directory):
            os.mkdir(directory)
        os.chdir(directory)

    @staticmethod
    def show():
        Download.prepareDirectory()
        os.system('explorer .')

