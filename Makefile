PROJPATH = $(PWD)
PROJNAME = $(notdir $PROJPATH))
APPNAME  = "derive"
MK = ./mk

include $(MK)/*.mk
