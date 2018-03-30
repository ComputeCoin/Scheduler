"""
This module is the read and write gateway between the scheduler and the
database. Any data that the scheduler need to access, will be requested
through this gateway, and sent back through this gateway.

This module is for read and write access to data that is not considered
CLOUD DATA!!

This module contains the method of the form:
    (Scheduler requests CloudData) -> (Cloud returns CloudData)

Example:
    | Request            | Return          |
    | get User history   | history of user |
"""


def get_user_history(id):
    pass