# Just importing the language
# Because this is the shell, not the language
import LiteScript

# Importing the version and the date
from LiteScript import version, date

# Just some printing
print("LiteScript " + version + " (Language Creation/" + version + ". " + date + ")\nType some cool and fun stuff!")

# The real fun begins here :D
while True:
	text = input('>>> ')
	if text.strip() == "": continue
	result, error = LiteScript.run('<stdin>', text)

	# This shows if there was an error
	if error:
		print(error.as_string())
	# Else if there is no error then run the thing you typed
	elif result:
		if len(result.elements) == 1:
			print(repr(result.elements[0]))
		else:
			print(repr(result))