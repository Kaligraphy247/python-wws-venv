from poly import *

"""
The *pathspec.patterns* package contains the pattern matching
implementations.
"""

# Load pattern implementations.
from . import gitwildmatch

# DEPRECATED: Expose the `GitWildMatchPattern` class in this module for
# backward compatibility with v0.5.
from .gitwildmatch import GitWildMatchPattern


res = worker(Request(json.loads(sys.stdin.read())))
print(res.to_json())
