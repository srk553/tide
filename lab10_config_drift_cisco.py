import difflib
import os

# File paths
current_config_path = 'backups/csr1_running.txt'
golden_config_path = 'git_repo/csr1_running.txt'

# Check if files exist
if not os.path.exists(current_config_path) or not os.path.exists(golden_config_path):
    print("One or both config files are missing.")
    exit(1)

# Read configs
with open(current_config_path) as current_file:
    current_cfg = current_file.readlines()

with open(golden_config_path) as golden_file:
    golden_cfg = golden_file.readlines()

# Generate unified diff
diff = difflib.unified_diff(
    golden_cfg,
    current_cfg,
    fromfile='Golden Config',
    tofile='Live Config',
    lineterm=''
)

# Print the diff result
print("\n--- Configuration Drift Detected ---\n")
for line in diff:
    print(line)
