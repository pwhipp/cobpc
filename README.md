# cobpc
COBPC Member portal

All of the portal code and related documentation will go in this repository.

It may also include the canonical club documents, role definitions etc.

## Installation and deployment

These instructions are for installing on Debian 8 or Ubuntu 16.04 servers (later versions are probably ok).

### Prerequisites

- git
- python3.7

### Deployment

If deploying remotely, set up nginx and a separate user for the service (e.g. *cobpc*).
Ensure whatever user you are using has access to the [github repository](https://github.com/pwhipp/cobpc)

1. Create a virtual environment running python 3.7 e.g:

   ``virtualenv --python=`which python3.7` website``
1. Activate the environment (*website*)

   ``cd website && . bin/activate``
1. Clone the repo into a subfolder in ``website``

   ``git clone git@github.com:pwhipp/cobpc.git``
1. Link the environment set up into the virtual env

   ``ln -s ${VIRTUAL_ENV}/cobpc/deploy/postactivate bin && . bin/postactivate``
1. Install the requirements

   ``pip install -r cobpc/requirements.txt``
1. Create a local configuration (may want to edit it)

   ``cp cobpc/core/settings/includes/local.example.py local.py``
1. Set up the database

   ``django migrate``

1. Build the html documentation
   
   ``django devdoc --no_open``
   
1. For development you can now run the service and work on it. Run it with

   ``django runserver``
   
1. For production you need to ensure that the service is run in a more robust manner:

   1. Hook up nginx
   
      ``sudo ln -s /home/cobpc/website/cobpc/deploy/nginx.cfg /etc/nginx/sites-available/cobpc``
      
      ``sudo ln -s /etc/nginx/sites-available/cobpc /etc/nginx/sites-enabled``
      
      ``sudo systemctl reload nginx``

   1. Link the service file so systemD can find it, enable it and start it:
   
      ``sudo ln -s /home/cobpc/website/cobpc/deploy/cobpc.service /etc/systemd/system``
      
      ``systemctl start cobpc``
      
      ``systemctl enable cobpc``
      
   1. When updating or installing on production for the first time static files must be collected
    
      ``django collectstatic``