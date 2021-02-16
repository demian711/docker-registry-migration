#!/usr/bin/env python3

from config import *
from docker_requests import *
from termcolor import colored

if __name__ == "__main__":

    print(colored("Migration start at {}".format(start_time), 'yellow'))

    # Get all the images from source
    images = getallimages(registry_source)

    # Iterate over all images
    for image in images['repositories']:
        repository = getrepoinfo( image, registry_source )

        try:
            repositoryName = repository['name']
            repositoryTags = repository['tags']
        except KeyError:
            print(colored("Image '{}' doesn't have correct formated name".format(image), 'red'))

        try:
            for tag in repositoryTags:
                dockerpull( repositoryName, tag, registry_source )
                dockertag( repositoryName, tag, registry_source, registry_dest )
                dockerpush( repositoryName, tag, registry_dest )
                dockerremoveimage( repositoryName, tag, registry_source, registry_dest )
                print("-------")
        except TypeError:
                 print(colored("Image '{}' doesn't have any correct tag".format(image), 'red'))

    # Print finished datetime of migration
    finish_time = str(datetime.now().strftime("%D, %H:%M:%S"))
    print(colored("Migration finished at {}".format(finish_time), 'yellow'))