import subprocess
import os
import shutil

def is_mitlm_installed():
    """Check if mitlm is already installed and meets version requirements."""
    try:
        result = subprocess.check_output(['estimate-ngram', '--version'], stderr=subprocess.STDOUT)
        print("MITLM is already installed.")
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def user_decision(prompt):
    """Prompt the user for a decision and return True for 'yes' responses."""
    decision = input(prompt + " (y/n): ").strip().lower()
    return decision in ['y', 'yes']

def install_mitlm():
    """Install mitlm if it's not already installed or doesn't meet the version requirement."""
    if not is_mitlm_installed():
        try:
            mitlm_dir = 'mitlm'
            
            # Check if the mitlm directory already exists and ask the user for direction
            if os.path.exists(mitlm_dir):
                if user_decision("The 'mitlm' directory already exists. Do you want to remove it and proceed with a fresh clone?"):
                    print("Removing existing 'mitlm' directory.")
                    shutil.rmtree(mitlm_dir)
                else:
                    print("Exiting installation as per user decision. Please handle the 'mitlm' directory manually if needed.")
                    return
            
            # Update package lists
            subprocess.check_call(['sudo', 'apt-get', 'update'])
            
            # Install necessary build tools
            subprocess.check_call(['sudo', 'apt-get', 'install', '-y', 'build-essential', 'autoconf', 'automake', 'libtool', 'git'])
            
            # Clone the mitlm repository
            print("Cloning the 'mitlm' repository.")
            subprocess.check_call(['git', 'clone', 'https://github.com/mitlm/mitlm.git'])
            
            os.chdir(mitlm_dir)
            
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
