import win32evtlog
import win32evtlogutil

def search_event_logs_for_ip(target_ip):
    logs = ['Application', 'Security', 'System']
    
    for log in logs: 
        try: 
            hand = win32evtlog.OpenEventLog(None, log) 
            flags = win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ 
            total = win32evtlog.GetNumberOfEventLogRecords(hand) 
    
            while True: 
                events = win32evtlog.ReadEventLog(hand, flags, 0) 
        
                if not events: 
                    break 
        
                for event in events: 
                    data = win32evtlogutil.SafeFormatMessage(event, log) 
                    if target_ip in data: 
                        print(f"[{log}] {data}") 
        except Exception as e: 
            print(f"Error in {log} log: {e}") 

if __name__ == "__main__": 
    target_ip = input("Input IP Address: ")    
    search_event_logs_for_ip(target_ip)