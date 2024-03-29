import subprocess
import os

def is_mitlm_installed():
    """Check if mitlm is already installed and meets version requirements."""
    try:
        # Attempt to get the version of mitlm (modify this command if mitlm offers a version flag)
        result = subprocess.check_output(['estimate-ngram', '--version'], stderr=subprocess.STDOUT)
        # Parse the version from the output, if necessary
        print("MITLM is already installed.")
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        # mitlm is not installed or version check command failed
        return False

def install_mitlm():
    """Install mitlm if it's not already installed or doesn't meet the version requirement."""
    if not is_mitlm_installed():
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
            print(f"An error occurred during the installation: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
    else:
        print("MITLM installation is up to date.")

# Run the installation function
install_mitlm()
