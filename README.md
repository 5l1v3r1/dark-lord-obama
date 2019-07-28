# Dark Lord Obama - Undetectable Pythonic Payload Generator

Chang Tan Lister
Lister Unlimited Cybersecurity Solutions, LLC.
changtan@listerunlimited.com

DLO generates a Pythonic reverse shell that as of July 29th, 2019, is undetectable on VirusTotal. It combines multiple won't-to-be-disclosed techniques (undiscloseable in detail) including but not limited to:

1. "Command Segmentation"
2. "AES Encryption" with a 32-bit key and a 16-bit initialization vector
3. Base64 Encoding - It was a necessity
4. Inline Python exec() functions, C asm() functions (will be added soon), Java/Jython, Cython, Ctypes

# Current usage

Currently it only works on targets that run Python. A cross-compilable and transpilable edition is in the works after DEFCON and after I pass the OSCP.

`python darklordobama-generator.py <LHOST> <LPORT>`

# Incoming features

1. Cross-compilation - Ideal targeted platforms, Android, iOS, MacOS (already possible with py2app), ARM/MIPS based routers and IoT devices
2. C2 Server - Encrypts a whole TLS 1.3 certificate within the payload, and attempts to negotiate a TLS session with the Command-and-Control Server (the payload does not have the key or IV, the server sends a CHALLENGE string containing it for the payload to decrypt the TLS cert), if a IP or host fails to provide the correct TLS certificate (handshake), the C2 Server immediately issues a permaban rule on IPTables (DROP packets)
3. "Steroid Injections" - Re-writable sections of memory occupied by the payload using statically defined functions, built in reverse-SSH tunnels, and SocketServer. Instantly grant your payload new abilities without having to re-touch the disk (it modifies a function that is holding a 5,000 byte buffer of \x90 NOP instructions and then lets you CALL it)
4. Dynamic DNS Support - With built-in dns resolver to ensure that you always use public DNS (1.1.1.1 or 8.8.8.8) to evade corporate DNS whitelisting
5. C2_Rotate Function - Using Ansible, Tensorflow, and Python, automate the spinning up of brand new Command-and-Control Servers, and immediately push a mass-update on all current bots to "rotate" to the new VPS. Requires Dynamic DNS subscription.
6. Built-in SSH client - Allow your payloads to create reverse SSH tunnels to tunnel out of restrictive firewalls (like a home NATed router)
7. ASM Interpreter - Run x86 Assembly Instructions or launch object .o files
