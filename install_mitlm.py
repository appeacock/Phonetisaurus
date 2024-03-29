import subprocess
import os

def install_mitlm():
    try:
        # Update package lists
        subprocess.check_call(['sudo', 'apt-get', 'update'])
        
        # Install necessary build tools
        subprocess.check_call(['sudo', 'apt-get', 'install', '-y', 'build-essential', 'autoconf', 'automake', 'libtool', 'git'])
        
        # Clone the mitlm repository
        subprocess.check_call(['git', 'clone', 'https://github.com/mitlm/mitlm.git'])
        
        # Change directory to mitlm
        os.chdir('mitlm')
        
        # Run autogen.sh to prepare the build environment
        subprocess.check_call(['./autogen.sh'])
        
        # Compile mitlm from source
        subprocess.check_call(['make'])
        
        # Install mitlm
        subprocess.check_call(['sudo', 'make', 'install'])
        
        print("MITLM installed successfully.")
        
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Call the install function
install_mitlm()
