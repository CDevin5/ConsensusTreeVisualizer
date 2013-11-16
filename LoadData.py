### ConsensusTreeVisualizer, a Claremont Colleges Hackathon project.
### Dates: 15-16 November 2013
### Authors: Coline Devin, Benjamin Johnson, Rachel Sherman, Sophia Williams
### School: Harvey Mudd College

### LoadData.py
### Author: Benjamin Johnson
### Creates a window with controls for viewing trees

import ConsensusTrees
import TreeDrawer

def main():
    """ """
    for i in range(51,101):
        tree = ConsensusTrees.main(i,'bigData')+';'
        print 'bigData', i
        print tree
        filename = 'images/bigData-%03d'%i
        TreeDrawer.writeTreeImage(tree, filename)
    for i in range(51,101):
        tree = ConsensusTrees.main(i,'Caesal')+';'
        print 'Caesal', i
        print tree
        filename = 'images/Caesal-%03d'%i
        TreeDrawer.writeTreeImage(tree, filename)

if __name__ == "__main__":
    main()
