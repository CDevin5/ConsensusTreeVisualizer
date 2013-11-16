### ConsensusTreeVisualizer, a Claremont Colleges Hackathon project.
### Dates: 15-16 November 2013
### Authors: Coline Devin, Benjamin Johnson, Rachel Sherman, Sophia Williams
### School: Harvey Mudd College

### TreeDrawer.py
### Author: Benjamin Johnson
### Draws consensus tress given various parameters.
### This is a (very) thin wrapper on the ete2 toolkit

from ete2 import Tree, TreeStyle
from datetime import datetime
import math

DEFAULT_HEIGHT = 512
DEFAULT_WIDTH = 512
DEFAULT_FORMAT = '.png'

IMAGE_DIR = 'images'

## Default style definitions

STYLE_BASIC = TreeStyle()

STYLE_NAMED = TreeStyle()
STYLE_NAMED.show_leaf_name = True

STYLE_LENGTHS = TreeStyle()
STYLE_LENGTHS.show_leaf_name = True
STYLE_LENGTHS.show_branch_length = True

DEFAULT_STYLE = STYLE_NAMED

##

def writeTreeImage(tree_string, filename=None,
                   height=DEFAULT_HEIGHT, width=DEFAULT_WIDTH,
                   style=DEFAULT_STYLE):
    """Writes out an image file with the tree.

    tree - the tree in newick format (as a string)
    filename - the filename for the tree to write out, excluding the extension
    height - the height of the image in pixels
    width - the width of the image in pixels
    style - the TreeStyle to use
    """
    if filename == None:
        timestamp = datetime.utcnow().strftime('%Y-%m-%d-%H%M%S')
            
        filename = 'TestTree-' + timestamp
    tree = Tree(tree_string)
    tree.render(filename + DEFAULT_FORMAT)
               # h=height, w=width, units='px',
               # tree_style=style)

def writeRandomSet(n_sizes=10, img_nums=range(51,101)):
    base_name = 'images/TestTree-%0' + str(len(str(max(img_nums)))) + 'd.png'
    for i in img_nums:
        t = Tree()
        t.populate(10, random_branches=True)
        t.render(base_name%i)

