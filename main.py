import eel

class EbayProduct:
    def __init__(self, url):
        self.url = url





if __name__ == "__main__":
    eel.init('web')
    size = (720, 600)
    eel.start('index.html', size=size)