
import webbrowser
import time

url = 'www.terra.com.br'
webbrowser.register('vivaldi', None, webbrowser.BackgroundBrowser("C:\\Users\\Jacks.GUTTSPC\\AppData\\Local\\Vivaldi\\Application\\vivaldi.exe"))
webbrowser.get('vivaldi').open(url)

while True: 
    time.sleep(20) 
    webbrowser.get('vivaldi').open(url)