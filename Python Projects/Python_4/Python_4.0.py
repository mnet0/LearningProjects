fh = open("/home/mneto/Documents/MyGitHubProjects/LearningProjects/Python Projects/Python_4/mbox-short.txt")

for line in fh:
    linestriped = line.rstrip()
    print(linestriped.upper())