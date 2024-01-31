from shodan import Shodan
import datetime
import os
 
def get_log_file_path():
    today = datetime.date.today()
    filename = f"{today}_shodan.log"
    file_path = os.path.join('/app/cti/elastic-stack-docker-part-one/filebeat_ingest_data/', filename)
    print(f"Log file patj: {file_path}")
    return file_path
#    return os.path.join('/app/cti/elastic-stack-docker-part-one/filebeat_ingest_data/', filename)
 
 
api_key = 'your_key'
api = Shodan(api_key)
print("Shodan API initialized.")
 
while True:
    log_file_path = get_log_file_path()
    with open(log_file_path, 'a') as log_file:
        print(f"Writing to log file: {log_file_path}")
        for banner in api.stream.alert(aid=None, timeout=None, raw=False):
            log_entry = str(banner) + '\n'
            log_file.write(str(banner) + '\n')
            print(f"Logged entry: {log_entry}")