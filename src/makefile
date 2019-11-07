MDFILES=$(wildcard *.md)
OUTPUT=$(MDFILES:.md=.html)

.SUFFIXES: .md .html

.md.html:
	pandoc $< -s --template ../templates/lgpsi.html -o ../docs/$@ 



all: $(OUTPUT)


