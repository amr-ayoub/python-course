import webbrowser



class Movie():
    class_var = 0
    
    
    def __init__(self,title,trailer):
        self.title = title
        self.trailer = trailer
        self.obj_var = 1
        

    def run_trailer(self):
        webbrowser.open_new(self.trailer)

    


    
    
