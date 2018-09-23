import json, requests, platform, sys, time

class RaspberryApi:
    
    def __init__(self):
        self.cronKey = None
    
    def getCronKey(self):
        if self.cronKey is None:
            with open('settings.json') as file:
                settings = json.load(file)
            self.cronKey = settings['cron_key']
        return self.cronKey
    
    def consume(self):
        return requests.get(
        'http://keboca.com/api/v1/raspberry-pi',
        params={
            'system': platform.system(),
            'machine': platform.machine(),
            'platform': platform.platform(),
            'cron_key': self.getCronKey()
        },
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
        })
    
    def run(self):
        try:
            response = self.consume()
        except:
            print("Unexpected error:", sys.exc_info()[0])
        else:
            print('Notification made successfully.')
            if requests.codes.ok == response.status_code:
                print(response.json())
            else:
                print('Error: {0}'.format(response.text))
        finally:
            print("Start over...")
            time.sleep(1)
            self.run()

# Create new instance and run it.
pi = RaspberryApi()
pi.run()
