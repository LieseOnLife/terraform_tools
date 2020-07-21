import subprocess
import shlex
from termcolor import colored

# This helps with when there is a for_each statement, so that we don't have to rewrite for_each variables
# Also, this makes it easier to do the weird quotes thing
variable1 = "\"variable1\""
variable2 = "\"variable2\""
variable3 = "\"variable3\""
variable4 = "\"variable4\""


# Replace Resources here for your own imports
RESOURCES = {
    "aws_default_security_group.default" : "sg-123434",
    "'aws_security_group.cloudcore["+variable1+"]'": "sg-98765",
    "'aws_security_group.cloudcore["+variable2+"]'" : "sg-095643",
}

# This can be terragrunt or terraform.  Whatever command you want to use, put it here
terra = "terragrunt import"

# Goes through
def module_import(resource, key):
    command = terra + " " + resource + " " + key  # Uncomment When you need a key
    # command = tgi + " " + resource  # Uncomment when you don't need a key
    print colored("Trying for "+resource,'green')
    subprocess.call(shlex.split(command))

for resource  in RESOURCES:
    module_import(resource, RESOURCES[resource])
