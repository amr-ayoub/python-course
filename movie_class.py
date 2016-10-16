import webbrowser



class Movie():
    def __init__(self,title,trailer):
        self.title = title
        self.trailer = trailer

    def run_trailer(self):
        webbrowser.open_new(self.trailer)

    


    
    
