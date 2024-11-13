import os
import glob

def aggregate_logs(log_directory):
    log_files = glob.glob(os.path.join(log_directory, '*.log'))
    all_logs = []
    
    for log_file in log_files:
        with open(log_file, 'r') as file:
            logs = file.read()
            all_logs.append(logs)
            # filter out the log that show the error 500
    
    return '\n'.join(all_logs)

# Example usage
log_directory = '/var/log/my_application'
aggregated_logs = aggregate_logs(log_directory)
print(aggregated_logs)