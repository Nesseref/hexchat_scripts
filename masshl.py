import hexchat

__module_name__ = 'masshl'
__module_author__ = 'Orc'
__module_version__ = '1.0'
__module_description__ = 'mass highlights'

full_name = "{} v{} by {}".format(__module_name__,__module_version__,__module_author__)
help_hook = "\"/masshl\" will highlight every nick in the current channel."

def masshl(word, word_eol, userdata):
	names = ""
	for i in hexchat.get_list("users"):
		names += i.nick + " "
	hexchat.command("say " + names)
	return hexchat.EAT_NONE
	
hexchat.hook_command("masshl", masshl, help=help_hook)
hexchat.prnt(full_name + " loaded.")