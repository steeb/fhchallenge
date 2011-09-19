#!/usr/bin/python
# -*- coding: latin-1 -*-

import random

fragen=["Geht zum Allgemeinen Studierenden-Ausschuss (AStA) und lasst euren Rallyebogen abstempeln.",
"Geht zum Studierendensekreteriat und bringe einen Antrag auf ... mit.",
"Geht zum Fitnesskeller, zähle die Lampen an der Decke des Fitnessbereiches.",
"Geht zum Dekanat des Fachbereiches, wie sind die Öffnungszeiten?",
"Geht zum Büro von Prof. Engels, welcher Raum?, welcher Forschungsbereich?, welches Fach im ersten Semester?",
"Geht zur Tischtennisplatte, welches Dezernat hat an der TT-Platte einen Hinweis auf Brandschutz angebracht?",
"Sucht den Grundstein des Neubau 1 und sagt aus welchem Material er ist.",
"Geht zum eXwerk (D -1.01) und bringt ein Foto des Space Invaders mit.",
"Wieviel Kaffeespezialitäten bietet euch die helle Kaffemaschine in der Mensa in Neubau 1?",
"Wieviele Kopierer/Scanner befinden sich im Untergeschoss der Bibliothek?",
"Überwelchen Kommunikationskanal kommuniziert die FSV am schnellsten Neuigkeiten?"]

random.shuffle(fragen)

print '''\\documentclass[a4paper,15pt]{scrartcl}
\\usepackage[utf8]{inputenc}
\\usepackage[ngermanb]{babel}
\\usepackage{geometry}
\\usepackage{graphicx}

\\pagestyle{empty}
\\geometry{a4paper,left=2cm,right=2cm,top=1cm,bottom=2cm} 

\\renewcommand{\\familydefault}{\sfdefault}
\\begin{document}
Gruppenname {\\tiny(Kreativität bringt Punkte)}:\hrulefill
Studiengang:\hrulefill
\\\\
\\\\
{\huge Erstsemester Rallye Informatik}
\\\\
\\\\

Hallo und herzlich Willkommen im Fachbereich Informatik. Um den Fachbereich und die Fachhochschule besser kennen zulernen, haben wir uns diese Rallye überlegt.
Auf der Rückseite findet ihr einen Plan, mit dem ihr euch ein wenig orientieren könnt.\\\\

Da die höheren Semeser, vorallem im Fachbereich, Klausuren schreiben, bearbeitet die Rallye bitte in angemessener Lautstärke. Nun aber viel Spaß, ihr solltet euch in Gruppen bis zu 5 Leuten auf den Weg machen und diesen Bogen in maximal einer Stunde bearbeitet und in eurer Fachschaftsvertretung abgegeben haben. Als ersten Gewinn, gibts leckere Würstchen. Dort prämieren wie auch die Sieger.

\\begin{enumerate}'''

for element in fragen:
	print "\\item " + element

print '''\end{enumerate}

\\newpage
\\begin{center}
	\\includegraphics[scale=3]{karte.jpg}
\\end{center}

\end{document}'''
