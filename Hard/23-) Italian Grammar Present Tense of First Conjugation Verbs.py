"""
In this challenge, you must build a function that inflects an infinitive regular Italian verb of
the first conjugation form to the present tense, including the personal subjective pronoun.

All first conjugation Italian verbs share the same suffix: ARE. The first thing to do is
separate the verb root from the suffix.

Root of "programmare" (to code) = "programm".
Root of "giocare" (to play) = "gioc".
For each subjective pronoun the root is combined
with a new suffix: see table below (pronouns are numbered for coding ease,
in real grammar they are grouped in singular and plural, both from first to third):

#	Pronoun	Suffix
1	Io (I)	o
2	Tu (You)	i
3	Egli (He)	a
4	Noi (We)	iamo
5	Voi (You)	ate
6	Essi (They)	ano
Present tense of verb "parlare" (to speak) for third pronoun:
Pronoun ("Egli") + Root ("parl") + Suffix ("a") = "Egli parla".
Present tense of verb "lavorare" (to work) for fourth pronoun:
Pronoun ("Noi") + Root ("lavor") + Suffix ("iamo") = "Noi lavoriamo".
There are two exceptions for present tense inflection:

If root ends with "c" or "g" the second and fourth pronoun suffixes add a "h" at the start:
"Attaccare" (to attack) = "Tu attacchi" (instead of "Tu attacci")
"Legare" (to tie) = "Noi leghiamo" (instead of "Noi legiamo")
If root ends with "i" the second and fourth pronoun suffixes lose the starting
"i" (so that second pronoun suffix disappears):
"Inviare" (to send) = "Noi inviamo" (instead of "Noi inviiamo")
"Tagliare" (to cut) = "Tu tagli" (instead of "Tu taglii")
"Mangiare" (to eat) = "Noi mangiamo" (instead of "Noi mangiiamo")
"Cacciare" (to hunt) = "Tu cacci" (instead of "Tu caccii")
Given a string verb being the infinitive form of the first conjugation
Italian regular verb, and an integer pronoun being the subjective personal
pronoun, implement a function that returns the inflected form as a string.

Examples
conjugate("programmare", 5) ➞ "Voi programmate"

conjugate("iniziare", 2) ➞ "Tu inizi"

conjugate("mancare", 4) ➞ "Noi manchiamo"
Notes
In the returned string, pronouns must be capitalized and verbs must be in lowercase,
separated by a space between them.
Curious fact: first conjugation (verbs ending in "are") is also called "the living conjugation",
because every new verb that enters the Italian dictionary is assigned to this category as a new
regular verb; it often happens for verbs "borrowed" from English and for informatical neologisms:
chattare, twittare, postare, spammare... will edabittare be the next?
"""

di = {
    1: ["Io ", "o"],
    2: ["Tu ", "i"],
    3: ["Egli ", "a"],
    4: ["Noi ", "iamo"],
    5: ["Voi ", "ate"],
    6: ["Essi ", "ano"]}


def conjugate(verb, pronoun):
    root = verb[:-3]
    if root[-1] in "cg":
        if pronoun in [2, 4]:
            root += "h"
    if root[-1] == "i":
        if pronoun in [2, 4]:
            root = root[:-1]
    return di[pronoun][0] + root + di[pronoun][1]


print(conjugate("programmare", 5))
