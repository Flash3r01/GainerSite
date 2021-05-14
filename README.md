# GainerSite

The GainerSite does not serve a specific purpose.  
She is being developed just for fun and to learn.  
The features and contents of this website are not
planed. She just grows organically and gets fun and
interesting features as time goes on.

If you are interested in this project, feel free to
contact me.

## Development/Debugging

The simplest way of debugging the website while developing is by running a *start_debug* Script.

**This should not be used for production environments!**

## Production Setup

This website is set up to run with Gunicorn and preferably with nginx.

### 1. Getting the newest stable sources

The stable branch is __not__ "main", but "production". To get the source files just from that branch, run:

`git clone -b production --single-branch https://github.com/Flash3r01/GainerSite.git gainerSite`

### 2. Setting up a virtual environment

  - Create a virtual environment for python with:  
  `python3 -m venv .venv`

  - Activate the virtual environment (Linux):  
  `. .venv/bin/activate`

  - Install the required modules:  
  `pip install -r requirements.txt`

### 3. Starting the website via Gunicorn

Start Gunicorn with your preferred options.  
Example:
`gunicorn -bind 0.0.0.0:5000 wsgi:app`

The website should now be served to clients who want to access it on port 5000.  
If you want the website to be controlled by services, [DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-20-04-de) has a great article, that also served as a basis for this README.