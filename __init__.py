import os
import sys
import filecmp
import shutil
import __main__
import json

python = sys.executable

# create config
if not os.path.isfile(os.path.join(os.path.dirname(os.path.realpath(__file__)),"config.json")):
    config = {
        "QWENVL_API_KEY": "your key"
    }
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),"config.json"), "w") as f:
        json.dump(config, f, indent=4)

#load config
with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),"config.json"), "r") as f:
    config = json.load(f)


from .QwenVL_API_Node import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS

# Combine the dictionaries
#NODE_CLASS_MAPPINGS = {**NODE_CLASS_MAPPINGS_G}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
