import sys
import subprocess

def send_festival_command(command):
    festival_process = subprocess.Popen(['festival', '--interactive'],
                                        stdin=subprocess.PIPE,
                                        stdout=subprocess.PIPE,
                                        stderr=subprocess.PIPE,
                                        universal_newlines=True)

    festival_process.stdin.write(command + '\n')
    festival_process.stdin.flush()

    output = festival_process.stdout.read()

    # Send the quit command to terminate Festival
    festival_process.stdin.write('(quit)\n')
    festival_process.stdin.flush()

    festival_process.terminate()


# Example usage
command = '(voice_cmu_us_rms_cg)(SayText "Hello, world!")'
output = send_festival_command(command)

sys.exit()  # Terminate the entire Python program
