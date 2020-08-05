import os
import requests


def get_all_droplets():
    url = 'https://api.digitalocean.com/v2/droplets/'
    r = requests.get(url, headers={'Authorization': 'Bearer %s' % os.getenv('DO_ACCESS_TOKEN')})
    droplets = r.json()
    droplet_list = []
    for i in range(len(droplets['droplets'])):
        droplet_list.append(droplets['droplets'][i])

    return droplet_list


def get_droplet(droplet):
    url = 'https://api.digitalocean.com/v2/droplets/' + str(droplet)
    r = requests.get(url, headers={'Authorization': 'Bearer %s' % os.getenv('DO_ACCESS_TOKEN')})
    droplet_data = r.json()

    return droplet_data['droplet']
