import subprocess

def install_sslscan():
    try:
        # Install sslscan using package manager (apt-get on Debian/Ubuntu)
        subprocess.run(['apt-get', 'install', '-y', 'sslscan'])
        print("sslscan installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred during installation: {e}")
        print(e.stderr)

def check_ssl_vulnerabilities():
    try:
        # Prompt the user to enter the target URL
        target_url = input("Enter the target URL: ")
        
        # Run the sslscan command with the target URL
        result = subprocess.run(['sslscan', target_url], capture_output=True, text=True)
        
        # Print the scan results
        print(result.stdout)
        
    except FileNotFoundError:
        print("sslscan command not found. Installing sslscan...")
        install_sslscan()
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
        print(e.stderr)

# Call the function to check SSL vulnerabilities
check_ssl_vulnerabilities()
