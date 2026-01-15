Create virtual environment 
- python3 -m venv venv 
Create requirement.txt
- run pip install -r requirement.txt to install python packages 

Requirement 
- Make a tool that can extract the file format from tar.xz/gzip 
- Change permission to sos-folder
- Access the files within sos-folder
- Print the information from different file, info like RHEL,Kernel,Processor,taint etc

Backend
- Store this information and find the knowledgebase article,Bugzilla url, JIRA url or any solution article using Gemini

fronend 
- make a "drag and drop" or select attachement to upload kind of button to upload sosreport
- add submit button 
- add container text area to display the information and recommended solution/workaround url

what is sosreport:
The sos report command is a tool that collects configuration details, system information and diagnostic information from a Red Hat Enterprise Linux system. For instance: the running kernel version, loaded modules, and system and service configuration files. The command also runs external programs to collect further information, and stores this output in the resulting archive. The tool itself aims to collect as much diagnostic data as possible, while doing so in a reasonable time and space, and without a substantial impact to the system resources.