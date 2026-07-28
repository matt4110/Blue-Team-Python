import os 
import sys

log_events = []

def search_logs_for_ip(ip): 

    log_directory = "/var/log" 
    files = [os.path.join(dp, f) for dp, dn, filenames in os.walk(log_directory) for f in filenames if not f.endswith('.gz')]

    for file in files: 
        try: 
            with open(file, 'r', errors='ignore') as f:
                lines = f.readlines() 
                for line in lines: 
                    if ip in line: 
                        log_events.append((line.strip(), file))
        except Exception as e:
            log_events.append((f"Error in {file} file: {e}", file))

if __name__ == "__main__": 

    if len(sys.argv) > 1: 
        target_ip = sys.argv[1] 
    else:
        target_ip = input("Input IP Address: ")

    search_logs_for_ip(target_ip)

    log_events.sort()

    for item in log_events: 
        print(f"{item[0]} {item[1]}")