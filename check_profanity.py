import urllib

def read_file():
    file_handle = open("C:\Users\Amr\Downloads\movie_quotes.txt")
    content = file_handle.read()
    check_content(content)
    #print(content)
    file_handle.close()


def check_content(content_to_check):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+content_to_check)
    response = connection.read()
    print(response)
    connection.close()

read_file()
