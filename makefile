
#############################################
# AUTHOR:	Christos Faloutsos
# DATE:		Sept. 2014
# PURPOSE:	runs a demo of Yuto's code
#############################################

DIR=sampledata
GRAPH=$(DIR)/graph
TRAINING=$(DIR)/training
TEST=$(DIR)/test
RESULT=result.out
PLOT=plot.dat

demo:
	python omniprop.py $(GRAPH) $(TRAINING) 1.0  > $(RESULT)
	python precision_at_p.py $(RESULT) $(TEST) > $(PLOT)

clean:
	\rm -f $(RESULT) $(PLOT)

spotless: clean
	\rm -f *.pyc
