def average_above_zero(tab):
	"""
	brief: computes ten average of the list
	args:
		tab: a list of numeric value expects at leas one positive value
	return:
		the computed average
	raises:
		ValueError if expected a list as input
		ValueError if no positive value found
	"""
	if not(isinstance(tab, list)):
		raise ValueError('Expected a list as input')

	valSum = 0.0
	nPositiveValues = 0

	for i in range(len(tab)):
		if tab[i] > 0:
			valSum += float(tab[i])
			nPositiveValues += 1

	if nPositiveValues <= 0:
		raise ValueError('No positive value found')
	
	avg = valSum/nPositiveValues

	return avg

def test_average_above_zero():
	assert average_above_zero([12, 0, 20, -5]) == 17.0

def maximum_value(tab):
	"""
	brief: return maximum value of the list
	args:
		tab: a list of numeric value expects at leas one positive value
	return:
		the max value of the list
		the index of the max value
	raises:
		ValueError if expected a list as input
		ValueError if no positive value found
	"""
	if not(isinstance(tab, list)):
		raise ValueError('Expected a list as input')

	valMax = 0.0
	valMaxIndex = -1;
	nPositiveValues = 0

	for i in range(len(tab)):
		if tab[i] >= 0 and tab[i] > valMax:
			valMax = float(tab[i])
			valMaxIndex = i
			nPositiveValues += 1

	if nPositiveValues <= 0:
		raise ValueError('No positive value found')

	return valMax, valMaxIndex

notes = [12, 0, 20, -5]

print(average_above_zero(notes))
print(maximum_value(notes))
