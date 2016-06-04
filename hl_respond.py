import hexchat
import random

__module_name__ = 'hl_respond'
__module_author__ = 'Orc'
__module_version__ = '1.0'
__module_description__ = 'responds to highlight in pm/channel'

full_name = "{} v{} by {}".format(__module_name__,__module_version__,__module_author__)

# set to true to respond in private message
# set to false to respond in channel
pm_response = False

# can add/modify quotes
quotes = ["something", "something else"]
# channels not to respond in
disabled_channels = ['#channame1', '#channame2']

def hl_respond(word, word_eol, userdata):
	if hexchat.get_info('channel') not in disabled_channels:
		# respond to hling user in pm
		if pm_response:
			hexchat.command("PRIVMSG " + word[0] + " :" + random.choice(quotes))
		# respond to hling user in channel
		else:
			hexchat.command("say " + random.choice(quotes))
	return hexchat.EAT_NONE
	
hexchat.hook_print('Channel Msg Hilight', hl_respond)
hexchat.prnt(full_name + " loaded.")