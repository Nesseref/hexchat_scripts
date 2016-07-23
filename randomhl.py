import hexchat
import random

__module_name__ = 'randomhl'
__module_author__ = 'Orc'
__module_version__ = '1.0'
__module_description__ = 'random highlights n names highlights'

full_name = "{} v{} by {}".format(__module_name__,__module_version__,__module_author__)
help_hook = "\"/randomhl\" will highlight n random nicks in the current channel."

num_names = 5

def randomhl(word, word_eol, userdata):
	names = ""
	for i in range(num_names):
		names += random.choice(hexchat.get_list("users")).nick + " "
	hexchat.command("say " + names)
	return hexchat.EAT_NONE
	
hexchat.hook_command("randomhl", randomhl, help=help_hook)
hexchat.prnt(full_name + " loaded.")
