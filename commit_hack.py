import os
import random
from datetime import datetime, timedelta

# The file we will continuously modify to create diffs
file_name = "dummy.txt"

# Decide how far back you want to go (e.g., 180 days)
days_back = 10
start_date = datetime.now() - timedelta(days=days_back)

print(f"Generating commits starting from {start_date.strftime('%Y-%m-%d')}...")

for i in range(days_back):
    current_date = start_date + timedelta(days=i)
    
    # Randomize commits per day (0 to 4) so the graph looks organically active, not like a solid block
    num_commits = random.randint(0, 8)
    
    for j in range(num_commits):
        # Format the date specifically for Git's parser: YYYY-MM-DDTHH:MM:SS
        date_str = current_date.strftime('%Y-%m-%dT12:00:00')
        
        # Make a physical change to the dummy file so Git has something to track
        with open(file_name, "a") as file:
            file.write(f"Commit iteration {i}-{j} on {date_str}\n")
        
        # Stage the change
        os.system("git add .")
        
        # The Hack: Override Git's internal environment variables for the timestamps
        commit_cmd = f'GIT_AUTHOR_DATE="{date_str}" GIT_COMMITTER_DATE="{date_str}" git commit -m "Automated backend generation" --quiet'
        os.system(commit_cmd)

print("Done! All local commits generated.")
print("Run 'git push origin main' to send them to GitHub.")