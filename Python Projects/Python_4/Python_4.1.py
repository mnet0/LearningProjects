fh = open("/home/mneto/Documents/MyGitHubProjects/LearningProjects/Python Projects/Python_4/mbox-short.txt")


for line in fh:
    
    line = line.rstrip()
    wds = line.split()
    
    # Guardian in a compound statement instead of having it before
    if len(wds) < 3 or wds[0] != 'From' :
        continue
    
    print(wds[2])