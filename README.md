# About the Project

This project derives from my term project of the class Computing for Social Sciences at the University of Chicago. I later expanded it to serve my master’s thesis. In the paper, I tried to explore the inter-organizational social networks among Chinese ENGOs (CENGOs), and to theorize the genesis of their organizational structure.

The selection of these specific chinese organizations as my research subjects, in hope of finding the “origin of organizational forms”, is based on a simple assumption: most ENGOs in China are relevantly young (ranging from 1 to 10+ years old, centering around 5-6), due to China’s most recent emergence of civil society organizations and awareness. By examining current conditions of Chinese ENGOs, I believe I am researching on the very initial stage of a social sub system —— if I adopt historians’ view of time. Given the initial conditions are critical to any complex systems, I am convinced that this project bears significance for future studies on the organizational forms of Chinese ENGOs and beyond.

The social network data was collected via a self-designed survey distributed to Chinese ENGOs’ managers. I concurrently asked the respondents to indicate four types of relations they developed with other organizations: financial aid (the monetory circulation among the CENGOs), support (who they resort to when they need help), information (where do they get their information from) and collaboration (who they work with) —— the four types of interactions which dictate CENGOs’ organizational life. The idea of constructing multiple networks over simple networks is to best approximate and reproduce social interactions among organizations in their field.

Using the network data, along with other contextualized interview data, I find that in general CENGOs are self-organized into four categories based upon their structural positions in the multiple networks. Their organizational structures present similarity within each category while contrasting each other across groups, hinting a tendency of organizational differentiation, as well as tight coupling between structure and function in this young system. Detailed information and analysis can be found in my paper.




# How to Read

There are currently three folders and two scripts involved in this project:

<dl>
	<dt>prepare_network.py</dt>   
	<dd>This script converts text from .txt to .csv format for the convenience of analysis<dd>

	<dt>analyze_network.py</dt>
	<dd>This script calculates related centrality measures of targeted networks and draw graphics for the purpose of research</dd>

	<dt>Data Folder</dt>
	<dd>This folder stores raw relational data among CENGOs</dd>

	<dt>Outputs Folder</dt>
	<dd>This folder stores outputs of centrality measures of four networks. The data was later used in the paper for explanatory and theorizing purposes.</dd>

	<dt>Pics Folder</dt>
	<dd>This folder stores graphs of four networks.</dd>
</dl>




# Credits 

I would like to thank manlius for his help and support. His amazing project, MuxViz, enables me to do complex calculations, mapping and visualization of multiple networks. Please visit his page to appreciate his excellent work: https://github.com/manlius/muxViz.

Cited papers/books are included in the bibliography section of my paper. Please contact me for a copy: lichengzhu@uchicago.edu.