import re

output = """
blacklist list of persons who are disapproved
of and are punished, such as by being refused

jobs (p. 406)

blitzkrieg name given to the sudden, violent |
offensive attacks the Germans used during World

War II; “lightning war” (p. 367)

blockade cut off an area by means of troops or
warships to stop supplies or people from coming in
or going out; to close off a country’s ports (pp. 35,

466)

border ruffian Missourian who traveled in armed
groups to vote in Kansas’s election during the

mid-1850s (p. 13)

border state state between the North and the
South that was divided over whether to stay

in the Union or join the Confederacy (p. 33)

bounty money given as a reward, such as to
encourage enlistment in the army (p. 54)

boycott to refuse to use in order to show disap-
proval or force acceptance of one’s terms (p. 436)

budget deficit the amount by which government
spending exceeds revenue (p. 541)"""

delimiter = "*-*"
text_delimiter = "[(][^(]*[)]"

flat = output.replace('\n',' ')
entries = re.split("[(][^(]*[)]", flat)

with open("defs.txt", "w") as fh:
    for entry in entries:
        if entry.strip() == '':
            continue

        split = entry.strip().split(" ")

        fh.write("{}{}{}\n".format(split[0], delimiter, " ".join(split[1:])))
