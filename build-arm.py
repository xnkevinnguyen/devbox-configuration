# This script loops through the Catalog directory and creates the azuredeploy.json files from the main.bicep files

import os
import subprocess

templates = []

catalog = os.path.realpath(os.path.dirname(__file__))

# loop through the directory and get the subdirectory (catalog item) names
with os.scandir(catalog) as s:
    for f in s:
        if f.is_dir():
            templates.append(f.name)

# for each catalog item, run az bicep build on the main.bicep file
for t in templates:
    print('Compiling template: {}'.format(t))
    subprocess.run(['az', 'bicep', 'build', '-f', '{}/{}/main.bicep'.format(catalog, t), '--outfile', '{}/{}/azuredeploy.json'.format(catalog, t)])
