#!/usr/bin/env python3

import requests
import subprocess
import sys
import requests
from config import *
from termcolor import colored

# Get all images for a given Registry
def getallimages(source):
    r = requests.get("https://{}/v2/_catalog?n=1000".format(registry_source), verify=False)
    images = r.json()
    return images

# Get all available images for a given image
def getrepoinfo(image, source):
    print(colored("Getting available tags for image '{}'".format(image), 'cyan'))
    request = requests.get("https://{}/v2/{}/tags/list?n=1000".format( source,image ), verify=False)
    repository = request.json()
    return repository

# Docker pull specified image and version
def dockerpull( image, tag, source ):
    print(colored("Pulling docker image '{}:{}'".format( image,tag ), 'blue'))
    subprocess.call(["/usr/bin/docker", "pull", "{}/{}:{}".format( source,image,tag )])
    print(colored("docker image '{}:{}' pulled correctly".format( image,tag ), 'green'))
    return

# Change tag of speficied image and version, ready to push to new Registry
def dockertag( image, tag, source, dest ):
    print(colored("Tagging docker image '{}:{}'".format( image,tag ), 'blue'))
    subprocess.call(["/usr/bin/docker", "tag", "{}/{}:{}".format( source,image,tag ), "{}/{}:{}".format( dest,image,tag )])
    print(colored("docker image '{}:{}' tagged correctly".format( image,tag ), 'green'))
    return

# Docker push to the new Registry
def dockerpush( image, tag, dest ):
    print(colored("Pushing docker image '{}:{}'".format( image,tag ), 'blue'))
    subprocess.call(["/usr/bin/docker", "push", "{}/{}:{}".format( dest,image,tag )])
    print(colored("docker image '{}:{}' pushed correctly".format( image,tag ), 'green'))
    return

# Remove already migrated image from local
def dockerremoveimage( image, tag, source, dest ):
    print(colored("Removing already migrated image '{}:{}'".format( image,tag ), 'blue'))
    subprocess.call(["/usr/bin/docker", "image", "rm", "-f", "{}/{}:{}".format( source,image,tag )])
    subprocess.call(["/usr/bin/docker", "image", "rm", "-f", "{}/{}:{}".format( dest,image,tag )])
    print(colored("docker image '{}:{}' already purged from local".format( image,tag ), 'green'))
    return