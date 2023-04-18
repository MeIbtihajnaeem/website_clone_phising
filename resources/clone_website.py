from pywebcopy import save_webpage
class CloneWebsite:
    url=""
    def __init__(self,url):
        self.url = url
    def clone(self):
        save_webpage( url=self.url,
      project_folder="./",
      project_name="project",
      bypass_robots=True,
      debug=True,
      open_in_browser=True,
      delay=None,
      threaded=False,)