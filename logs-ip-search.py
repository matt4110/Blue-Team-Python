import os 

def search_logs_for_ip(ip): 

    log_directory = "/var/log" 
    files = [os.path.join(dp, f) for dp, dn, filenames in os.walk(log_directory) for f in filenames if not f.endswith('.gz')]

    for file in files: 
        try: 
            with open(file, 'r', errors='ignore') as f:
                lines = f.readlines() 
                for line in lines: 
                    if ip in line: print(f"[{file}] {line.strip()}") 
        except Exception as e:
            print(f"Error in {file} file: {e}") 

if __name__ == "__main__": 

    target_ip = input("Input IP Address: ")     
    search_logs_for_ip(target_ip)